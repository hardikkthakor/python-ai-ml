

                        #=========================================
                                    #PROJECT-3  ATM SYSTEM
                        #=========================================


accounts = {
    "name": "Hardik Thakor",
    "pin": 3899,
    "balance": 110000.00
}

print("--------Welcome To The ATM--------")
user_pin= int(input("Enter Your PIN :"))

if accounts["pin"] == user_pin:
    print("Welcome", accounts["name"])
    running = True
else:
    print("Access Denied")


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
