# ESP32-S2 Digibyte Mining Guide (NerdMiner V2/NM-TV)

This guide walks through flashing an ESP32-S2 dongle with NerdMiner V2 (or NM-TV) firmware, configured to connect to a Digibyte (DGB) SHA-256 solo or low-hash pool. 

While NerdMiner is typically used for Bitcoin lotteries, Digibyte's multi-algo approach includes SHA-256, allowing these ultra-low-power devices to mine DGB directly on compatible pools.

## 1. Requirements

- ESP32-S2 USB Dongle (or any ESP32-S2/S3 board)
- A PC/Mac/Linux machine for flashing
- Chrome/Edge browser (for Web Flasher) OR `esptool.py` installed
- A Digibyte Wallet Address (e.g., from an exchange or official DGB wallet)

## 2. Choosing a Pool

You need a pool that supports low-difficulty SHA-256 for Digibyte. Solo mining or standard DGB pools can be used depending on network difficulty.
Example pools:
- `sha256.dgb256.online:3333` (Example solo/low diff pool)
- `stratum+tcp://sha256.eu.mine.zergpool.com:3434` (Auto-exchange pools that pay out in DGB)

*Check miningpoolstats.stream/digibyte-sha256 for active SHA-256 DGB pools.*

## 3. Flashing the Firmware

You do not need to install Python or use the command line (`esptool.py`) to flash your ESP32-S2. You can flash the compiled `.bin` file directly from your browser.

1. Download the custom compiled firmware from the DePIN Hub homepage.
2. Open Google Chrome or Microsoft Edge (Safari/Firefox do not support Web Serial).
3. Go to the official **[Espressif Web Flasher (esptool-js)](https://espressif.github.io/esptool-js/)**.
4. Plug your ESP32-S2 into your computer via USB. *(If it's not recognized, hold the `BOOT` button on the board while plugging it in).*
5. Change the **Baudrate** dropdown to `115200`.
6. Click the **Connect** button and select the USB/COM port for your ESP32 from the browser popup.
7. In the **Program** section that appears:
   - Set the **Flash Address** to `0x0`.
   - Click **Choose File** and select your downloaded `nerdminer-dgb-merged.bin` file.
8. Click **Program** and wait for the progress bar to reach 100%.

## 4. Configuration

1. After flashing, unplug and replug the ESP32-S2.
2. Connect to the new Wi-Fi network: **NerdMinerAP** (Password: `MineYourCoins`).
3. A captive portal will pop up. If not, browse to `192.168.4.1`.
4. Enter your configuration:
   - **SSID & Password:** Your local Wi-Fi network credentials.
   - **Pool URL:** `sha256.eu.mine.zergpool.com`
   - **Pool Port:** `3434`
   - **Your BTC/DGB Address:** Your Digibyte Wallet Address (Note: some pools like Zergpool require putting your payout coin in the password field: `c=DGB`). If mining directly to a DGB SHA256 pool, just use your DGB address as the username.
   - **Password:** `c=DGB,mc=DGB` (if using auto-exchange pool) or `x` for standard pools.

5. Click **Save** and wait for the device to reboot.

## 5. Monitoring

Your ESP32-S2 will now connect to your Wi-Fi and begin hashing. The NM-TV interface (or standard NerdMiner screen if using a board with a display) will show your current hash rate (typically ~40-60 kH/s on ESP32-S2). 

Check your pool's dashboard by entering your wallet address to see live statistics and payouts.