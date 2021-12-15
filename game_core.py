import random
import houseguest
import required_functions

def hohCompetition(houseGuestList,houseGuests,cantPlay):
    canPlay = houseGuestList[:]
    if cantPlay is not None:
        canPlay.remove(cantPlay)
    winner = random.choice(houseGuestList)
    input('\n' + winner + ' wins HOH!')
    houseGuests[winner].hohWins += 1
    return winner

def nominations(houseGuestList,houseGuests,hohWinner,playerName):
    i = True
    while i:
        if hohWinner == playerName:
            nom1,nom2 = required_functions.userInput('nominations',houseGuestList)
        else:
            nom1 = random.choice(houseGuestList)
            nom2 = random.choice(houseGuestList)
        if hohWinner is not nom1 and hohWinner is not nom2 and nom1 is not nom2:
            i = False
            input(hohWinner + ' has nominated...')
            input(nom1 + ' and ' + nom2 + ' for eviction!\n')
            houseGuests[nom1].beenNominated = True
            houseGuests[nom2].beenNominated = True
    return nom1,nom2

def vetoNominations(houseGuestList,houseGuests,hohWinner,nom1,nom2):
    print('The Veto players are!:')
    playingVeto = []
    if len(houseGuestList) < 6:
        for person in houseGuestList:
            print(person)
            playingVeto.append(person)
        input()
        return playingVeto
    playingVeto = [hohWinner,nom1,nom2]
    guestList = houseGuestList[:]
    guestList.remove(hohWinner)
    guestList.remove(nom1)
    guestList.remove(nom2)
    count = 0
    while count < 3:
        chosen = random.choice(guestList)
        playingVeto.append(chosen)
        guestList.remove(chosen)
        count += 1
    for person in playingVeto:
        print(person)
    input()
    return playingVeto

def vetoCompetition(houseGuests,vetoPlayers):
    vetoWinner = random.choice(vetoPlayers)
    houseGuests[vetoWinner].vetoWins += 1
    input(vetoWinner + ' has won the Veto competition!')
    return vetoWinner

def vetoCeremony(houseGuestList,houseGuests,playerName,vetoWinner,hohWinner,nom1,nom2):
    #Removes people from houseGuestList that can be nominated if veto is used
    guestList = houseGuestList[:]
    if vetoWinner == hohWinner:
        guestList.remove(hohWinner)
        guestList.remove(nom1)
        guestList.remove(nom2)
    elif vetoWinner == nom1:
        guestList.remove(hohWinner)
        guestList.remove(vetoWinner)
        guestList.remove(nom2)
    elif vetoWinner == nom2:
        guestList.remove(hohWinner)
        guestList.remove(vetoWinner)
        guestList.remove(nom1)
    else:
        guestList.remove(hohWinner)
        guestList.remove(vetoWinner)
        guestList.remove(nom1)
        guestList.remove(nom2)
    #Happens if player wins veto
    if vetoWinner == playerName:
        required_functions.userInput('power of veto',guestList,playerName)
    #if nom1 or nom2 is vetoWinner, they get taken off and an elidgable person gets nominated
    if vetoWinner == nom1:
        input(nom1 + ' has decided...')
        input('To use the power of veto on themself!')
        nom1 = random.choice(guestList)
        houseGuests[nom1].beenNominated = True
        input('The HOH, ' + hohWinner + ', has nominated ' + nom1 + ' for eviction!')
    elif vetoWinner == nom2:
        input(nom2 + ' has decided...')
        input('To use the power of veto on themself!')
        nom2 = random.choice(guestList)
        houseGuests[nom2].beenNominated = True
        input('The HOH, ' + hohWinner + ', has nominated ' + nom2 + ' for eviction!')
    #Happens if nom1 or nom2 is not the vetoWinner
    else:
        vetoChoice = random.choice(['yes','no'])
        if len(houseGuestList) == 4:
            input(vetoWinner + ' has decided...')
            input('Not to use the power of veto!')
            return nom1,nom2
        #veto is used
        if vetoChoice == 'yes':
            vetoChoice = random.choice([nom1,nom2])
            #veto is used on nom1
            if vetoChoice == nom1:
                input(vetoWinner + ' has decided...')
                input('To use the power of veto on ' + nom1 + '!')
                nom1 = random.choice(guestList)
                houseGuests[nom1].beenNominated = True
                input('The HOH, ' + hohWinner + ', has nominated ' + nom1 + ' for eviction!')
            #veto is used on nom2
            elif vetoChoice == nom2:
                input(vetoWinner + ' has decided...')
                input('To use the power of veto on ' + nom2 + '!')
                nom2 = random.choice(guestList)
                houseGuests[nom2].beenNominated = True
                input('The HOH, ' + hohWinner + ', has nominated ' + nom2 + ' for eviction!')
        #veto is not used
        elif vetoChoice == 'no':
            input(vetoWinner + ' has decided...')
            input('Not to use the power of veto!')
    return nom1,nom2

