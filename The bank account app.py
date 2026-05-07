class BankAccount:
    def __init__(self,balance = 0):
        self._balance = balance

    def deposit(self,amount):
        if amount <=0:
            print("Deposit must be a positive")
        else:
            self._balance += amount  ##this basicly means (new)self._balance = (old)self._balance + amount
            print(f"Deposited ${amount}.New Balance:${self._balance}")

    def withdraw(self,amount):
        if amount <=0:
            print("Amount must be positive")
        elif amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount
            print(f"Withdrew ${amount}.New Balance: ${self._balance}")

    def seebalance(self):
        print(F"Account balance ${self._balance}")

account = BankAccount()
while True:
        print("\n Choose service(1-4)")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Seebalance")  
        print("4.Exit")

        choice = input("Enter option (1-4):")

        if choice == "1":
            amount = int(input("Deposit Amount"))
            account.deposit(amount)

        elif choice == "2":
            amount = int(input("Withdraw Amount"))
            account.withdraw(amount)

        elif choice == "3":
            account.seebalance()

        elif choice == "4":
            print("Goodbye,get yo money up")
            break

        else:
            print("invalid choice")
            
            













    



        
        
                  
        



        

            