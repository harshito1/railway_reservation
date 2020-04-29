"""This program contains Railway reservation
and creating a file which include total fare of your
bookings"""
total_fare=0

file = open("File.txt", "w")
#import different class
from ticket_booking import Book_Ticket
book_ticket = Book_Ticket()

for x in range(45):
    print("*", end = '')

print("\n   Railway Reservation")
print("\n       Harshit        ")

for x in range(45):
    print("*", end = '')

while (True):
#Welcome message
    print("""\nMake selection for ticket:
          1 Child\t
          2 Adult\t
          3 Senior\t
          4 Concession\t
          5 Checkout\t""")
#Specifying Amounts and Number of tickets        
    choose = int(input("Choose your ticket:"))
    if choose==1:
        amount = 100
        print("Amount of child tickets: ",amount)
        tickets_req = int(input("How many child tickets you want to buy: "))
       #creating text file 
        file.write("Total amount of ticket: " + str(book_ticket.ticket_(tickets_req, amount)))
        file.write("\n")
        total_fare += book_ticket.ticket_(tickets_req, amount)
#Specifying Amounts and Number of tickets       
    elif choose==2:
        amount = 200
        print("Amouont of Adult ticket : ",amount)
        tickets_req = int(input("How many adult tickets you want to buy: "))
      #creating text file  
        file.write("Total amount of ticket: " + str(book_ticket.ticket_(tickets_req, amount)))
        file.write("\n")
        total_fare += book_ticket.ticket_(tickets_req, amount)
        
#Specifying Amounts and Number of tickets       
    elif choose==3:
        amount = 150
        print("Amount of Senior ticket : ",amount)
        tickets_req = int(input("How many senior tickets you want to buy: "))
     #creating text file   
        file.write("Total amount of ticket: " + str(book_ticket.ticket_(tickets_req, amount)))
        file.write("\n")
        total_fare += book_ticket.ticket_(tickets_req, amount)
#Specifying Amounts and Number of tickets        
    elif choose==4:
        amount = 60
        print("Amount of Concession ticket : ",amount)
        tickets_req = int(input("How many concession tickets you want to buy: "))
     #creating text file   
        file.write("Total amount of ticket: " + str(book_ticket.ticket_(tickets_req, amount)))
        file.write("\n")
        total_fare += book_ticket.ticket_(tickets_req, amount)
#Enter Card Details
    elif choose == 5 :
      #import different class  
        from checkouts import Check
        checkout = Check()
        checkout.card_(total_fare)
        file.write("Total amount: " + str(total_fare))
        file.close()
        print("Ticket booked successfully")
        break
