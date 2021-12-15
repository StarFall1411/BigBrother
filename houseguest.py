import random
#names for houseguests
maleNames = ["Liam","Noah","Oliver","William","Elijah",
              "James","Benjamin","Lucas","Mason","Ethan",
              "Alexander","Henry","Jacob","Michael","Daniel",
              "Logan","Jackson","Sebastion","Jack","Aiden","Owen",
              "Samuel","Matthew","Joseph","Mateo","David","John",
              "Wyatt","Carter","Julian","Luke","Grayson","Isaac",
              "Jayden","Theodore","Gabriel","Anthony","Dylan","Leo",
              "Lincoln","Jaxon","Asher","Christopher","Josiah",
              "Andrew","Thomas","Joshua","Ezra","Hudson","Charles"]

femaleNames = ["Olivia","Emma","Ava","Sophia","Isabella","Charlotte",
                "Amelia","Mia","Harper","Evelyn","Abigail","Emily",
                "Ella","Elizabeth","Camila","Luna","Sofia","Avery",
                "Mila","Aria","Scarlett","Penelope","Layla","Chloe",
                "Victoria","Madison","Eleanor","Grace","Nora","Riley",
                "Zoey","Hannah","Hazel","Lily","Ellie","Violet","Lillian",
                "Zoe","Stella","Aurora","Natalie","Emilia","Everly",
                "Leah","Aubrey","Willow","Addison","Lucy","Audrey",
                "Bella"]

lastNames = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
             'P','Q','R','S','T','U','V','W','X','Y','Z']

#/names for houseguests

#the base for Player and HouseGuest to inherit from
class Base:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        
        self.hohWins = 0
        self.vetoWins = 0
        beenNominated = False
        
        self.showmance = ''
        self.alliance = []

#player object
#inherits from Base
class Player(Base):
    def __init__(self,name,gender):
        super().__init__(name,gender)


#houseguest objects
#inherits from Base
#DOES NOT MAKE PLAYER
class HouseGuest(Base):
    def __init__(self,name,gender):
        super().__init__(name,gender)
        self.difficulty = 0

#makes all the houseguests in the house and returns it to main
#inherits from Base
#DOES NOT INCLUDE PLAYER
def houseGuestbuilder(playerGender):
    houseguests = {}
    female = 8
    male = 8
    if playerGender == 'f':
        female -= 1
    else:
        male -= 1
    for i in range(female):
        name = random.choice(femaleNames) + ' ' + random.choice(lastNames) + '.'
        houseguests[name] = HouseGuest(name,'f')
    for i in range(male):
        name = random.choice(maleNames) + ' ' + random.choice(lastNames) + '.'
        houseguests[name] = HouseGuest(name,'m')

    return houseguests 