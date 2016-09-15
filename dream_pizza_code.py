'''
Dream Pizza Co. Phone Ordering System
Designed and programmed by Joel Robertson
6 September 2013
New Plymouth Boys' High School

This program allows a pizza company telephone operator to record and manage pizza orders as they are ordered and completed.

'''

#DISPLAYPIZZALIST
#this function is for printing the list of available pizzas and their prices
#this is useful to have in a function because it is quite messy code and would make the full program harder to read. 
def displaypizzalist(): 
    print("\nPIZZA MENU")
    print((("_")*60)+"\n") #looks like a horizontal rule, and is easier to repeat one string many times than write the entire thing in code
    for i in range(0,7): #because there are 7 pizzas in the list it repeats the print 7 times
        print("\t|\t" +str(i+1) + ". \t" + str(pizzasale[0][i]) + "\t" + "$" + str("{:0.2f}".format(pizzasale[1][i])))
#       \t are for tabs^                       ^ prints out pizza name i from pizzalist sublist 1 (pizza names)
#                       ^^string here prints out a number for reference     ^^ this string prints pizza price from pizzalist sublist 2 (prices)
    print((("_")*60)) #looks like a horizontal rule

#REMOVEORDER
#this function allows an order to be removed from the order lists
#this is a function because it is called upon more than once in the program in seperate places
#originally this function consisted of two separate functions, removeorder and removelastorderbut with a few lines of code this one can now do the jobs of both
#decided to implement the ordernumber or False mechanism to save on space and make my functions more efficient
def removeorder(order): #takes the number of the order to be completed and makes it available to the function as order
#If the value sent to the function is a boolean False then the last order will be removed. This saves having a separate function for removing the last order.
    if order == False: #if the order being removed is to be the last, then order will have a False value, and the completeorder will be set to the last order in each order variable list
        completeorder = -1
    else:
        completeorder = ordernumber.index(order) #finds the location of order in the ordernumber list, so it knows which list position to delete.
       #This is the easiest way to find the specified order within the list of orders that have been made. Referencing to a list index can't work because it would muck up when an order was completed.
    ordernumber.pop(completeorder) #all of the pop statements simply take the order'th value out of the list they are functioning on, in this case ordernumber
    orderpizzatype.pop(completeorder) #.pop() command is great because it removes the value at index () (in this case (completeorder) and everything gets shifted in the list to compensate.
    orderpizzaprice.pop(completeorder)
    orderpizzanum.pop(completeorder)
    ordertotalcost.pop(completeorder)
    orderdelivery.pop(completeorder)
    orderaddress.pop(completeorder)
    orderphone.pop(completeorder)
    if order == False: #if the order being removed is the last then this will print out "ORDER REMOVED" to show that the order has ben removed.
        print("\nORDER CANCELLED")
        global ordercounter
        ordercounter-=1 #this will also take one off the ordercounter number so that the recreated order will have the same number as the deleted one and the number won't get skipped

