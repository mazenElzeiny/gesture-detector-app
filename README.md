# Gesture Detector App

A mobile Android app that receives gesture commands via Bluetooth and displays visual indications.

## Features

- **Bluetooth Connectivity**: Connects to HC-06/HC-05 Bluetooth modules
- **Gesture Detection**: Receives and displays three gesture types:
  - **L** → Left gesture (Blue background with ← icon)
  - **R** → Right gesture (Green background with → icon)
  - **S** → Static gesture (Orange background with || icon)
- **Visual Feedback**: Color-coded backgrounds and intuitive icons
- **Connection Management**: Easy connect/disconnect controls

## Requirements

- Android device with Bluetooth
- HC-06 or HC-05 Bluetooth module (paired with the device)
- Python 3 (for building)
- Buildozer (for building Android APK)

## Installation

### Building the APK

1. Install Buildozer:
   ```bash
   pip install buildozer
   ```

2. Build the Android APK:
   ```bash
   buildozer android debug
   ```

3. The APK will be created in `bin/` directory

### Installing on Android

1. Transfer the APK to your Android device
2. Enable "Install from Unknown Sources" in your device settings
3. Install the APK

## Usage

1. **Pair your Bluetooth module**: First, pair your HC-06/HC-05 module with your Android device through system Bluetooth settings
2. **Open the app**: Launch the Gesture Detector app
3. **Connect**: Tap the "Connect to HC-06" button
4. **Send commands**: From your Bluetooth module, send:
   - `L` for Left gesture
   - `R` for Right gesture
   - `S` for Static gesture
5. **Disconnect**: Tap "Disconnect" when done

## Technical Details

- **Framework**: Kivy 2.2.1
- **Language**: Python 3
- **Bluetooth**: Uses Android Bluetooth API via PyJNIus
- **Target Android API**: 33
- **Minimum Android API**: 21

## Permissions

The app requires the following Android permissions:
- BLUETOOTH
- BLUETOOTH_ADMIN
- BLUETOOTH_CONNECT
- BLUETOOTH_SCAN
- ACCESS_FINE_LOCATION

## Protocol

The app listens for single-character commands over Bluetooth SPP (Serial Port Profile):
- `L` or `l` → Switch to Left gesture
- `R` or `r` → Switch to Right gesture
- `S` or `s` → Switch to Static gesture

## License

Open source - feel free to modify and use as needed.
