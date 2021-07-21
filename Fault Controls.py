while True:
    try:
         value = int(input("Type in a number between 1 and 10 :"))
    except ValueError:
         print ("You must enter a number from 1 to 10 !")
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
    else:
        if value > 0 and value <=10:
            print(f"You typed : {value}")
            break
        else:
            print("Value you typed is incorrect")
            continue