#DISPLAYORDERS
#this a function which can print either the last order placed or all of the orders currently uncompleted
#originally this function consisted of two different functions, displayallorders and displaylastorder but with a few lines of code this one can now do the jobs of both
#program either sends True or False to the function. True will print every order that is uncompleted, whereas False will print only the last order placed.
def displayorders(allorders): #True or False value sent to function becomes available as allorders within the function
    if allorders ==True: #if allorders is True then the function should print every uncompleted order
        print("\nUNCOMPLETED ORDERS")
        maxorder = len(ordernumber)+1 #this makes maxorder (the maximum number of the orders to be printed) equal to the number of orders already placed (via ordernumber list)
    else:
        print("\nDETAILS FOR LAST ORDER") #if allorders is False then the function should print every uncompleted order
        maxorder = 2 #this makes the maxorder just two, so only one item will be printed
    print((("_")*60)) #looks like a horizontal rule
    for i in range (1,maxorder): #for the number of orders currently incomplete, repeat the display process.
                                            #It goes from 1 to the number of orders +1 because to print the orders in reverse (most recent to least recent) it uses -i rather than i.
        print("\n\t|\tOrder No. " + str(ordernumber[-i])) #prints the number of the order since the beginning of time
        if orderdelivery[-i]==True: #if the i'th to last item in orderdelivery is True, the i'th to last order was for delivery
            print("\t|\tOrder is for delivery.")
            print("\t|\tName:\t" + ordername[-i]) #print the name for the order
            print("\t|\tAddress:\t" + orderaddress[-i]) #print the address for the order
            print("\t|\tPhone:\t" + orderphone[-i]) #print the phone number for the order
        else: #if the i'th to last item in orderdelivery is NOT True, the i'th to last order was for pickup
            print("\t|\tOrder is for pickup.")
            print("\t|\tName:\t" + ordername[-i]) #print the name for the order
        print("\t|\n\t|\tPizzas ordered:") #this begins the printing of all of the pizzas that were ordered for the particular order
        for ii in range(0,(orderpizzanum[-i])): #ii is just the new loop counter variable. 0,orderpizzanum[-i] references to the the number of pizzas for i'th to last order
            print("\t|\t" +str(ii+1) + ". \t" + str(orderpizzatype[-i][ii]) + "\t" + "$" + str("{:0.2f}".format(orderpizzaprice[-i][ii])))
#       \t are for tabs^                       ^ prints out pizza name i from orderpizzatype sublist 1 (pizza names)
#                       ^^string here prints out each pizza with its own number     ^^ this string prints pizza price from orderpizzalist sublist 2 (prices)
        if orderdelivery[-i]==True: #if the order is for delivery then print that the delivery charge is $3
            print("\t|\t\tDelivery charge:\t$3.00")
        print("\t|\t\tTotal order cost:\t$" + str("{:0.2f}".format(ordertotalcost[-i]))) #prints the total order cost (ordertotalcost) variable to 2 decimal places for currency continuity.
        print((("_")*60)) #looks like a horizontal rule

#beginning of main programme

pizzasale = [["Hawaiian\t","Meatie\t","Vege\t","Mushroom","Chicken\t","Italian\t","Pigout\t"],[5,5,5,5,8.5,8.5,8.5]] #set pizzas for sale and thier prices (in $) under one list with two sublists
delivery = 3 #sets delivery charge to $3 dollars
ordercounter = 0 #starts the ordercounter at 0
ordernumber = [] #creates a list for ordernumbers to go into
orderdelivery = [] #creates a list for whether an order is for delivery or not
ordername = [] #creates a list for the names under which orders are placed
ordertotalcost = [] #creates a list for the totalcost of orders to go into
orderphone = [] # creates a list for the order phone numbers
orderaddress = [] # creates a list for the order addresses to go into
orderpizzatype = [] #creates a list for lists of pizza types to go into for orders
orderpizzanum = [] #creates a list for the number of pizzas in each order to go into
orderpizzaprice = [] #creates a list for the pizza prices to go into for orders
ordering=True #makes the program start with a new order

