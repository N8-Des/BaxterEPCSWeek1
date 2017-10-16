import random
def main():
  students = [
    Champion()
  ]

  printHeader()
  selection = getUserSelection()
  if selection == 0:
    RandomizedChampions()
  else:
    print ("SELECTION NOT RECOGNIZED")


class Champion:
  lanes = ['mid','adc','support','top','jungle']
  mainChamps = ['Aatrox','Ahri','Akali','Alistar','Amumu','Anivia','Annie','Ashe','Aurelion Sol','Azir','Bard','Blitzcrank','Brand','Braum','Caitlyn','Camille','Cassiopeia','ChoGath','Corki','Darius','Diana','Dr Mundo','Draven','Ekko','Elise','Evelynn','Ezreal','Fiddlesticks','Fiora','Fizz','Galio','Gangplank','Garen','Gnar','Gragas','Graves','Hecarim','Heimerdinger','Illoai','Irelia','Ivern','Janna','Jarvan IV','Jax','Jayce','Jhin','Jinx','Kalista','Karma','Karthus','Kassadin','Katarina','Kayle','Kennen','KhaZix','Kindred','Kled','KogMaw','LeBlanc','Lee Sin','Leona','Lissandra','Lucian','Lulu','Lux','Malphite','Malzahar','Maokai','Master Yi','Miss Fortune','Mordekaiser','Morgana','Nami','Nasus','Nautilus','Nidalee','Nocturne','Nunu','Olaf','Orianna','Pantheon','Poppy','Quinn','Rammus','RekSai','Renekton','Rengar','Riven','Rumble','Ryze','Sejuani','Shaco','Shen','Shyvana','Singed','Sion','Sivir','Skarner','Sona','Soraka','Swain','Syndra','Tahm Kench','Taliyah','Talon','Taric','Teemo','Thresh','Thresh','Tristana','Trundle','Tryndamere','Twisted Fate','Twitch','Udyr','Urgot','Varus','Vayne','Veigar','VelKoz','Vi','Viktor','Vladimir','Volibear','Warwick','Wukong','Xerath','Xin Zhao','Yasuo','Yorick','Zac','Zed','Ziggs','Zilean','Zyra']
  fullItems = ['Abyssal Mask','Adaptive Helm','Archangels Staff','Ardent Censer','Unholy Grail','Banner of Command','Banshees Veil','Blade of the Ruined King','Dead Mans Plate','Deaths Dance','Duskblade of Drakathaar','Edge of Night','Essence Reaver','Eye of Equinox','Eye of the Oasis','Eye of the Watcher','Face of the Mountain','Frost Queens Claim','Frozen Heart','Frozen Mallet','Gargoyle Stoneplate','Guardian Angel','Guinsoos Rageblade','Hextech GLP-800','Hextech Gunblade','Hextech Protobelt-01','Iceborn Gauntlet','Infinity Edge','Knights Vow','Liandrys Torment','Lich Bane','Locket of the Iron Solari','Lord Dominiks Regards','Ludens Echo','Manamune','Maw of Malmortius','Mejais Soulstealer','Mercurial Scimitar','Mikaels Crucible','Morellonomicon','Mortal Reminder','Nashors Tooth','Ohmwrecker','Phantom Dancer','Rabadons Deathcap','Randuins Omen','Rapid Firecannon','Ravenous Hydra','Redemption','Righteous Glory','Rod Of Ages','Ruby Sightstone','Runaans Hurricane','Rylais Crystal Scepter','Spirit Visage','Statikk Shiv','Steraks Gage','Sunfire Cape','Talisman of Ascension','The Black Cleaver','The Bloodthirstier','Thornmail','Titanic Hydra','Trinity Force','Void Staff','Warmogs Armor','Wits End','Yomuus Ghostblade','Zekes Convergence','Zhonyas Hourglass','ZZ-Rot Portal','','','','','','','','']
  def __init__(self):
    self.assignRandomK()
    self.assignRandomD()
    self.assignRandomA()
    self.randomChampion()
    self.randomLane()
    self.randomItem1()
    self.randomItem2()
    self.randomItem3()
    self.randomItem4()
    self.randomItem5()
    self.randomItem6()

  def randomLane(self):
     self.lane = random.choice(self.lanes)

  def randomChampion(self):
     self.mainChamp = random.choice(self.mainChamps)
  
  def assignRandomK(self):
     self.K = random.randint(0,30)
  def assignRandomD(self):
     self.D = random.randint(0,30)
  def assignRandomA(self):
     self.A = random.randint(0,30)  
  def randomItem1(self):
    self.item1 = random.choice(self.fullItems)
  def randomItem2(self):
    self.item2 = random.choice(self.fullItems)  
  def randomItem3(self):
    self.item3 = random.choice(self.fullItems)
  def randomItem4(self):
    self.item4 = random.choice(self.fullItems)
  def randomItem5(self):
    self.item5 = random.choice(self.fullItems)
  def randomItem6(self):
    self.item6 = random.choice(self.fullItems)

inputQuestions = [ 
  "For CHAMPIONS, type 0",
]

def getUserSelection():
  print (inputQuestions[0])
  return int(input("Type selection and press enter: "))

def RandomizedChampions():
  count = int( input("How Many Randomized Champions? "))
  for i in range(0, count):
    champ = Champion()
    print (str(champ.mainChamp) + " " + str(champ.lane) + ", " + str(champ.item1) + ", " + str(champ.item2) + ", " + str(champ.item3) + ", " + str(champ.item4) +", " + str(champ.item5) + ", " + str(champ.item6))
def printHeader():
    print("League Champion Build Generator")
main()