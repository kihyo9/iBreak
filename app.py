import tkinter as tk

class app():
	def __init__(self, GPIO, sensor_pin):
		self.root = tk.Tk()
		self.label = tk.Label(text="")
		self.label.pack()
		self.totalTime = 0
		self.sittingTime = 0
		self.GPIO = GPIO
		self.sensor_pin = sensor_pin
		self.sitting = False
		self.update_clock()
		self.root.mainloop()

	def update_clock(self):
		# now = time.strftime("%H:%M:%S")
		self.root.after(1000, self.update_clock)
		self.totalTime += 1
		self.sittingTime += 1     

		if self.totalTime % 5 == 0:
			self.eyeBreak()
		elif self.totalTime % 5 == 2:
			self.restBreak()

		self.sitting = self.checkChair() 
		if not self.sitting:
			sittingTime = 0

	def checkChair(self):
		return self.GPIO.input(self.sensor_pin)

	def eyeBreak(self):
		self.label.configure(
			text="EYE BREAK",
			foreground="white",  # Set the text color to white
			background="black",  # Set the background color to black
			width=10,
			height=10,
		)

	def restBreak(self):
		self.label.configure(
			text="REST BREAK",
			foreground="white",  # Set the text color to white
			background="green",  # Set the background color to black
			width=10,
			height=10,
		)