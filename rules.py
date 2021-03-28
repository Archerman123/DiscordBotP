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