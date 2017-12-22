#----------------------------------------------------------------------
#  eliza.py
#
#  a cheezy little Eliza knock-off by Joe Strout <joe@strout.net>
#  with some updates by Jeff Epler <jepler@inetnebr.com>
#  hacked into a module and updated by Jez Higgins <jez@jezuk.co.uk>
#  revived on Github by irgbit <birgit@moddr.net>
#  last revised: 27 August 2015
#----------------------------------------------------------------------

import string
import re
import random
class parser:
  def __init__(self):
    self.keys = map(lambda x:re.compile(x[0], re.IGNORECASE),gPats)
    self.values = map(lambda x:x[1],gPats)

  #----------------------------------------------------------------------
  # translate: take a string, replace any words found in dict.keys()
  #  with the corresponding dict.values()
  #----------------------------------------------------------------------
  def translate(self,str,dict):
    words = string.split(string.lower(str))
    keys = dict.keys();
    for i in range(0,len(words)):
      if words[i] in keys:
        words[i] = dict[words[i]]
    return string.join(words)

  #----------------------------------------------------------------------
  #  respond: take a string, a set of regexps, and a corresponding
  #    set of response lists; find a match, and return a randomly
  #    chosen response from the corresponding list.
  #----------------------------------------------------------------------
  def parse(self,str):
    # find a match among keys
    for i in range(0,len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        # found a match ... stuff with corresponding value
        # chosen randomly from among the available options
        resp = random.choice(self.values[i])
        # we've got a response... stuff in reflected text where indicated
        pos = string.find(resp,'%')
        #print resp
        while pos > -1:
          num = string.atoi(resp[pos+1:pos+2])
          resp = resp[:pos] + \
            self.translate(match.group(num),gReflections) + \
            resp[pos+2:]
          pos = string.find(resp,'%')
        # fix munged punctuation at the end
        if resp[-2:] == '?.': resp = resp[:-2] + '.'
        if resp[-2:] == '??': resp = resp[:-2] + '?'
        return resp
        
#----------------------------------------------------------------------
# gReflections, a translation table used to convert things you say
#    into things the computer says back, e.g. "I am" --> "you are"
#----------------------------------------------------------------------
gReflections = {
  "am"   : "are",
  "was"  : "were",
  "i"    : "you",
  "i'd"  : "you would",
  "i've"  : "you have",
  "i'll"  : "you will",
  "my"  : "your",
  "are"  : "am",
  "you've": "I have",
  "you'll": "I will",
  "your"  : "my",
  "yours"  : "mine",
  "you"  : "me",
  "me"  : "you"
}

#----------------------------------------------------------------------
# gPats, the main response table.  Each element of the list is a
#  two-element list; the first is a regexp, and the second is a
#  list of possible responses, with group-macros labelled as
#  %1, %2, etc.  
#----------------------------------------------------------------------
gPats = [

  
   [r'tell me about (.*)',
  [  "%1",
   ]],
  [r'what do you know about (.*)',
  [  "%1",
   ]],
   [r'wikipedia search for (.*)',
  [  "%1",
   ]],
    
  ]

#----------------------------------------------------------------------
#  command_interface
#----------------------------------------------------------------------
