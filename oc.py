import JsonReader

class ocStorage():
  def __init__(self):
    self.loadData()

  def loadData(self):
    self.storage = JsonReader.reader("ocStorage.json")
    self.links = self.storage.getData()
    self.names = [*self.links]

  def getOC(self, name):
    return self.links[name]

  def getList(self):
    return self.names

  def addOC(self,name,link):
    self.links[name] = link
    self.storage.writeData(self.links)
    self.loadData()

