import random
def main():
  students = [
    Student("Larsson", "Halsted", 0, 1, 1, "Wukong", "top"),
    Student("Desjardins", "Nate", 1, 30, 2, "Anivia", "mid"),
    Student("Desalle", "Samson", 14, 2, 5, "Jhin", "adc"),
    Student("Kreps", "Alex", 30, 15, 3, "Akali", "jungle"),
    Student("Bonney", "Kent", 10, 4, 20, "Bard", "supp"),
  ]

  printHeader()
  selection = getUserSelection()
  if selection == 0:
    printStudentsByAge(students)
  elif selection == 1:
    pass
  elif selection == 2:
    pass
  else:
    print ("SELECTION NOT RECOGNIZED")


class Student:
  names = ['John','Halsted','Nate','Samson','Alex','Meme-Man','Garbage','Bob','Aatrox','Aaron','Peter','George','Kent','Jack','Billy','Mortimer','Rick','Carl','Alfred','Steven','Jerome','Jerimiah']
  lNames = ['Bonjovi','Larsson','Desjardins','Dankness','Benson','McDepressed','Salad','Trashson','Stevenson','Weeabo','Namek','Salty','MacDonald','Tenderoni','Bonney','Kreps']
  lanes = ['mid','adc', 'support', 'top','jungle']
  mainChamps = ['Aatrox','Ahri','Akali','Alistar','Amumu','Anivia','Annie','Ashe','Aurelion Sol','Azir','Bard','Blitzcrank','Brand','Braum','Caitlyn','Camille','Cassiopeia','ChoGath','Corki','Darius','Diana','Dr Mundo','Draven','Ekko','Elise','Evelynn','Ezreal','Fiddlesticks','Fiora','Fizz','Galio','Gangplank','Garen','Gnar','Gragas','Graves','Hecarim','Heimerdinger','Illoai','Irelia','Ivern','Janna','Jarvan IV','Jax','Jayce','Jhin','Jinx','Kalista','Karma','Karthus','Kassadin','Katarina','Kayle','Kennen','KhaZix','Kindred','Kled','KogMaw','LeBlanc','Lee Sin','Leona','Lissandra','Lucian','Lulu','Lux','Malphite','Malzahar','Maokai','Master Yi','Miss Fortune','Mordekaiser','Morgana','Nami','Nasus','Nautilus','Nidalee','Nocturne','Nunu','Olaf','Orianna','Pantheon','Poppy','Quinn','Rammus','RekSai','Renekton','Rengar','Riven','Rumble','Ryze','Sejuani','Shaco','Shen','Shyvana','Singed','Sion','Sivir','Skarner','Sona','Soraka','Swain','Syndra','Tahm Kench','Taliyah','Talon','Taric','Teemo','Thresh','Thresh','Tristana','Trundle','Tryndamere','Twisted Fate','Twitch','Udyr','Urgot','Varus','Vayne','Veigar','VelKoz','Vi','Viktor','Vladimir','Volibear','Warwick','Wukong','Xerath','Xin Zhao','Yasuo','Yorick','Zac','Zed','Ziggs','Zilean','Zyra']
  def __init__(self, lastName, firstName, K, D, A, mainChamp, lane):
    self.assignRandomK()
    self.assignRandomD()
    self.assignRandomA()
    self.randomFirstName()
    self.randomLastName()
    self.randomChampion()
    self.randomLane()

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

  def assignRandomWeight(self, isMetric):
    pass

  def assignRandomHeight(self, isMetric):
    pass
  
  def randomFirstName(self): 
     self.firstName = random.choice(self.names) 
  
  def randomLastName(self):
     self.lastName = random.choice(self.lNames)

inputQuestions = [ 
  "For PLAYERS BY DEATHS, type 0",
  "For STUDENTS BY LAST NAME, type 1",
  "For STUDENTS BY FIRST NAME, type 3",
  "For SUM of STUDENT AGES type 4",
  "For AVERAGE of STUDENT AGES type 5",
]

def getUserSelection():
  print (inputQuestions[0])
  print (inputQuestions[1])
  print (inputQuestions[2])
  return int(input("Type selection and press enter: "))

def printHeader():
    print("HEADER TEXT HERE")

def printStudentsByAge(students):
  print ("----Students By Age-----")
  sortStudents = sorted(students, key=lambda student: student.D)
  for student in sortStudents:
    print (student.lastName + ", " + student.firstName + ", " + str(student.K) + "/" + str(student.D) + "/" + str(student.A) + ", " + str(student.mainChamp) + ", " + str(student.lane))
def printStudentsByLName(students):
  print ("----Students By -----")

def printStudentsByFName(students):
  print ("----Students By -----")

def printSumAge(students):
  print ("Answer:")

def printAvgAge(students):
  print ("Answer:")

def ageRange(studentA, studentB):
  return math.abs(studentA.age - studentB.age)


main()