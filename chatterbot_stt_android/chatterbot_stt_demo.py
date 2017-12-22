from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer 
from chatterbot.trainers import ListTrainer


# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[ { 'import_path': 'chatterbot.logic.BestMatch' },
                     
                     ],
    
    input_adapter='chatterbot_stt.AndroidSpeechAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    #database='my',
    database_uri='sqlite:////storage/emulated/0/example.sqlite'
    
)
bot.set_trainer(ListTrainer) 

bot.train([
    "What is your name",
    "My name is sansa",
    " what is this demo about",
    "this demo is about Android recognize speech adapter",
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
])
#bot.set_trainer(ChatterBotCorpusTrainer) 
#bot.train("chatterbot.corpus.english")

print('Say something to begin...')

while True:
    try:
        bot_input = bot.get_response(None)
        
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break