from gpiozero import Robot
from flask import Flask
from flask_restful import Resource, Api

robot = Robot(left=(18, 24), right=(27, 22))
app = Flask(__name__)
api = Api(app)

class Forward(Resource):
	def get(self):
		robot.forward()
		return 
	    
class Backward(Resource):
	def get(self):
		robot.backward()
		return 
	    
class Left(Resource):
	def get(self):
		robot.left()
		return 
	    
class Right(Resource):
	def get(self):
		robot.right()
		return 

class PlayMode(Resource):
        def get(self):
            for i in range(4):
                robot.forward()
                sleep(10)
                robot.right()
                sleep(1)
                return 
      
class Stop(Resource):
	def get(self):
		robot.stop()
		return 
	    


api.add_resource(Forward, '/forward')
api.add_resource(Stop,'/stop')
api.add_resource(Right,'/right')
api.add_resource(Left,'/left')
api.add_resource(Backward,'/backward')
api.add_resource(PlayMode,'/play')

if __name__ == '__main__':
	app.run(debug=True)

