from __future__ import unicode_literals
from chatterbot.output import OutputAdapter
from androidhelper import sl4a
droid = sl4a.Android()

class AndroidSpeechAdapter(OutputAdapter):
    """
    A simple adapter that allows ChatterBot to
    communicate through the Android TTS.
    """

    def process_response(self, statement, session_id=None):
        """
        Print the response to the user's input.
        """
        droid.ttsSpeak(statement.text)
        print statement.text.encode("utf-8"). strip()
        return statement.text
