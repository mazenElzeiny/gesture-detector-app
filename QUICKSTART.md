# Quick Start Guide

Get your Gesture Detector app up and running in 5 minutes!

## Prerequisites

- Android phone or tablet
- HC-06 or HC-05 Bluetooth module
- Microcontroller (Arduino, ESP32, etc.) or USB-to-Serial adapter

## Step 1: Build the App (5 minutes)

### Option A: Using Pre-built APK
Download the APK from the releases page and skip to Step 2.

### Option B: Build from Source
```bash
# Install buildozer
pip install buildozer

# Clone the repository
git clone https://github.com/mazenElzeiny/gesture-detector-app.git
cd gesture-detector-app

# Build the APK
buildozer android debug

# APK will be in bin/ directory
```

## Step 2: Install on Android (2 minutes)

1. Transfer the APK to your Android device
2. Enable "Install from Unknown Sources"
3. Tap the APK file and install
4. Grant Bluetooth and Location permissions when prompted

## Step 3: Pair HC-06 Module (2 minutes)

1. Power on your HC-06/HC-05 module
2. Open Android Settings → Bluetooth
3. Turn on Bluetooth if not already enabled
4. Tap "Pair new device"
5. Select your HC-06 module from the list
6. Enter PIN (usually `1234` or `0000`)
7. Wait for "Paired" status

## Step 4: Connect and Test (1 minute)

1. Open the Gesture Detector app
2. Tap "Connect to HC-06"
3. Wait for "Connected!" status
4. Send test commands from your device:
   - Send `L` → See blue left arrow
   - Send `R` → See green right arrow
   - Send `S` → See orange static indicator

## Arduino Example Code

Quick test setup using Arduino:

```cpp
// Gesture Detector Test - Arduino
// Connect HC-06: TX->RX(pin 10), RX->TX(pin 11), VCC->5V, GND->GND

#include <SoftwareSerial.h>

SoftwareSerial bluetooth(10, 11); // RX, TX

void setup() {
  bluetooth.begin(9600);
  Serial.begin(9600);
  Serial.println("Gesture Test Ready!");
}

void loop() {
  // Test sequence: Left -> Right -> Static
  bluetooth.print('L');
  Serial.println("Sent: L (Left)");
  delay(2000);
  
  bluetooth.print('R');
  Serial.println("Sent: R (Right)");
  delay(2000);
  
  bluetooth.print('S');
  Serial.println("Sent: S (Static)");
  delay(2000);
}
```

Upload this code to test the app automatically!

## Expected Results

✅ **Successful Connection**:
- Status shows "Connected!"
- Connect button becomes disabled
- Disconnect button becomes enabled
- Background changes to orange (Static)

✅ **When Sending 'L'**:
- Background turns blue
- Icon shows `<--`
- Text shows "LEFT"

✅ **When Sending 'R'**:
- Background turns green
- Icon shows `-->`
- Text shows "RIGHT"

✅ **When Sending 'S'**:
- Background turns orange
- Icon shows `||`
- Text shows "STATIC"

## Command Cheat Sheet

| Command | Gesture | Visual |
|---------|---------|--------|
| `L` or `l` | Left | Blue, `<--` |
| `R` or `r` | Right | Green, `-->` |
| `S` or `s` | Static | Orange, `\|\|` |

## Troubleshooting Quick Fixes

❌ **"HC-06 not paired"**
→ Pair the device in Bluetooth settings first

❌ **"Enable Bluetooth first"**
→ Turn on Bluetooth in settings

❌ **Connection fails**
→ Make sure HC-06 is powered on and not connected elsewhere

❌ **No response to commands**
→ Check baud rate is 9600 and you're sending L/R/S

## Next Steps

- Integrate with your gesture recognition system
- Modify Arduino code for actual gesture sensors
- Customize the app colors and icons (edit main.py)
- Add more gesture types if needed

## Resources

- [Full README](README.md) - Complete documentation
- [Architecture Guide](ARCHITECTURE.md) - Technical details
- [Troubleshooting](TROUBLESHOOTING.md) - Detailed problem solving

## Support

Having issues? Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) or open an issue on GitHub!

---

**That's it!** You now have a working gesture detector app. 🎉
