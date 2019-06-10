hungry = input("Are you hungry: ")
if hungry == "yes":
    cook = input("do you have any food left?")
    if cook == "yes":
        print("Eat it")
    else:
        print("Then cook and eat")

    print("Eat your food")
else:
    print("Its time to sleep")