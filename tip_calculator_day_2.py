#!/usr/bin/env
#Python Program to calculate the total bill and the tip
#and split the bill among the number of people

class Bill:
    __actual_bill = None
    __total_bill = None
    __tip_percent = None
    __number_of_splits = None
    __share_per_person = None


    def __init__(self):
        self.__actual_bill = 0
        self.__total_bill = 0
        self.__tip_percent = 0
        self.__number_of_splits = 0
        self.__share_per_person = 0

    def __calculate_total_bill(self):
        self.__total_bill = self.__actual_bill + (self.__actual_bill * self.__tip_percent) / 100
        return
    def __calculate_share_per_person(self):
        self.__share_per_person = self.__total_bill/self.__number_of_splits
        return
    def set_bill_value(self, value):
        self.__actual_bill = float(value)
        return
    def set_number_of_persons(self,value):
        self.__number_of_splits = float(value)
        return
    def set_tip_percent(self,value):
        self.__tip_percent = float(value)
        return
    def tip_calculator(self):
        self.__calculate_total_bill()
        self.__calculate_share_per_person()
        return self.__share_per_person

def main():
    print("Welcome to the tip calculator")
    obj1 = Bill()
    obj1.set_bill_value(input("What was the bill amount? $"))
    obj1.set_number_of_persons(input("How many people to split the bill? "))
    obj1.set_tip_percent(input("What percentage of tip you would like to give? 10 , 12 or 15? "))
    output = obj1.tip_calculator()
    print("Each person has to pay : $" + str(output))



if __name__=="__main__":
    main()