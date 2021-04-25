import wheel
import JsonReader

class wheelMaker():
  def __init__(self):
    self.servers = {}
    self.storage = JsonReader.reader("storageFile/wheelStorage.json")

    self.loadData()

    self.wheels = []
    for server in self.content:
      self.servers[server] = self.content[server]

  def loadData(self):
    self.content = self.storage.getData()

  def getWheels(self,server):
    server = str(server)
    if server not in self.servers:
      self.addServer(server)
      self.loadData()

    for w in self.servers[server]:
      toAdd = []
      for c in self.servers[server][w]:
        toAdd.append(c)
      self.wheels.append(wheel.wheel(w,toAdd))
    return self.wheels

  def updateWheel(self,wheel,server):
    server = str(server)
    self.servers[server][wheel.getName()] = wheel.getContent()
    self.storage.writeData(self.content)
    self.loadData()

  def addServer(self,server):
    server = str(server)
    temp = {"default":[]}
    
    print(temp)
    self.servers[server] = temp
    self.storage.writeData(self.servers)
    self.loadData()