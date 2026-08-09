

                        #=========================================
                                    #PROJECT-3  ATM SYSTEM
                        #=========================================

try:
    accounts = {
        "name": "Hardik Thakor",
        "pin": 3899,
        "balance": 110000.00
    }

    print("--------Welcome To The ATM--------")
    attempt = 0
    max_attempts = 3
    running = False
    while attempt < max_attempts:
        user_pin= int(input("Enter Your PIN :"))

        if accounts["pin"] == user_pin:
            print("Welcome", accounts["name"])
            running = True
            break   
        else:
            attempt += 1
            remaining = max_attempts - attempt
            if remaining == 0:
                print("Access Denied")
                
            else:
                print("Incorrect PIN")


    while running:
            print("====== ATM MENU========")
            print("1.Check Balance")
            print("2.Deposite")
            print("3.Withdraw")
            print("4.Exit")

            choice = input("Enter Your Choice :")

            if choice == "1":
                print("Current Balance :",accounts["balance"])
            elif choice =="2":
                amount = int(input("Enter Deposite Amount :"))
                accounts["balance"] += amount
                print("Your Balance :", amount, "New Balance", accounts["balance"])

            elif choice == "3":
                Withdraw_amount = int(input("Enter Withdraw Amount :"))

                if Withdraw_amount <= accounts["balance"]:
                    accounts["balance"] -= Withdraw_amount
                    print("Withdraw Amount", Withdraw_amount, "Current Balance :", accounts["balance"])
                else:
                    print("Insufficient balance")
            elif choice == "4":
                print("Thank you for using our ATM!")
                running = False
            else:
                print("Invalid Choice")
except ValueError:
    print("Invalid Input")