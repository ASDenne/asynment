def drop_off():
    print()
def pick_up():
    print()
def Printroll():
    print()
def calccost():
    print()
#main
Dogs = []
control = 0
while control != 4:
    print("what do you want to do?")
    print("1 drop a pet off")
    print("2 pick a pet up")
    print("3 print roll")
    print("4 quit")
    control = int(input(">>"))
    while control > 0 and control < 5:
        print("please enter a number between 1 and 4")
        control = int(input(">>"))
    if control == 1:
        print(1)
    elif control == 2:
        print(2)
    elif control == 3:
        print(3)
    else:
        print(4)
