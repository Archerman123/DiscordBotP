import random

class wheel():
  def __init__(self, name, content):
    self.name = name
    self.content = content
    
  def addContent(self,word):
    self.content.append(word)

  def removeContent(self,word):
    try:
      self.content.remove(word)
      return word + " was removed from the wheel successfully"
    except:
      return "Error: " + word + " is not in the list. (type !wheel list to see if you have made a spelling error)"

  def getContent(self):
    return self.content
  
  def spin(self):
    picked = random.randint(1,len(self.content) - 1)
    return "The wheel was spun, and the result is: " + self.content[picked] + '!'

  def getName(self):
    return self.name