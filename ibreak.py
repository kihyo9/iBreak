import time
import tkinter as tk
from app import app

# for contact sensor's digital input
import RPi.GPIO as GPIO

# Setup GPIO input reading
sensor_pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor_pin,GPIO.IN) # board pin 13

# window = tk.Tk()
# greeting = tk.Label(
#     text="Hello, Tkinter",
#     foreground="white",  # Set the text color to white
#     background="black",  # Set the background color to black
#     width=10,
#     height=10,
#     bg="blue",
#     fg="yellow"
# )
# greeting.pack()

# counter = 0
# while counter < 100:
# 	time.sleep(0.5)
# 	if GPIO.input(sensor_pin):
# 		print("Touched")
# 	else:
# 		print("Not touched")

a = app(GPIO, sensor_pin)
GPIO.cleanup()

# window.mainloop()