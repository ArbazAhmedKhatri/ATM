print("    ***************    ****************    *******       *******\n")
print("    ***************    ****************    ********     ********\n")
print("    ****       ****          ****          **** ****   **** ****\n")
print("    ****       ****          ****          ****  **** ****  ****\n")
print("    ***************          ****          ****    ******   ****\n")
print("    ***************          ****          ****     ****    ****\n")
print("    ****       ****          ****          ****             ****\n")
print("    ****       ****          ****          ****             ****\n")
print("    ****       ****          ****          ****             ****\n")
print("    ****       ****          ****          ****             ****\n")



print("WELCOM TO ATM\nput your card and")
pin = int(input("Enter your pin : "))

# this is for pin, 
# if pin will correct so program will run forword, 
# otherthan stop here.
if pin == 1234 : 
   print("Press 1 for current balance\nPress 2 for widthdraw\nPress 3 for Deposite")
   # this is for choices.
   choice = int(input("Enter choice : "))

   #this is for choice 1.
   balance = 37000
   if choice == 1 : 
       print("Your current balnace is : ",balance)

   # this is for choice 2.
   elif choice == 2 : 
       widthdraw = int(input("Enter amount to widthdraw : ")) 
       if widthdraw > balance : print("Sorry! you have insufficient balance")
       else : print("Collect your amount :",widthdraw,"\nYour current balance is : ",balance-widthdraw)

   # this is for choice 3.
   elif choice == 3 : 
       deposite = int(input("Enter amount to deposite : "))
       if deposite > 0: print("Your update balance is : ",deposite+balance)

   # this is for invalid choice.
   else : print("invalid choice, please try again!")
         
#this is for wrong pin.
else:print("invalid pin, please try again!")
