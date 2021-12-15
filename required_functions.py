def UserInput(type,houseGuestList,playerName):
    if type == 'nominations':
        #Prints players availible to nominate
        for guest in houseGuestList:
            if guest != playerName:
                print(guest)
        nom1 = input('Enter your first nomination ')
        nom2 = input('Enter your second nomination ')
        print('\n')
        return nom1,nom2
    elif type == "powerofveto":
        pass

    elif type == 'evictionceremony':
        pass