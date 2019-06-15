import os
import logging
import android

"""
Misc / Allow External Access must be set in Tasker's prefs.

Tasker action code reference:
  http://tasker.dinglisch.net/ActionCodes.java
"""
SET_VARIABLE = 547
CLEAR_VARIABLE = 549
POPUP = 550
RUN_TASK = 130

logging.basicConfig(level=logging.INFO)

class Tasker(object):
  def __init__(self,task_name):
    self.droid = android.Android()
    tasker_task_name = ""
    if task_name:
    	tasker_task_name = task_name
    self.extras = dict(
      version_number = '1.0',
      task_name = tasker_task_name,
      task_priority = 9)
    self.actions = 0

  def bundle(self, action, *args):
    # Unused parameters are padded with False
    args = list(args)
    args.extend([False]*(6-len(args)))

    self.actions += 1
    self.extras.update(
      {'action{}'.format(self.actions) : dict(
        {'action' : action,
         'arg:1' : args[0],
       
         'arg:2' : args[1],
         'arg:3' : args[2],
         'arg:4' : args[3],
         'arg:5' : args[4],
         'arg:6' : args[5]})
         })

  def broadcast_intent(self):
    intent = self.droid.makeIntent(
      'net.dinglisch.android.tasker.ACTION_TASK', None, None, self.extras).result
    logging.debug("-- {}".format(intent))
    self.droid.sendBroadcastIntent(intent) 

#helper function to initialize the class
#bundle actions and arguments and
#broadcast the intent
#to set a variable you must make the task_name 
#argument False
#it won't execute a task and set variables
#at the same time
def taskerTask(task_name,var,value):

    tasker = Tasker(task_name)
    if var:
        tasker.bundle(SET_VARIABLE, var,value)
    tasker.broadcast_intent()
#run a task
#taskerTask("Show Popup",False,False)

#set a variable and run a task to show variable
#value
#taskerTask(False,'%Var1', 'Hello World!')
#taskerTask("Shell",False,False)
