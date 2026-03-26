#!/usr/bin/env python3
import json
import time
import os
import re
from playwright.sync_api import sync_playwright

COOKIE_FILE = "twitter_cookies.json"
HTML_FILE = "../index.html"
SEARCH_URL = "https://x.com/search?q=(%23DePIN%20OR%20%23Crypto%20OR%20%23Mining)%20(%23Giveaway%20OR%20%23Airdrop)%20min_faves%3A50%20within_time%3A24h&src=typed_query&f=top"

def run_scraper():
    # Setup your X cookies file in depin-hub/scripts/twitter_cookies.json
    if not os.path.exists(COOKIE_FILE):
        print(f"Error: {COOKIE_FILE} not found. Waiting for burner account setup.")
        return []

    try:
        with open(COOKIE_FILE, "r") as f:
            cookies = json.load(f)
    except Exception as e:
        print(f"Failed to read cookies: {e}")
        return []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        context.add_cookies(cookies)
        page = context.new_page()
        
        print(f"Navigating to: {SEARCH_URL}")
        page.goto(SEARCH_URL, wait_until="networkidle")
        time.sleep(5)  # Wait for React to render

        try:
            page.wait_for_selector('article[data-testid="tweet"]', timeout=15000)
        except Exception:
            print("Failed to find tweets. Check if cookies are expired or layout changed.")
            browser.close()
            return []

        tweets = page.query_selector_all('article[data-testid="tweet"]')
        extracted = []
        
        for tweet in tweets[:6]: # Get top 6
            try:
                # Text
                text_el = tweet.query_selector('div[data-testid="tweetText"]')
                text = text_el.inner_text() if text_el else ""
                
                # Link
                time_el = tweet.query_selector_all('time')
                link = ""
                if time_el:
                    parent_a = time_el[0].evaluate_handle("el => el.closest('a')")
                    if parent_a:
                        link = parent_a.get_property("href").json_value()
                
                # Author
                author_el = tweet.query_selector('div[data-testid="User-Name"]')
                author = author_el.inner_text().split('\n')[0] if author_el else "Unknown"

                if len(text) > 10 and link:
                    extracted.append({
                        "author": author,
                        "text": text[:150] + "..." if len(text) > 150 else text,
                        "link": link
                    })
            except Exception:
                continue

        browser.close()
        return extracted

def update_html(giveaways):
    if not giveaways:
        return

    html_blocks = []
    for g in giveaways:
        html_blocks.append(f'''
                <!-- GIVEAWAY ITEM -->
                <div class="p-4 bg-[#161b22] border border-gray-800 rounded-md hover:border-[#58a6ff] transition group flex flex-col justify-between min-h-[140px]">
                    <div>
                        <p class="text-sm font-bold text-white mb-2 truncate" title="{g['author']}">{g['author']}</p>
                        <p class="text-xs text-gray-400 mb-4 line-clamp-3">{g['text']}</p>
                    </div>
                    <a href="{g['link']}" target="_blank" class="mt-auto text-xs font-mono text-[#58a6ff] hover:text-white transition group-hover:underline">Enter Giveaway →</a>
                </div>''')

    combined_html = "\n".join(html_blocks)
    
    # Needs absolute pathing if running from sub-dir
    script_dir = os.path.dirname(os.path.realpath(__file__))
    html_path = os.path.join(script_dir, HTML_FILE)

    with open(html_path, 'r') as f:
        html = f.read()

    pattern = re.compile(r'(<!-- GIVEAWAYS_START -->)(.*?)(<!-- GIVEAWAYS_END -->)', re.DOTALL)
    new_html = pattern.sub(rf'\1\n{combined_html}\n                \3', html)

    with open(html_path, 'w') as f:
        f.write(new_html)
    
    print(f"Successfully injected {len(giveaways)} giveaways into index.html")

if __name__ == "__main__":
    giveaways = run_scraper()
    if giveaways:
        update_html(giveaways)
