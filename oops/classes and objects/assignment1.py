class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    

car1=car("toyota","camry",202)
print(car1.make,car1.model,car1.year)