import json

class reader():
  def __init__(self,file):
    self.file = file

  def writeData(self,data):
    with open(self.file,'w') as f:
      json.dump(data, f, indent=4)
      
  def getData(self):
    # read file
    with open(self.file, 'r') as myfile:
      self.data=myfile.read()

		# parse file
    with open(self.file) as json_file:
      self.data = json.load(json_file)
    self.dataList = self.data
    return self.dataList