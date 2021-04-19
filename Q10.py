class My_class():
    def __init__(self,Distance_Km,Time_Hr):
        self.Distance_Km=Distance_Km
        self.Time_Hr=Time_Hr
    def speed (self):
        return (self.Distance_Km/self.Time_Hr)
car = My_class(250,5)
print(str(car.speed()) +' Km/Hr')
