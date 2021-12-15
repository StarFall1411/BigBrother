import houseguest
import game_core

playerGender  = 'f'#input('Are you [m]ale or [f]emale? ')
#Makes every house guest into an object and appends it to a list except for the player
houseGuests = houseguest.houseGuestbuilder(playerGender)
houseGuestList = []
for person in houseGuests:
    houseGuestList.append(person)

#Adds player to houseGuests and houseGuestList
name = 'Alissa'#input('What is your name? ')
lastName = 'Goff'#input('What is your last name? ')
playerName = name + ' ' + lastName[0] + '.'
houseGuests[playerName] = houseguest.Player(playerName,playerGender)
houseGuestList.append(playerName)

#The whole core of the game running
jury = []
cantPlay = None
onGoing = True
while onGoing:
    hohWinner = game_core.hohCompetition(houseGuestList,houseGuests,cantPlay)
    nom1,nom2 = game_core.nominations(houseGuestList,houseGuests,hohWinner,playerName)
    vetoPlayers = game_core.vetoNominations(houseGuestList,houseGuests,hohWinner,nom1,nom2)
    vetoWinner = game_core.vetoCompetition(houseGuests,vetoPlayers)
    nom1,nom2 = game_core.vetoCeremony(houseGuestList,houseGuests,playerName,vetoWinner,hohWinner,nom1,nom2)
    cantPlay,evictee = game_core.evictionCeremony(houseGuestList,hohWinner,nom1,nom2,jury)
    if evictee == playerName:
        onGoing = False
    if len(houseGuestList) == 3:
        onGoing = False
#Final moments of the game
if evictee != playerName:
    finalWinner = game_core.finalThreeCompetitions(houseGuestList,houseGuests)
    game_core.finalThreeVote(houseGuestList,finalWinner,jury)
    game_core.finalJuryVotes(houseGuestList,jury)