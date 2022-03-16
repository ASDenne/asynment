def drop_off():
    Dogs.append(input("whats thier name"))

def pick_up():
    leaving = input("whats thier name")
    if leaving in Dogs:
        Dogs.remove(leaving)
        print(leaving+"removed")
    else:
        print("not in register")
def Printroll():
    print(Dogs)
def calccost():
    print(len(Dogs)*22.5)
#main
Dogs = []

control = 0
Dogs
while control != 5:
    print("what do you want to do?")
    print("1 drop a pet off")
    print("2 pick a pet up")
    print("3 print roll")
    print("4 money made today")
    print("5 shut down")
    control = int(input(">>"))
    while control > 6 and control < 0:
        print("please enter a number between 1 and 4")
        control = int(input(">>"))
    if control == 1:
        drop_off()
    elif control == 2:
        pick_up()
    elif control == 3:
        Printroll()
    elif control == 4:
        calccost()

