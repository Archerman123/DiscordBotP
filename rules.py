class rulesList():
  def __init__(self):
    self.rules = []
    self.rules.append(rule(1, "No users below 18, this is an adult server and no minors will be admited, if I come to knowledge of any member being a minor it will be grounds to kick them/ ban them inmediately. You'll be welcome to come back once you are of age."))

    self.rules.append(rule(2, " No political, or religious disccusion, because the best way to get people angry is to discuss either of those subjects."))

    self.rules.append(rule(3, "No harassing each other! Do not beg, or demand free art from any artist, this includes requests, as well as sexual harassment and demands for nudes or cybering. No means no."))

    self.rules.append(rule(4, "No posting of certain kinks/fetiches such as, but not limited to gore, vore, scat, diaper, or others of the sort, I'll edit this rule as I remember more of my personal no-nos."))

    self.rules.append(rule(5, "No loli or foalcon. We go by appearance for this rule and not canonical age. If it's a fictional character and can pass for 18, then it's allowed. The same goes in reverse though. If a character is older than 18, but looks like a loli, it's not kosher here."))

    self.rules.append(rule(6, "No uploading of patreon exclusive pics of any kind, unless the artist himself decides to upload them."))

    self.rules.append(rule(7, "No picture spam (Limited to 5 pictures every 10 mins)"))

    self.rules.append(rule(34, "There is porn of it, no exception. If not, you must make it."))
    self.rules.append(rule(63, "For every given male character, there is a female version of that character; conversely for every given female character, there is a male version of that character."))
    self.rules.append(rule(66, "Eliminate all jedis"))

    self.rules.append(rule("r1", "Respect your fellow players. If there's an active roleplay going on in the channel, don't just invite yourself! Ask out-of-character first if you can join in."))

    self.rules.append(rule("r2", "No gore play please. If that's your thing, we don't kink shame you here, but please keep it in DM's"))

    self.rules.append(rule("r3", "Don't ping someone unless you absolutely have to! Nobody likes getting pinged for no reason."))

    self.rules.append(rule("r4", "Keep out-of-character chatting outside the channel, please!"))

    self.rules.append(rule("r5", "Violating these rules is considered grounds for revocation of channel access. READ THE RULES, PLEASE! IGNORANCE IS NO EXCUSE!"))

    self.rules.append(rule("r6", "If you are rp-ing in a room and want to change to a different one, say it on the other channel so that other people can join you if they wish to!"))

    self.rules.append(rule("r7", "Remember this is ero-rp, anyone with the “under-18” role will not have acess to the roleplay area, if someone does, please report me and I’ll remove the role from the user, this is to not get our server closed, lol."))

    self.rules.append(rule("r8", "Use of magic and fantasy  technology is restricted to benign or sexual purposes. This is an ero-rp, not a test of power level."))

    self.rules.append(rule("r10", "If a player has not interacted in 24hrs it is assumed they left"))

    self.rules.append(rule("r11", "Do not disrespect your fellow players by abandoning the roleplay through unannounced AFK's.\n\n Doing so will result in moderator intervention to remove your character from the situation and an evaluation of the frequency in which you have engaged in this disrespectful behavior."))

    self.rules.append(rule("r12", "The Abandoned Factory is a rule free zone intended for doing things that would be outside the law, with three key exceptions. No death, no gore, and no forcing people to go there.\n\n If you voluntarily travel to this location, you accept that something bad might happen"))

    

    
  def getRule(self,number):
    for rule in self.rules:
      #print(str(rule.getNumber()) + ": " + rule.getDesc())
      if str(rule.getNumber()) == str(number):
        
        return rule.getDesc()

    return "Error: Rule not found"


class rule():
  def __init__(self, number, description):
    self.number = number
    self.description = description 

  def getDesc(self):
    return self.description

  def getNumber(self):
    return self.number