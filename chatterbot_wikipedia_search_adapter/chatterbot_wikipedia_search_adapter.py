from __future__ import unicode_literals
from datetime import datetime
from chatterbot.logic import LogicAdapter
from query_parser import parser
import wikipedia

class WikipediaAdapter(LogicAdapter):
    """
    The TimeLogicAdapter returns the current time.
    """

    def __init__(self, **kwargs):
        super(WikipediaAdapter, self).__init__(**kwargs)
        from nltk import NaiveBayesClassifier

        self.positive = [
            'wikipedia search for',
            'tell me about ',
            'what do you know about',
        ]

        self.negative = [
            'How are you',
            'What time is it',
            'When will you walk'

        ]

            

        labeled_data = (
            [(name, 0) for name in self.negative] +
            [(name, 1) for name in self.positive]
        )

        # train_set = apply_features(self.time_question_features, training_data)
        train_set = [(self.web_question_features(n), text) for (n, text) in labeled_data]

        self.classifier = NaiveBayesClassifier.train(train_set)

    def web_question_features(self, text):
        """
        Provide an analysis of significan features in the string.
        """
        features = {}

        all_words = " ".join(self.positive + self.negative).split()

        for word in text.split():
            features['contains({})'.format(word)] = (word in all_words)

        for letter in 'abcdefghijklmnopqrstuvwxyz':
            features['count({})'.format(letter)] = text.lower().count(letter)
            features['has({})'.format(letter)] = (letter in text.lower())

        return features

    def process(self, statement):
        from chatterbot.conversation import Statement

        now = datetime.now()

        web_features = self.web_question_features(statement.text.lower())
        confidence = self.classifier.classify(web_features)
        response = Statement('classified as web ' )
  
        response.confidence = confidence
        
        #print statement.text
        #parser gets the last word or phrase from the query
        p = parser()
        wiki_query = p.parse(statement.text)
        try:
            result = wikipedia.summary(wiki_query,sentences=2)
        except:
            result = " I did not find any result"
        
        res =Statement(result)
        res.confidence=confidence
        return res
