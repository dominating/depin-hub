# Duino-Coin (DUCO) ESP32-S2 Web Flashing Guide

This guide explains how to configure the official Duino-Coin ESP32 firmware with your Wi-Fi and wallet details, and how to flash it using the extremely easy browser-based Web UI.

## 1. Configure Your Credentials
Unlike NerdMiner, the standard Duino-Coin firmware requires you to hardcode your Wi-Fi and wallet credentials into the code *before* you compile it.

If you are compiling from source (using PlatformIO or Arduino IDE), open the `Settings.h` file and update these specific variables:

```cpp
// Change to your Duino-Coin wallet username
extern char *DUCO_USER = "Your_Username_Here";

// Change to your Wi-Fi network name
extern const char SSID[] = "Your_WiFi_SSID";

// Change to your Wi-Fi password
extern const char PASSWORD[] = "Your_WiFi_Password";
```
*Note: Leave `MINER_KEY = "None";` unless you specifically set up a mining key in your Duino-Coin web wallet.*

Once you've entered your details, compile the project to generate your `.bin` file.

## 2. Flash Using the Web UI (Easiest Method)
You do not need to install Python or use the command line (`esptool.py`) to flash your ESP32-S2. You can flash the compiled `.bin` file directly from your browser.

1. Open Google Chrome or Microsoft Edge (Web Serial is required, which Safari/Firefox do not support).
2. Go to the official **[Espressif Web Flasher (esptool-js)](https://espressif.github.io/esptool-js/)**.
3. Plug your ESP32-S2 into your computer via USB. *(If it's not recognized, hold the `BOOT` button on the board while plugging it in).*
4. Change the **Baudrate** dropdown to `115200`.
5. Click the **Connect** button and select the USB/COM port for your ESP32 from the browser popup.
6. In the **Program** section that appears:
   - Set the **Flash Address** to `0x0`.
   - Click **Choose File** and select your compiled `.bin` file.
7. Click **Program** and wait for the progress bar to reach 100%.

## 3. Monitor Your Miner
Once the flashing is complete, the ESP32-S2 will automatically reboot, connect to your Wi-Fi network, and begin mining.

You can verify that it is submitting shares by logging into your [Duino-Coin Web Wallet](https://wallet.duinocoin.com/) and checking the **Miners** tab.