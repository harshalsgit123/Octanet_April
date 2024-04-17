class ATM:
    def __init__(self):
        self.users = {
            '1234': {'pin': '1111', 'balance': 1000, 'transaction_history': []},
            '5678': {'pin': '2222', 'balance': 2000, 'transaction_history': []},
            '1000': {'pin':'1000', 'balance':40000, 'transaction_history': []}
        }
        self.current_user = None

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id]['pin'] == pin:
            self.current_user = user_id
            print("Login successful.")
            self.show_menu()
        else:
            print("Please check user id again and password.")

    def show_menu(self):
        while True:
            print("\nATM Menu:")
            print("1. View Transaction History")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Transfer Money")
            print("5. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_transaction_history()
            elif choice == '2':
                self.withdraw_money()
            elif choice == '3':
                self.deposit_money()
            elif choice == '4':
                self.transfer_money()
            elif choice == '5':
                print("please visit again!")
                break
            else:
                print("Invalid choice.")



    def view_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.users[self.current_user]['transaction_history']:
            print(transaction)




    def withdraw_money(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= self.users[self.current_user]['balance']:
            self.users[self.current_user]['balance'] -= amount
            self.users[self.current_user]['transaction_history'].append(
                f"Withdrew ${amount}")
            print("Withdrawal successful.")
            print("Remaining balance:", self.users[self.current_user]['balance'])
        else:
            print( "insufficient balance.")


    def deposit_money(self):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.users[self.current_user]['balance'] += amount
            self.users[self.current_user]['transaction_history'].append(
                f"Deposited ${amount}")
            print("Deposit successful.")
            print("New balance:", self.users[self.current_user]['balance'])
        else:
            print("Invalid amount.")

    def transfer_money(self):
        receiver_id = input("Enter receiver's user ID: ")
        if receiver_id in self.users:
            amount = float(input("Enter amount to transfer: "))
 
            if amount > 0 and amount <= self.users[self.current_user]['balance']:
                self.users[self.current_user]['balance'] -= amount
                self.users[receiver_id]['balance'] += amount
                self.users[self.current_user]['transaction_history'].append(
                    f"Transferred ${amount} to {receiver_id}")
                self.users[receiver_id]['transaction_history'].append(
                    f"Received ${amount} from {self.current_user}")
                print("Transfer successful.")
                print("Remaining balance:", self.users[self.current_user]['balance'])
            else:
                print("Invalid amount or insufficient balance.")
        else:
            print("Receiver user ID not found.")

def main():
    atm = ATM()
    while True:
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")
        atm.authenticate_user(user_id, pin)

if __name__ == "__main__":
    main()
