def fun_in_the_sun():
    age = input_()
    return age
def active_kidz():
    age = input_()
    return age
def input_():
    print("what is the childs name?")
    input(">>")
    print("what is the childs age?")
    return float(input(">>"))

#main
program = ""
FITS_count = 0
AK_count = 0
FITS_age = 0.0
AK_age = 0.0
while program != "x":
    print("fun in the sun or active kidz")
    program = input(">>").lower()
    if program == "fun in the sun":
        FITS_age += fun_in_the_sun()
        FITS_count += 1
    elif program == "active kidz":
        AK_age += active_kidz()
        AK_count += 1
    elif program == "x":
        break
    else:
        print("input not valid")
print(f"{AK_count} people signed up for active kidz at an average age of {AK_age/AK_count}")
print(f"{FITS_count} people signed up for fun in the sun at an average age of {FITS_age/FITS_count}")
