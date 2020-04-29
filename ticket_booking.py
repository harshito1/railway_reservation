class Book_Ticket():
#Calculate Total amount
    def ticket_(self, numbers, amount):
        self.numbers = numbers
        self.amount = amount
        total_fare = numbers*amount
        
        return total_fare    
