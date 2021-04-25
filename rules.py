import JsonReader


class rulesList():
  def __init__(self):
    
    self.servers = {}
    self.storage = JsonReader.reader("storageFile/rulesStorage.json")
    self.rules = self.storage.getData()

    for server in self.rules:
      self.servers[server] = self.rules[server]
  
  def getRule(self,number,server):
    server = str(server)
    if server in self.rules:
      try:
        return self.rules[server][number]
      except:
        return "Rule not found"
    else:
      self.addServer(server)
      return "No rules for the server yet"
    return "Rule not found"

  def loadData(self):
    self.rules = self.storage.getData()

  #def addRule(self,number,server):
    #server = str(server)
    #temp = {}
    #for aRule in self.rules:
      #temp[aRule.getNumber()] = aRule.getDesc()
    
    #print(temp)
    #self.servers[server] = temp
    #self.storage.writeData(self.servers)
    #self.loadData()

  def addServer(self,server):
    server = str(server)
    temp = {"1":"Undefined"}
    
    print(temp)
    self.servers[server] = temp
    self.storage.writeData(self.servers)
    self.loadData()

#class rule():
  #def __init__(self, number, description):
    #self.number = number
    #self.description = description 

  #def getDesc(self):
    #return self.description

  #def getNumber(self):
    #return self.number



    
