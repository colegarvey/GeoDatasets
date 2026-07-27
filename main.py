# from ssd1306 import SSD1306_I2C
# from pico_i2c_lcd import I2cLcd
# from time import sleep

# Pin.IN - read current state of pin
# Pin.OUT - set pin to high/low and control devices
# Pin.PULL_UP/DOWN - prevents floating states, only valid for Pin.OUT
# def Oled096():
#     WIDTH = 128
#     HEIGHT = 64

#     i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)

#     oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

#     oled.fill(0)
#     oled.text("hello world", 20, 20)
#     oled.show()
    
# def Led():
#     led = Pin(15, Pin.OUT)
#     while True:
#         led.toggle()
#         sleep(0.5)
        
# def Button():
#     button = Pin(14, Pin.IN, Pin.PULL_UP)
#     while True:
#         if button.value() == 0:
#             print("Button is Pressed")
#         else:
#             print("Button is not Pressed")
#         sleep(0.1)
        
# def Buzzer():
#         # Initialize the buzzer pin (GP15)
#     buzzer = Pin(15, Pin.OUT)

#     try:
#         while True:
#             buzzer.value(0)  # Turn the buzzer on
#             sleep(0.2)  # Wait for 0.5 seconds
#             buzzer.value(1)  # Turn the buzzer off
#             sleep(1)  # Wait for 0.5 seconds
#     except:
#         print("err")
#         pass

# def potentiometer(): 
#     pot = ADC(Pin(26))

#     while True:
#         value = pot.read_u16()
#         print(value)
#         sleep(0.1)



# create pot select [wildlife, police]
# open/write to files logic
# button press to write data to file
# add lcd


from machine import Pin, ADC, UART
from lib import gps_parser 
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1)) # GPS Module
button = Pin(14, Pin.IN, Pin.PULL_UP) # Log button
pot = ADC(Pin(26)) # Potentiometer

gps = gps_parser.GPSReader(uart)


while True:
    gps_data = gps.get_data()
    
    print(gps_data.has_fix, gps_data.latitude, gps_data.longitude)
    
    time.sleep(0.5)