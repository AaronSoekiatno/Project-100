import keyboard

class Atm:
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    
def CashWithdrawl():
    print("Cash has been withdrawn")

def BalanceEnquiry(balance):
    print("You have",balance,"in your bank account")

def main():
    card = input("Enter card number")
    pin = input("Enter you PIN number")
    balance = input("Enter desired amount to store")
    print("Your card number is",card)
    print("Your PIN number is",pin)

    if keyboard.read_key() == "w":
        CashWithdrawl()
    elif keyboard.read_key() == "b":
        BalanceEnquiry(balance)
main()
