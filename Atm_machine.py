class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.menu()

    def menu(self):
        user_input = input(
            """
What would you Like to do?
1. Press 1 to Create Pin
2. Press 2 to Deposit 
3. Press 3 to Withdraw
4. Press 4 to Check Balance
5. Press 5 to Exit
"""
        )
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            exit
        else:
            print("Invalid Input")

    def create_pin(self):
        self.__pin = input("Enter Your Pin")
        print("Pin Set Successfully")
        self.menu()

    def deposit(self):
        pin = input("Enter Your Pin")
        if pin == self.__pin:
            amount = int(input("Enter the amount to deposit"))
            self.__balance += amount
        else:
            print("Invalid Pin")
        self.menu()

    def withdraw(self):
        pin = input("Enter Your Pin")
        if pin == self.__pin:
            amount = int(input("Enter the amount to Withdraw"))
            if amount < self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin")
        self.menu()

    def check_balance(self):
        pin = input("Enter Your Pin")
        if pin == self.__pin:
            print(self.__balance)
        else:
            print("Invalid Pin")
        self.menu()
atm=Atm()