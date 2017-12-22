from __future__ import unicode_literals
from chatterbot.input import InputAdapter
from chatterbot.conversation import Statement
from chatterbot.utils import input_function
from androidhelper import sl4a
droid = sl4a.Android()
import time
class AndroidSpeechAdapter(InputAdapter):
    """
    A simple adapter that allows ChatterBot to
    communicate through the Android recognizeSpeech.
    """

    def process_input(self, *args, **kwargs):
        """
        Read the user's input from the terminal.
        """
        time.sleep(5)
        new_message = False
        data = None
        while not new_message:
            
            if not droid.ttsIsSpeaking().result:
            	
                data = droid.recognizeSpeech()
                if data.result:
                    new_message = True
                else:
                    pass
                
        
        return Statement(data.result)
