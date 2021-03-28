import wheel
import JsonReader

class wheelMaker():
  def __init__(self):
    self.storage = JsonReader.reader("storage.json")
    self.content = self.storage.getData()
    self.wheels = []
    for w in self.content:
      toAdd = []
      for c in self.content[w]:
        toAdd.append(c)
      self.wheels.append(wheel.wheel(w,toAdd))
    
  def getWheels(self):
    return self.wheels

  def updateWheel(self,wheel):
    self.content[wheel.getName()] = wheel.getContent()
    self.storage.writeData(self.content)