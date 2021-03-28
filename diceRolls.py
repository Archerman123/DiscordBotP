#!/usr/bin/env python
# Python dice rolling and parsing
# Embed into a bot, service, whatever...
# made by ryands on github, updated by me

import random
import re
#import sys
#from exceptions import ValueError

def roll(sides):
    """ Roll a (sides) sided die and return the value. 1 <= N <= sides """
    return random.randint(1,sides)

def parse_dice(cmd):
  """ Parse strings like "2d6" or "1d20" or "5d103+5" and roll accordingly """
  pattern2 = re.compile(r'(?P<count>\d+)?d(?P<sides>\d+)(?P<mod>[\+\-]\d+)?')
  match2 = re.match(pattern2, cmd)
  
  if not match2:
      return "Error: Input invalid. The correct way to use this command is: \n !roll [how many dices][the letter d][what kind of dice] + or - [modifier] \n Exemples: !roll d20, !roll 2d6, !roll 5d7+5"
    
  sides = int(match2.group('sides'))
  try:
    count = int(match2.group('count'))
  except:
    count = 1

  try:
    mod = int(match2.group('mod'))
  except:
    mod = 0

  if count > 1:
    return [ roll(sides)+ mod for i in range(count) ]
  else:
    return roll(sides)