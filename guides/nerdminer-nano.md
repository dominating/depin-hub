# Nano (XNO) Mining with ESP32-S2 (NerdMiner)

You can use your ESP32-S2 to mine Nano (XNO) using auto-exchange pools that accept SHA-256 hashes and pay out in Nano. Because the ESP32 has a very low hash rate (~50-70 kH/s), it is critical to use a pool that supports **low-difficulty shares**.

While **Unmineable** is popular, its SHA-256 pool is tuned for ASICs and the difficulty is too high for an ESP32 to ever submit a share. Instead, we highly recommend **Prohashing**, which allows you to manually set an ultra-low difficulty and pays out directly in Nano (XNO) with zero fees.

## 1. Firmware Requirements
You do not need special "Nano" firmware! You will use the exact same highly optimized **ZY ESP32-S2 NerdMiner V2** firmware we compiled for Digibyte.

[Download the Optimized .bin Here](/firmware/s2/nerdminer-dgb-merged.bin)

## 2. Setting Up the Pool (Prohashing)
Prohashing is the best "Unmineable-style" alternative for low-power devices because of its custom difficulty settings.

1. Create a free account at [Prohashing.com](https://cryptol.ink/jTIGYV
2. Go to **Payout Options** and add your Nano (XNO) wallet address. Set the payout proportion to 100%. Nano has no transaction fees, so daily minimum payouts are incredibly low.

## 3. Configuring the ESP32
1. Flash your ESP32-S2 using the Web Flasher or `esptool.py`.
2. Connect to the **NerdMinerAP** Wi-Fi network (Password: `MineYourCoins`).
3. In the captive portal (or at `192.168.4.1`), enter your network details and the following pool configuration:

- **Pool URL:** `prohashing.com`
- **Pool Port:** `3333`
- **Username:** `[Your Prohashing Username]`
- **Password:** `a=sha256 n=ESP32 d=0.0001`

*(The `d=0.0001` in the password forces the pool to accept ultra-low difficulty shares, ensuring your ESP32-S2 actually registers work!)*

## 4. Alternative: Unmineable (Not Recommended for ESP32)
If you absolutely want to try Unmineable, use these settings. Note that you may run for days without submitting a valid share due to the ASIC-level difficulty.

- **Pool URL:** `sha256.unmineable.com`
- **Pool Port:** `3333`
- **Username:** `NANO:[Your_Nano_Address].ESP32`
- **Password:** `x`