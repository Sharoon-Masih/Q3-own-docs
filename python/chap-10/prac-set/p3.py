class Train:
    noOfSeat = 50; 
    bookStatus = False; 
    def __init__(self,name,date):
        self.name = name; 
        self.date = date; 

    def bookTicket(self,trainName="Greenline" or "Tezgam" or "Karakoram"):
        self.bookStatus = True
        self.trainName = trainName
        return f'Your Ticket is booked Successfully \n name = {self.name} \n date = {self.date} \n train = {self.trainName}'
    
    def getStatus(self):
        if (self.bookStatus):
            self.noOfSeat -= 1
            return f'Ticket Status : Booked \n Remaining Seats = {self.noOfSeat}'
        else:
            return f'Ticket Status : Not Booked \n Remaining Seats = {self.noOfSeat}'
    @staticmethod
    def getCurrenTrains():
        return '1-Greenline \n2-Tezgam \n3-Karakoram'
    

passenger1 = Train('sharoon','2-8-2024'); 
print(passenger1.getCurrenTrains())
print(passenger1.getStatus())
print(passenger1.bookTicket("Greenline"))
print(passenger1.getStatus())

passenger2 = Train('jane','2-8-2024'); 
print(passenger2.getCurrenTrains())
print(passenger2.getStatus())
print(passenger2.bookTicket("tezgam"))
print(passenger2.getStatus())