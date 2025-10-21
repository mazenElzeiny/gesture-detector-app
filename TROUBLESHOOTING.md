# Troubleshooting Guide

## Common Issues and Solutions

### 1. "No Bluetooth adapter" Error

**Problem**: The app can't find a Bluetooth adapter on your device.

**Solutions**:
- Verify your device has Bluetooth hardware
- Try restarting the app
- Check if Bluetooth works in other apps

### 2. "Enable Bluetooth first" Message

**Problem**: Bluetooth is disabled on the device.

**Solutions**:
- Enable Bluetooth in Android settings
- Swipe down and tap the Bluetooth quick toggle
- Restart the app after enabling Bluetooth

### 3. "HC-06 not paired" Error

**Problem**: The Bluetooth module is not paired with your device.

**Solutions**:
1. Go to Android Settings → Bluetooth
2. Make sure your HC-06/HC-05 is powered on
3. Scan for new devices
4. Pair with the device (default PIN is usually `1234` or `0000`)
5. Return to the app and try connecting again

### 4. Connection Fails

**Problem**: The app can't connect to the paired device.

**Solutions**:
- Make sure the HC-06/HC-05 is powered on
- Check if the module is already connected to another device
- Try unpairing and re-pairing the device
- Restart both your phone and the Bluetooth module
- Check the distance (keep within 10 meters)

### 5. No Gesture Response

**Problem**: Connected but gestures don't show up.

**Solutions**:
- Verify your device is sending `L`, `R`, or `S` characters
- Check the baud rate (default HC-06 is usually 9600)
- Make sure commands are uppercase (or lowercase - app handles both)
- Test with a serial terminal app to verify the HC-06 is working

### 6. App Crashes on Connect

**Problem**: App crashes when tapping Connect button.

**Solutions**:
- Grant all required permissions in Android settings
- Update to latest Android System WebView
- Try clearing app data and cache
- Reinstall the app

### 7. "Lost connection" Message

**Problem**: Connection drops unexpectedly.

**Solutions**:
- Check power supply to HC-06 module
- Reduce distance between devices
- Check for interference from other Bluetooth devices
- Verify the HC-06 module is functioning properly

### 8. Build Errors

**Problem**: Can't build the APK with Buildozer.

**Solutions**:
- Make sure you have all dependencies: `pip install buildozer`
- On Linux, install: `sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev`
- Clean buildozer cache: `buildozer android clean`
- Try building again: `buildozer android debug`

### 9. Permissions Not Granted

**Problem**: App doesn't request Bluetooth permissions.

**Solutions**:
1. Go to Android Settings → Apps → Gesture Detector
2. Tap "Permissions"
3. Manually grant Bluetooth and Location permissions
4. Restart the app

### 10. Can't Install APK

**Problem**: APK installation fails.

**Solutions**:
- Enable "Install from Unknown Sources" for your file manager
- On Android 8+: Enable "Install Unknown Apps" for specific apps
- Try transferring the APK differently (USB, cloud, etc.)
- Make sure you have enough storage space

## Testing Your Setup

### Test HC-06 Module
1. Use a USB-to-Serial adapter or Arduino
2. Connect to HC-06 at 9600 baud
3. Send `L`, `R`, `S` commands
4. Verify the module responds

### Test Android Bluetooth
1. Install a Bluetooth terminal app
2. Connect to HC-06
3. Verify you can send/receive data
4. If this works, the issue is with the app

### Debug Mode
To get more information:
1. Connect your phone via USB
2. Enable USB debugging
3. Use `adb logcat` to view logs
4. Look for Bluetooth or app-related errors

## Getting Help

If none of these solutions work:
1. Check the GitHub repository for similar issues
2. Open a new issue with:
   - Your device model and Android version
   - HC-06/HC-05 module details
   - Steps to reproduce the problem
   - Any error messages
   - Logcat output if available

## Hardware Specifications

### Recommended HC-06 Settings
- **Baud Rate**: 9600 (default)
- **Data Bits**: 8
- **Stop Bits**: 1
- **Parity**: None
- **Flow Control**: None

### Wiring (if using Arduino)
```
HC-06 Module:
- VCC → 5V
- GND → GND
- TX → Arduino RX (or via voltage divider)
- RX → Arduino TX
```

### Testing Commands (via Serial)
```python
# Send these through serial terminal:
L  # Should trigger Left gesture
R  # Should trigger Right gesture
S  # Should trigger Static gesture
```
