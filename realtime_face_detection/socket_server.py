from flask import Flask, render_template,request
from flask_socketio import SocketIO
import time
import logging
from sl4a_to_tasker import taskerTask as ta
logging.getLogger('socketio').setLevel(logging.ERROR)
app = Flask(__name__)

socketio = SocketIO(app,logger= False,log_output=False)
@socketio.on('connect')
def connect():
    print 'Connected'+request.namespace  
@socketio.on('disconnect')
def disconnect():  
    print 'Disconnected'
@socketio.on('task',namespace="/qpy")
def handle_message(message):
	ta(message,"","")
	print "received "+message
	socketio.emit("my event"," task executed successfully")
@socketio.on('var',namespace="/qpy")
def handle_message(message):
	b=message.split("***")
	ta(False,b[0],b[1])
	print"received "+message
	socketio.emit("my event"," variable set successfully")
    
if __name__ == '__main__':
    socketio.run(app,host='localhost',port=8000,debug=False)