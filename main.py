from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from jnius import autoclass, cast
import threading

BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
UUID = autoclass('java.util.UUID')

class GestureDetectorApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bt_adapter = None
        self.bt_socket = None
        self.input_stream = None
        self.connected = False
        self.current_gesture = "WAITING"
        
    def build(self):
        Window.clearcolor = (0.4, 0.4, 0.4, 1)
        self.root_layout = BoxLayout(orientation='vertical')
        self.gesture_box = BoxLayout(orientation='vertical', size_hint=(1, 0.6))
        
        with self.gesture_box.canvas.before:
            self.bg_color = Color(0.4, 0.4, 0.4, 1)
            self.bg_rect = Rectangle(size=self.gesture_box.size, pos=self.gesture_box.pos)
        
        self.gesture_box.bind(size=self._update_rect, pos=self._update_rect)
        
        self.gesture_icon = Label(text='?', font_size='80sp', size_hint=(1, 0.5))
        self.gesture_text = Label(text='WAITING', font_size='40sp', bold=True, size_hint=(1, 0.5))
        
        self.gesture_box.add_widget(self.gesture_icon)
        self.gesture_box.add_widget(self.gesture_text)
        
        control_box = BoxLayout(orientation='vertical', size_hint=(1, 0.4), padding=20, spacing=10)
        
        self.status_label = Label(text='Not Connected', size_hint=(1, 0.2), font_size='16sp', color=(0, 0, 0, 1))
        
        self.connect_btn = Button(text='Connect to HC-06', size_hint=(1, 0.2), background_color=(0.05, 0.43, 0.99, 1), font_size='18sp', bold=True)
        self.connect_btn.bind(on_press=self.connect_bluetooth)
        
        self.disconnect_btn = Button(text='Disconnect', size_hint=(1, 0.2), background_color=(0.86, 0.21, 0.27, 1), font_size='18sp', bold=True, disabled=True)
        self.disconnect_btn.bind(on_press=self.disconnect_bluetooth)
        
        legend_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.4), padding=10, spacing=5)
        legend_layout.add_widget(Label(text='Commands:', font_size='14sp', bold=True, color=(0, 0, 0, 1), size_hint=(1, 0.25)))
        legend_layout.add_widget(Label(text='L = Left (Blue)', font_size='12sp', color=(0, 0, 0, 1), size_hint=(1, 0.25)))
        legend_layout.add_widget(Label(text='R = Right (Green)', font_size='12sp', color=(0, 0, 0, 1), size_hint=(1, 0.25)))
        legend_layout.add_widget(Label(text='S = Static (Orange)', font_size='12sp', color=(0, 0, 0, 1), size_hint=(1, 0.25)))
        
        control_box.add_widget(self.status_label)
        control_box.add_widget(self.connect_btn)
        control_box.add_widget(self.disconnect_btn)
        control_box.add_widget(legend_layout)
        
        self.root_layout.add_widget(self.gesture_box)
        self.root_layout.add_widget(control_box)
        
        return self.root_layout
    
    def _update_rect(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size
    
    def connect_bluetooth(self, instance):
        try:
            self.status_label.text = "Connecting..."
            self.bt_adapter = BluetoothAdapter.getDefaultAdapter()
            
            if not self.bt_adapter:
                self.status_label.text = "No Bluetooth adapter"
                return
            
            if not self.bt_adapter.isEnabled():
                self.status_label.text = "Enable Bluetooth first"
                return
            
            paired_devices = self.bt_adapter.getBondedDevices().toArray()
            
            hc06_device = None
            for device in paired_devices:
                device = cast(BluetoothDevice, device)
                name = device.getName()
                if name and ("HC-06" in name or "HC-05" in name or "HC" in name):
                    hc06_device = device
                    break
            
            if not hc06_device:
                self.status_label.text = "HC-06 not paired"
                return
            
            threading.Thread(target=self._connect_thread, args=(hc06_device,), daemon=True).start()
            
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"
    
    def _connect_thread(self, device):
        try:
            spp_uuid = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB")
            self.bt_socket = device.createRfcommSocketToServiceRecord(spp_uuid)
            self.bt_socket.connect()
            
            self.input_stream = self.bt_socket.getInputStream()
            self.connected = True
            
            Clock.schedule_once(lambda dt: self._update_connection_status(True))
            self.read_bluetooth_data()
            
        except Exception as e:
            Clock.schedule_once(lambda dt: self._update_connection_status(False, str(e)))
    
    def _update_connection_status(self, success, error_msg=""):
        if success:
            self.status_label.text = "Connected!"
            self.connect_btn.disabled = True
            self.disconnect_btn.disabled = False
            self.update_gesture('STATIC')
        else:
            self.status_label.text = f"Failed: {error_msg}"
    
    def read_bluetooth_data(self):
        try:
            while self.connected and self.input_stream:
                if self.input_stream.available() > 0:
                    byte_data = self.input_stream.read()
                    if byte_data != -1:
                        char = chr(byte_data).upper()
                        if char in ['L', 'R', 'S']:
                            Clock.schedule_once(lambda dt, c=char: self.process_gesture(c))
        except Exception as e:
            Clock.schedule_once(lambda dt: self._handle_disconnect(str(e)))
    
    def process_gesture(self, data):
        if data == 'L':
            self.update_gesture('LEFT')
        elif data == 'R':
            self.update_gesture('RIGHT')
        elif data == 'S':
            self.update_gesture('STATIC')
    
    def update_gesture(self, gesture):
        self.current_gesture = gesture
        self.gesture_text.text = gesture
        
        if gesture == 'LEFT':
            self.bg_color.rgba = (0.05, 0.43, 0.99, 1)
            self.gesture_icon.text = '<--'
        elif gesture == 'RIGHT':
            self.bg_color.rgba = (0.10, 0.59, 0.33, 1)
            self.gesture_icon.text = '-->'
        elif gesture == 'STATIC':
            self.bg_color.rgba = (0.99, 0.49, 0.08, 1)
            self.gesture_icon.text = '||'
        else:
            self.bg_color.rgba = (0.4, 0.4, 0.4, 1)
            self.gesture_icon.text = '?'
    
    def disconnect_bluetooth(self, instance):
        try:
            self.connected = False
            if self.bt_socket:
                self.bt_socket.close()
            self.status_label.text = "Disconnected"
            self.connect_btn.disabled = False
            self.disconnect_btn.disabled = True
            self.update_gesture('WAITING')
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"
    
    def _handle_disconnect(self, error_msg):
        self.connected = False
        self.status_label.text = f"Lost connection"
        self.connect_btn.disabled = False
        self.disconnect_btn.disabled = True
        self.update_gesture('WAITING')
    
    def on_stop(self):
        self.disconnect_bluetooth(None)

if __name__ == '__main__':
    GestureDetectorApp().run()
