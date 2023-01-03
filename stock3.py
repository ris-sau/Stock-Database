def access(): 
    question1 = input("What stock symbol would you like to access?\n")
    answer1 = stockdict.get(question1)
    if answer1 == None: 
        return("Invalid. Not in database. ")
    else :
        return("The stock is called " + answer1 + ". " )

def add(): 
    question2 = input("What stock symbol would you like to add?\n")
    question3 = input("What does it stand for?\n")
    stockdict.update({question2:question3})
    return ("It has now been added in! \n" + str(stockdict)) 

def remove(): 
    question4 = input("What stock symbol would you like to remove?\n")
    if question4 in stockdict: 
        del stockdict[question4]
        return("It has now been removed! \n"+  str(stockdict))
    else: 
        return("Invalid. Not in database. ")

def stop():
    return("Thanks for using the program! ")

def view(): 
    return stockdict 


def update(): 
    question5 = input("Would you like to update symbol/stock name?\n")
    if question5 == 'stock name':
        question6 = input("What symbol does this stock have?\n")
        question7 = input("What would the name be changed to?\n")
        if question6 in stockdict: 
                stockdict.update({question6:question7})
                return ("It has now been updated!\n" + str(stockdict))
        else : 
            return ("Invalid. Not in database. ")
    elif question5 == 'symbol':
        question8 = input("What is this symbol's current name?\n")
        question9 = input("What would the symbol be changed to?\n")
        if question8 in stockdict: 
            if question8 == question9: 
                return ("Your change cannot be the same as the original. ")
            else:
                stockdict.update({question9:stockdict[question8]})
                del stockdict[question8]
                return ("It has now been updated!\n" + str(stockdict))
        else: 
            return ("Invalid. Not in database. ")
    else :
        return ("Invalid. Not in database. ")


stockdict = {'TWTR': 'Twitter', 'GOOG': 'Google', 'APPL': 'Apple', 'AMZN' : 'Amazon'} 

while True: 
    ask = input("Would you like to access, add, remove, view, update, or stop?\n")
    if ask == 'add': 
        print (add())
    elif ask == 'access':
        print (access())
    elif ask == 'remove':
        print(remove())
    elif ask == 'view':
        print(view())
    elif ask == 'update':
        print(update())
    elif ask == 'stop':
        print(stop())
        break; 
    else :
        print("Try typing again.")