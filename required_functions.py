def UserInput(type,guestList,playerName,nom1,nom2):
    if type == 'nominations':
        #Prints players availible to nominate
        for guest in guestList:
            if guest != playerName:
                print(guest)
        nom1 = input('Enter your first nomination ')
        nom2 = input('Enter your second nomination ')
        print('\n')
        return nom1,nom2

    elif type == "powerofveto":
        #Asks player if they would like to use the power of veto
        answer = input('Would you like to use the power of veto? yes/no ')
        if answer == 'yes':
            #Prints players availible to veto
            print(nom1)
            print(nom2)
            nom = input('Who would you like to veto?')
            return answer,nom
        else:
            return 'no'

    elif type == 'hohvetoreplacement':
        for guest in guestList:
            if guest != playerName:
                print(guest)
        print('As the HOH, you have the power to nominate a new person for eviction')
        result = input('Who would you like to nominate for eviction? ')
        return result


    elif type == 'evictionceremony':
        pass