while True: #repeats the entire program indefinitely so that an infinite number of orders are able to be placed. This was sensible in this context because the ordering system has no real beginning and end.
    while ordering==True:
        ordercounter += 1 #increase order number by 1 so that the order has a unique number. The order number could be used for both referencing for the customer and it is the basis of order completion.
        ordernumber.append(ordercounter) #add the order number to a list of current order numbers. The .append() command is very good because it adds on to the end of a list
        orderpizzatype.append([],) #add a new sublist (for the new order) to orderpizzatype list which contains the types of pizzas ordered
        orderpizzaprice.append([],) #add a new sublist (for the new order) to orderpizzaprice list which contains the prices of pizzas ordered
        print("\nNEW ORDER\n")
        deliverytemp = str(input("Is order for delivery? Y/N ")).lower().strip() #find if order is for delivery and convert to lower case and strip of any spaces
        if deliverytemp=="y" or deliverytemp=="yes":  #if the program detects that the order is for delivery then it will record this in the orderdeliverylist and add $3 for delivery to the order's total cost
            #only y and yes are necessary here because I think that the user of the system is likely to be quite careful about his/her input, so nothing too stupid should be typed in expecting to be valid.
            orderdelivery.append(True) #add True to orderdelivery
            ordertotalcost.append(float(3)) #make initial order cost $3
        else:
            orderdelivery.append(False) #add False to orderdelivery
            ordertotalcost.append(float(0)) #make inital order cost $0
        nametemp = str(input("Enter customer name: ")) #get customer name
        ordername.append(nametemp) #add customer name to ordername
        if orderdelivery[-1] == True: #if last item in list orderdelivery is True
            phonetemp = str(input("Enter customer contact number: ")) #ask for phone number
            orderphone.append(phonetemp) #add phone number to orderphone
            addresstemp = str(input("Enter customer delivery address: ")) #ask for address
            orderaddress.append(addresstemp) #add address to orderaddress
        else: #if last item in list orderdelivery isn't true
            orderphone.append(False) #add a False to orderphone
            orderaddress.append(False) #add a False to orderaddress
        integermarker= False #integermarker is set to false because in the loop below, the question of how many pizzas in the order must be answered with an integer between 1 and 10.
        #until this criteria is met then the loop needs to repeat, and thus a while loop on the condition of integermarker being false satisfies this requirement.
        while integermarker == False:
            pizzanumtemp = (input("Enter number of pizzas to order (up to 10): ").strip()) #asks for the number of pizzas and then strips the answer of any spaces
            try: #try loops are used when the result may produce an error. It will try the following code and if no errors are detected the loop will finish.
                pizzanumtemp=int(pizzanumtemp) #convert the number of pizzas from a string to an integer.
                if pizzanumtemp<11 and pizzanumtemp>0: #if the integer is between 1 and 11 then the program can continue
                    orderpizzanum.append(pizzanumtemp) #add the number of pizzas in the order to orderpizzanum list which is referenced when printing the order.
                    integermarker = True #ends the while loop and progresses to next stage of program
                else: #if the integer is not between 1 and 11
                    raise ValueError #then raise a valueerror which will trigger failure of the try loop.
                    #it is convenient to trigger an error here on purpose to avoid re-writing the string that needs to be printed and instead use existing code.
            except ValueError or TypeError: #if the try loop returns an error of value or type then the following code will be executed
                print("'"+str(pizzanumtemp)+ "' is not a whole number between 1 and 10. Try again.\n") #tells user that what they have entered does not satisfy requirements of the question
        displaypizzalist() # runs the displaypizzalist function which prints the list of pizzas that can be ordered. It is nice to have this in a module so it doesn't clutter up the code here.
        for i in range (0,orderpizzanum[-1]): #for the number of pizzas which are being ordered
            integermarker= False #integermarker is false again because of the same situation where an integer which meets the requirements of the question must be entered.
            while integermarker == False: #while a correct answer has not been given
                pizzatemp = (input("\nEnter pizza type number code for pizza " + str(i+1) + " / " + str(orderpizzanum[-1]) + ": ").strip()) #ask for the code of the pizza which is to be ordered (provided in pizzalist) and strip it of any spaces.
                try: #try to execute following code and if errors occur jump down to except
                    pizzatemp = int(pizzatemp) #try to convert the code to an integer
                    if pizzatemp > 0 and pizzatemp < 8: # if the code has been converted to an integer without error, then check if it meets the requirement of being between 1 and 7
                        orderpizzatype[-1].append(pizzasale[0][pizzatemp-1]) #this adds a new value, equal to the name of the pizza being ordered, to the last sublist (so the latest order) of orderpizzatype
                        orderpizzaprice[-1].append(pizzasale[1][pizzatemp-1]) #similar principle to function above, except adds price value of the pizza being ordered rather than name, to last sublist of orderpizzaprice
                        ordertotalcost[-1] += float(pizzasale[1][pizzatemp-1]) #this adds the price of the pizza being ordered to the last element (the cost of the current order) of ordertotalcost
                        integermarker = True #quit out of the loop
                    else: #if the integer is not between 1 and 7 then raise an error which will trigger the except part of the try loop
                        raise ValueError
                except ValueError or IndexError or TypeError: #if an error of the listed types occurs within the try loop then it will come to this statement
                    print("'"+str(pizzatemp)+ "' is not a valid selection. Try again.") #alert user to invalid entry and then the loop starts again asking them to enter a correct value.
        displayorders(False) #runs the displayorders function and sends a value of False, which correlates to the function only printing the last order in all lists, which is the one that has just been placed.
        ordercorrect=str(input("\nIs this order correct? Y/N ")).lower().strip() #this asks the user if the order they have just placed (which has just been printed) is correct
        if ordercorrect=="n" or ordercorrect=="no": #if the order is not correct
            removeorder(False) #runs the removeorder value and sends a value of false to the function indicating to delete the last order in all lists, which is the one that has just been placed
        else: #if the order is correct
            ordering=False #ordering is now complete and the while loop of ordering can be discontinued until a new order is to be placed.


    displayall = str(input("\nWould you like to display all orders? Y/N ")).lower().strip() #asks user if they would like to display all of the orders uncompleted.
    while displayall == "y" or displayall == "yes": #if the user indicates that they would like to display all of the currently uncompleted orders
        displayorders(True) #runs the displayorder function and sends a true value to the function which causes all orders to be printed out from most recently placed to least recent.
            #this means that the orders which have been uncompleted for the longest are at the bottom of the page where the operator is looking, so he can easily complete them.
        completeorder = str(input("\nWould you like to mark an order as complete? Y/N ")).lower().strip() #asks if the user wants to complete any orders or not
        if completeorder == "y" or completeorder == "yes": #if the user does want to complete an order
            integermarker= False # integermarker is false because thus far a correct answer has not been given
            while integermarker == False: # while a correct answer has not been given
                ordertocomplete = (input("\nWhich order number would you like to complete? ")) #find out which ordernumber is destined for completion by the user
                try: # try to execute the following code without any errors. If errors do crop up and are listed with the Except statement then run that code instead.
                    ordertocomplete = int(ordertocomplete) #convert the string of the ordertocomplete into an integer that can be user for reference to index
                    inordernumber = any(ordertocomplete == i for i in ordernumber) #the any function finds whether a certain value (in this case the value of ordertocomplete) is in a list (in this case ordernumber)
                    if inordernumber == True: #if the ordernumber specified does exist in the ordernumber list
                        removeorder(ordertocomplete) #remove this order by running the removeorder function and sending it a value of the ordertocomplete
                        integermarker = True #end the while loop by settin integermarker to true
                    else: #if the ordernumber specified does not exist in the ordernumber list
                        raise ValueError #raise an error that will trigger the Except statement of the Try loop. This is easier than writing the same print statement twice.
                except ValueError or IndexError or TypeError: #if one of these error types comes up when executing the Try loop
                        print("'"+str(ordertocomplete)+ "' is not a valid order number. Try again.") #tell the user that their ordernumber is not valid, and then jump back up to asking them for an ordernumber
            if len(ordernumber)>0 : #if there are one or more orders still in ordernumber list
                    print("\nOrder completed.")
            else: #if there are no more orders left
                    print("\nAll orders completed.")
                    displayall ="n" #this will exit the displayall loop and return to ordering
        else: #if completeorder is not y or yes it must be a no
            displayall="n" #this will exit the displayall loop and return to ordering
    ordering=True #when the user has said no to printing all orders, then ordering becomes true and the program repeats itself in the While True loop.
