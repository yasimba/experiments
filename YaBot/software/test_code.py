from gpiozero import Robot
from time import sleep
robot = Robot(left = (18, 24), right = (27, 22))
while True:
	print("Forward")
	robot.forward()
	sleep(3)
	robot.stop()
	print("right")
	robot.right()
	sleep(3)
	robot.stop()
	print("Backward")
	robot.backward()
	sleep(3)

