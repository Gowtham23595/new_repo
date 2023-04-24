#!/usr/bin/env python3

class band:
        def __init__(self,city,pet):
            self.city  = city
            self.pet = pet
        def print_city(self):
            print("Band name is  " + str(self.city+self.pet) + " \n Have a good day\n")

def main():
    obj1 = band("aus","kang")
    obj1.print_city()
    obj1.city = "India"
    obj1.pet = "Lion"
    obj1.print_city()



if __name__ == "__main__":
    main()