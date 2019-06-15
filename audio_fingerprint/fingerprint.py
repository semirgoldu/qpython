import warnings
import json
from time import sleep
warnings.filterwarnings("ignore")
import logging 
import androidhelper.sl4a as android
droid = android.Android()

import re 
logger = logging.getLogger("mne") 
logger.addFilter(lambda s: not re.match(".*convention.*", s.getMessage()))
from dejavu import *
from dejavu.recognize import FileRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("/sdcard/djv.cnf") as f:
    config = json.load(f)
print "starting ..."
#droid.recorderStartMicrophone("/sdcard/d.wav")
#sleep(10)
#droid.recorderStop()
#print "stopping ..."
if __name__ == '__main__':
 
	# create a Dejavu instance
	djv = Dejavu(config)

	# Fingerprint all the mp3's in the directory we give it
	#djv.fingerprint_file("/storage/emulated/0/mp3/Alexandra.mp3")

	# Recognize audio from a file
	song = djv.recognize(FileRecognizer, "/sdcard/d.mp3")
	print "From file we recognized: %s\n" % song

	