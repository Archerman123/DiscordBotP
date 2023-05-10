import wheel
import JsonReader

class wheelMaker():
  def __init__(self):
    self.servers = {}
    self.storage = JsonReader.reader("storageFile/wheelStorage.json")
    self.loadData()

  def loadData(self):
    self.content = self.storage.getData()
    for server in self.content:
      self.servers[server] = self.content[server]
      

  def getWheels(self,server):
    server = str(server)
    toSend = []
    if server not in self.servers:
      self.addServer(server)
      self.loadData()
    for w in self.servers[server]:
      toSend.append(wheel.wheel(w,self.servers[server][w]))
    return toSend

  def updateWheel(self,wheel,server):
    server = str(server)
    self.servers[server][wheel.getName()] = wheel.getContent()
    self.storage.writeData(self.content)
    self.loadData()

  def addServer(self,server):
    server = str(server)
    temp = {"default":["default"]}
    
    print(temp)
    self.servers[server] = temp
    self.storage.writeData(self.servers)
    self.loadData()