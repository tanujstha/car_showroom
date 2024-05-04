class cars:
    
    def __init__(self,name):
        self.name = name
        #lists of avaliable cars
        self.cars = ["gt3", "cayenne", "panamera", "macan", "boxster", "cayman", "taycan"] 
        #created a list to store the damaged cars
        self.damaged = []

    #FUNC TO BORROW THE CARS FROM THE LIST 
    def borrowed_cars(self,canr):
        if canr in self.cars:
            self.cars.remove(canr)
            print(f"{canr} borrowed successfullr")
        else:
            print("No cars avaliable")

    # FUNC TO ADD DAMAGED CARS TO THE DAMAGED LIST
    def  damaged_cars(self,canr):
        self.damaged.append(canr)
        if canr in self.damaged:
            print(f"you need to pay the fine {self.name}")

        else:
            print(f"you are free to borrow the car again{self.name}")

    #FUNC TO RETURN THE BORROWED CAR
    def return_car(self,canr):
        if canr not in self.cars:
            self.cars.append(canr)

            print(f" {canr} has successfully been returned by {self.name}")

        else:
            print("car was not borrowed")



class necars:
    def __init__(self):
        self.caars = []
        self.owners = {}
    #ADD CARS IN THE LIST SE CAARS
    def add_cars(self,canr):
        if canr not in self.caars:
            self.caars.append(canr)

        else:
            print("Car is already there")

    #REMOVE CARS FORM THE IST 
    def remove_cars(self,canr):
        if canr in self.caars:
            self.caars.remove(canr)

        else:
            print(f"Car {canr} not in the garage")

    #FUNC TO ADD THE OWNERS OF DIFFERRNT CARS BUT NOT SEQUENTIALLY
    def add_owners(self,name):
        if name not in self.owners:
            self.owners[name] = self.owners
            print(f"New owners added successfully")

        else:
            print("Owners is already registered")

    # FUNC TO RENT THE CARS 
    def rent_cars(self,name,canr):
        if canr in self.caars:
           
            # memb.rent_cars(canr)
            self.caars.remove(canr)
            print(f"{name} rented the car")
        else:
            print("no car avaliable")

    
    def return_rented_car(self,canr):
        if canr not in self.caars:
            self.caars.append(canr)
            print(f"Car {canr} returned successfully")
        else:
            print("Cars already returned ")


    def display_cars(self):
        if self.caars:
            for dis in self.caars:
                print(f"The avaliable cars are {dis}")
        else:
            print("No cars in the garage")


    def show_owners(self):
        if self.owners:
            for owner in self.owners:
                print(f"The car owners are {owner}")

        else:
            print("currently there are no cars owners ")



newcars = necars()
newcars.add_cars("mercedes amg ")
newcars.add_cars("ferrari")

newcars.add_owners("tnauj")
newcars.add_owners("jonny")

# newcars.rent_cars("taaanujj","pagani")

newcars.display_cars()
newcars.show_owners()
newcars.rent_cars("taaanujj","pagani")

amgg = cars("john")
amgg.borrowed_cars("cayman")
amgg.return_car("cayman")




