#!/usr/bin/env/ python3
score = 67
if score < 80 and score > 70:
    print("A")
elif score < 90 or score > 80:
    print("B")
elif score > 60:
    print("C")
else:
    print("D")
def interchange(list,N):
    length = len(list)
    temp = list[0]
    list[0] = list[length-1]
    list[length-1] = temp
    return list

def print_list(list1):
    print(list1)
    return

def main():
    N = input("Enter the number of elements in the list")
    N = int(N)
    list = []
    for i in range(0,N):
        print("Please enter" + str(i) + "element")
        list.append(input())
    print(list)
    new_list = interchange(list,N)
    print("New list \n")
    print(list)
    return

if __name__ == "__main__":
    main()
