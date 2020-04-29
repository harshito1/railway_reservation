class Check():
    
    def card_(self, total_fare):
        self.total_fare = total_fare
#Valid Details of Card        
        while(True):
            name = input("Enter name")
            card_no = input("Enter card no")
            if len(card_no)!=12:
                print("enter valid details")
            else:
                break
        return "{} total ticket fare is{}".format(name,total_fare)
