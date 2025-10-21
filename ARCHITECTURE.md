# Architecture Overview

## App Structure

```
GestureDetectorApp (Kivy App)
├── UI Components
│   ├── Gesture Display Box (60% height)
│   │   ├── Gesture Icon (?, <--, -->, ||)
│   │   └── Gesture Text (WAITING, LEFT, RIGHT, STATIC)
│   └── Control Box (40% height)
│       ├── Status Label
│       ├── Connect Button
│       ├── Disconnect Button
│       └── Command Legend
└── Bluetooth Management
    ├── Connection Thread
    ├── Data Reader Thread
    └── Gesture Processor
```

## Data Flow

```
Bluetooth Module (HC-06/HC-05)
    ↓
[Send: L, R, or S]
    ↓
Bluetooth Socket (SPP)
    ↓
Input Stream Reader
    ↓
Character Parser (uppercase)
    ↓
Gesture Processor
    ↓
UI Update (Main Thread)
    ├── Update Background Color
    ├── Update Icon
    └── Update Text Label
```

## Thread Architecture

### Main Thread (UI Thread)
- Handles all UI updates
- Manages button interactions
- Updates gesture display

### Connection Thread
- Establishes Bluetooth connection
- Creates socket with HC-06/HC-05
- Initializes input stream

### Reader Thread
- Continuously reads from Bluetooth input stream
- Parses incoming characters
- Schedules UI updates on main thread

## State Machine

```
[DISCONNECTED]
    ↓ (Connect Button)
[CONNECTING]
    ↓ (Success)
[CONNECTED]
    ├── Receive 'L' → [LEFT GESTURE]
    ├── Receive 'R' → [RIGHT GESTURE]
    └── Receive 'S' → [STATIC GESTURE]
    ↓ (Disconnect Button or Error)
[DISCONNECTED]
```

## Color Scheme

| Gesture | Background Color | RGB Values | Icon |
|---------|-----------------|------------|------|
| Waiting | Gray | (0.4, 0.4, 0.4) | ? |
| Left | Blue | (0.05, 0.43, 0.99) | <-- |
| Right | Green | (0.10, 0.59, 0.33) | --> |
| Static | Orange | (0.99, 0.49, 0.08) | \|\| |

## Bluetooth Protocol

### SPP UUID
`00001101-0000-1000-8000-00805F9B34FB` (Standard Serial Port Profile)

### Commands
- Single-character commands (case-insensitive)
- No delimiter required
- Commands: L, R, S

### Connection Process
1. Get default Bluetooth adapter
2. Check if Bluetooth is enabled
3. Scan bonded (paired) devices
4. Find HC-06/HC-05 device by name
5. Create RFCOMM socket
6. Connect to device
7. Get input stream
8. Start reading loop

## Error Handling

- **No Bluetooth Adapter**: Display error message
- **Bluetooth Disabled**: Prompt user to enable Bluetooth
- **Device Not Paired**: Inform user to pair HC-06 first
- **Connection Failed**: Show error details
- **Connection Lost**: Auto-disconnect and reset UI
- **Invalid Commands**: Silently ignore non-L/R/S characters

## Android Permissions

Required for Bluetooth functionality:
- `BLUETOOTH`: Basic Bluetooth operations
- `BLUETOOTH_ADMIN`: Device discovery and management
- `BLUETOOTH_CONNECT`: Connect to paired devices (Android 12+)
- `BLUETOOTH_SCAN`: Scan for devices (Android 12+)
- `ACCESS_FINE_LOCATION`: Required for Bluetooth discovery on Android 10+
