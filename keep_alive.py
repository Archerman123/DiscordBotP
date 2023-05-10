from flask import Flask
from threading import Thread
from flask import Flask, render_template
app = Flask('')
running = False
status = "Starting"
reset = 0
attempts = 0
success = 0

@app.route('/')
def home():
    global status
    global success
    message = "null"
    message = "<div>Current Status: " + str(status) + "</div>"
    message += "<div> Relaunch attempts: " + str(attempts)+ "</div>"
    message += "<div> Sucessfully made online: " + str(success)+ "</div>"
    #return render_template('Website/html/autoclicker.html')
    return message

def run():
  global running
  if not running:
      running = True
      app.run(host='0.0.0.0', port=8080)

def keep_alive():
      t = Thread(target=run)
      t.start()

class website():
  def __init__(self):
    self.reset = 0
    self.attempts = 0
    self.success = 0

  def updateStat(self,s):
    global status
    status = s

  def addSuccess(self):
    global success
    success += 1

  def addAttempt(self):
      global attempts
      attempts += 1

  def getStatus(self):
    global status
    return status
    
  def getAttempt(self):
    global attempts
    return attempts