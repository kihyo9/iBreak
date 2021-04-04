import tkinter as tk
import time

class app():
	def __init__(self, GPIO, sensor_pin):
		self.root = tk.Tk()
		self.totalTime = 0
		self.sittingTime = 0
		self.notSittingTime = 0
		self.GPIO = GPIO
		self.width = 70
		self.height = 20
		self.sensor_pin = sensor_pin
		self.sitting = False

		self.label = tk.Label(text="")
		self.label.pack()
		self.default()
		self.update_clock()
		self.root.mainloop()

	def update_clock(self):
		# now = time.strftime("%H:%M:%S")
		self.root.after(1000, self.update_clock)
		self.totalTime += 1
		self.sittingTime += 1     
		self.sitting = self.checkChair()
		print(self.totalTime)
		print(self.sitting == 0)

		# if self.totalTime < 3:
		# 	self.running()
		# elif self.totalTime < 10:
		# 	self.default()
		# elif self.totalTime < 15:
		# 	self.eyeBreak()
		# elif self.totalTime < 25:
		# 	self.default()
		# elif self.totalTime < 35:
		# 	self.restBreak()
		# elif self.totalTime < 100:
		# 	self.default()

		if self.totalTime % 4 in [0,1]:
			self.default2()
		else:
			self.default()

		# if self.totalTime % 20 == 0:
		# 	self.restBreak()
		# elif self.totalTime % 5 == 0:
		# 	self.eyeBreak()
		# elif self.sitting:
		# 	self.sittingTime = 0
		# 	self.sittingAlert()

			

	def checkChair(self):
		return self.GPIO.input(self.sensor_pin)

	def eyeBreak(self):
		self.label.configure(
			text="Take an EYE break!\nLook at something 20 feet away for 20 seconds.",
			foreground="white",  # Set the text color to white
			background="black",  # Set the background color to black
			width=self.width,
			height=self.height,
			font=("Arial", 25)
		)

	def restBreak(self):
		self.label.configure(
			text="Take a REST break!\n Get up from your chair, stretch and walk around for a few minutes.",
			foreground="white",  # Set the text color to white
			background="grey",  # Set the background color to black
			width=self.width,
			height=self.height,
			font=("Arial", 25)
		)

	def sittingAlert(self):
		self.label.configure(
			text="YOU ARE SITTING",
			foreground="white",  # Set the text color to white
			background="red",  # Set the background color to black
			width=self.width,
			height=self.height,
			font=("Arial", 25)
		)

	def now(self):
		return time.strftime("%H:%M:%S")

	def default(self):
		self.label.configure(
			text="You are currently sitting!",
			foreground="black",  # Set the text color to white
			background="white",  # Set the background color to black
			width=self.width,
			height=self.height,
			font=("Arial", 25)
		)

	def running(self):
		self.label.configure(
			text="Running...",
			foreground="black",  # Set the text color to white
			background="white",  # Set the background color to black
			width=self.width,
			height=self.height,
			font=("Arial", 25)
		)

	def default2(self):
		self.label.configure(
			text="You are currently not sitting!",
			foreground="black",  # Set the text color to white
			background="white",  # Set the background color to black
			width=self.width,
			height=self.height,
			font=("Arial", 25)
		)

