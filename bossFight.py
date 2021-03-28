import diceRolls as dice



class Boss():
  def __init__(self):
    self.maxHP = 10
    self.currentHP = self.maxHP
    self.AC = 10
    self.logs = []
    #make this a dictionary instead with players being assigned a status value: idle, attacking, downed, getting healed, healing
    self.players = []
    self.spentPlayers = []
    self.downedPlayers = []

  def join(self,player):
    self.players.append(player)

  def isCharLegit(self,char):
    return char in self.players

  def reset(self):
    self.currentHP = self.maxHP
    self.logs = []
    return "Bossfight has been reseted"

  def canAttack(self,char):
    if self.isCharLegit(char):
      if char not in self.spentPlayers:
        if char not in self.downedPlayers:
          return self.attack(char)
        else:
          return char + " is downed, someone need to save them!"
      else:
        return char + " already took an action, wait for the round to be over"
    else:
      return "Character not recognised, try !boss join [character name]" 

  def attack(self, user = 'User'):
    user = str(user)
    if self.currentHP < 1:
      self.logs.append("The boss is already down, no use to beat a dead h-...tree!")
      return "Action saved succesfully"
    result = dice.roll(20)
    wasHit = "dodged the attack."
    if result > self.AC:
      if result == 20:
        self.currentHP = self.currentHP -2
        wasHit = "was hit with a critical! The boss took 2 damage!"
      else:
        self.currentHP = self.currentHP -1
        wasHit = "was hit! The boss took 1 damage."
    if self.currentHP < 1:
      self.logs.append(user + " rolled a "+ str(result) + " and the boss " + wasHit + " The boss is now defeated!")
      return "Action saved succesfully"
    self.logs.append(user + " rolled a "+ str(result) + " and the boss " + wasHit)
    self.spentPlayers.append(user)
    return "Action saved succesfully"
  
  def status(self):
    print(str(self.currentHP) + '/' + str(self.maxHP))
    toSend = "The following players have taken action: " + str(self.spentPlayers)
    toSend += "\n The following players are downed, consider healing them: " + str(self.downedPlayers)
    if self.currentHP < self.maxHP/2:
      toSend += "\n The boss looks like they are getting tired"
    elif self.currentHP < 1:
      toSend += "\n The boss has fallen! congrats!"
    else:
      toSend += "\n The boss looks like they are still very healthy"
    return toSend

  def setHP(self,hp):
    self.maxHP = hp
    self.reset()
  
  def setAC(self,AC):
    self.AC = AC
    self.reset()

  def endRound(self):
    message = ''
    for log in self.logs:
      message += log + "\n"
    self.logs = []
    message += "\n"
    message += self.status()
    self.spentPlayers = []
    return message
  
  def bossAttack():
    pass
    #taunt variable
    #check if no one is attacking
    #down a player, two is no one is attacking. might miss based on roll
    