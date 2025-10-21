# gesture-detector-app
Bluetooth gesture detector for HC-06

## Description
A Kivy-based Android application that connects to HC-06 Bluetooth modules and displays gesture commands (Left, Right, Static) received from the device.

## Prerequisites
Before building the app, ensure you have the following installed:

- **Python 3.8+** (Python 3.10 recommended)
- **pip** (Python package installer)
- **Git**
- **Java Development Kit (JDK)** - OpenJDK 17 or higher
- **Build tools** (Linux/WSL):
  ```bash
  sudo apt-get update
  sudo apt-get install -y git zip unzip openjdk-17-jdk wget autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
  ```

## Installation

### 1. Install Buildozer
Buildozer is the tool used to package Python applications for Android:

```bash
pip install --upgrade pip
pip install buildozer==1.5.0 cython==0.29.33
```

### 2. Clone the Repository
```bash
git clone https://github.com/mazenElzeiny/gesture-detector-app.git
cd gesture-detector-app
```

## Building the APK

### Build for Android Debug

To build the Android debug APK, run the following command **in the project root directory** (where `buildozer.spec` is located):

```bash
buildozer android debug
```

This command will:
1. Download and set up the Android SDK and NDK (first time only)
2. Install required Python dependencies
3. Compile the app
4. Generate a debug APK

**Note:** The first build can take 20-30 minutes as it downloads and sets up the Android build environment.

### Output Location

After a successful build, the APK file will be located in:
```
bin/gesturedetector-1.0-debug.apk
```

You can install this APK on your Android device by:
- Transferring it via USB and installing manually
- Using `adb install bin/gesturedetector-1.0-debug.apk`

## Troubleshooting

### Common Issues

1. **"Command not found: buildozer"**
   - Make sure buildozer is installed: `pip install buildozer`
   - Ensure your Python scripts directory is in PATH

2. **"SDK download failed"**
   - Check your internet connection
   - Try running `buildozer android clean` and rebuild

3. **"Java not found"**
   - Install OpenJDK: `sudo apt-get install openjdk-17-jdk`
   - Set JAVA_HOME environment variable

4. **Build fails on first attempt**
   - Run `buildozer android clean`
   - Delete `.buildozer` directory
   - Try building again

5. **Permission denied errors**
   - Buildozer may need write permissions in the project directory
   - Avoid running buildozer as root

## App Features

- Connect to HC-06 Bluetooth modules
- Display real-time gesture commands:
  - **L** = Left (Blue background)
  - **R** = Right (Green background)  
  - **S** = Static (Orange background)
- Visual feedback with icons and color changes

## Permissions

The app requires the following Android permissions:
- BLUETOOTH
- BLUETOOTH_ADMIN
- BLUETOOTH_CONNECT
- BLUETOOTH_SCAN
- ACCESS_FINE_LOCATION

These are configured in `buildozer.spec` and will be requested when the app runs.