def evictionCeremony(houseGuestList,hohWinner,nom1,nom2,jury):
    #Removes hohWinner, nom1, and nom2 from voting in the ceremony
    votingList = houseGuestList[:]
    votingList.remove(hohWinner)
    votingList.remove(nom1)
    votingList.remove(nom2)
    nom1Votes = 0
    nom2Votes = 0
    #guests are voting here
    for guest in votingList:
        voteChoice = random.choice([nom1,nom2])
        if voteChoice == nom1:
            nom1Votes += 1
        elif voteChoice == nom2:
            nom2Votes += 1
    #If there is a tie, the HOH casts a vote to evict
    if nom1Votes == nom2Votes:
        input('\nThere has been a tie. The HOH will cast the deciding vote to evict')
        evictee = random.choice([nom1,nom2])
        input('The HOH, ' + hohWinner + ', voted to evict ' + evictee + '!')
        if len(houseGuestList) <= 11:
            jury.append(evictee)
        houseGuestList.remove(evictee)
        return hohWinner,evictee
    #nom1 is evicted
    if nom1Votes > nom2Votes:
        input('\nBy a vote of  ' + str(nom1Votes) + '-' + str(nom2Votes) + '...')
        input(nom1 + ' has been evicted!')
        if len(houseGuestList) <= 11:
            jury.append(nom1)
        houseGuestList.remove(nom1)
        return hohWinner,nom1
    #nom2 is evicted
    elif nom2Votes > nom1Votes:
        input('\nBy a vote of  ' + str(nom2Votes) + '-' + str(nom1Votes) + '...')
        input(nom2 + ' has been evicted!')
        if len(houseGuestList) <= 11:
            jury.append(nom2)
        houseGuestList.remove(nom2)
        return hohWinner,nom2
    
def finalThreeCompetitions(houseGuestList,houseGuests):
    houseGuestsCopy = houseGuestList[:]
    input("It's time for the final three competitions!")
    #First competition
    winner1 = random.choice(houseGuestsCopy)
    houseGuestsCopy.remove(winner1)
    input(winner1 + ' won the first competition!')
    #Second competition
    winner2 = random.choice(houseGuestsCopy)
    input(winner2 + ' won the second competition!')
    #Third competition
    finalWinner = random.choice([winner1,winner2])
    houseGuests[finalWinner].hohWins += 1
    input(finalWinner + ' won the last HOH competition! They will now vote on who to bring to the final two')
    return finalWinner

def finalThreeVote(houseGuestList,finalWinner,jury):
    houseGuests = houseGuestList[:]
    houseGuests.remove(finalWinner)
    input(finalWinner + ' has voted to evict...')
    #HOH winner chooses the last person to evict
    evictee = random.choice(houseGuests)
    input(evictee)
    jury.append(evictee)
    houseGuestList.remove(evictee)

def finalJuryVotes(houseGuestList,jury):
    #jury votes on who to win
    input("It's time for the jury to vote ")
    final1 = 0
    final2 = 0
    for person in jury:
        input(person + ' has voted... ')
        choice = random.choice(houseGuestList)
        if choice == houseGuestList[0]:
            final1 += 1
        else:
            final2+= 1
    #Votes are revealed
    input('The votes are in ')
    if final1 > final2:
        input('By a vote of ' + str(final1) + ' to ' + str(final2) + '... ')
        input(houseGuestList[0] + ' has won!')
    else:
        input('By a vote of ' + str(final2) + ' to ' + str(final1) + '... ')
        input(houseGuestList[1] + ' has won!')

# jury = []
# houseGuestList = ['Levi','Alissa','David']
# finalWinner = finalThreeCompetitions(houseGuestList)
#finalThreeVote(houseGuestList,finalWinner,jury)
# houseGuestList = ['Alissa','Levi','David','Erick','Liam','Reid','Mom','Dad','Kayle','Jason','Chris',]
# hohWinner = 'Levi'
# nom1 = 'David'
# nom2 = 'Erick'
# evictionCeremony(houseGuestList,hohWinner,nom1,nom2)






    