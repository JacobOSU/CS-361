

class checkingAccount:
    def __init__(self, account_balance):
        self._account_balance = account_balance
        self._expenses = {}

    def get_balance(self):
        return self._account_balance

    def update_balance(self, amount):
        self._account_balance += amount

    def add_expense(self, name, cost, category):
        self._expenses[name] = cost, category
        self._account_balance -= cost

    def remove_expense(self, name):
        item_cost, category = self._expenses[name]
        del self._expenses[name]
        self._account_balance += item_cost

    def view_expenses(self):
        for item in self._expenses:
            print(item, self._expenses[item])

    def view_category_expenses(self, request_category):
        for item in self._expenses:
            cost, category = self._expenses[item]
            if category == request_category:
                print(item, self._expenses[item])

starting_balance = int(input("Hello, welcome to your own personal finance app! Please enter your current account balance to get started: "))
assure_correct = input(f"You entered {starting_balance}, are you sure that is correct? Enter Y for yes and N for no. ")
if assure_correct == 'Y':
    print(f"Okay, you're starting balance is {starting_balance}")
if assure_correct == 'N':
    starting_balance = int(input("Please enter a new amount: "))
user_account = checkingAccount(starting_balance)
print("Now that you have your account balance setup, you can add expenses to keep track of your spending.")
print("You can add an expense by entering 'add expense', you can remove expenses by entering 'remove expense',\n "
      "you can add money to your account by entering 'add paycheck', and you can view your account balance by entering"
      "'show me my balance'. Enter 'quit' to close the app.")
while True:
    user_input = input("What would you like to do? ")
    if user_input == 'add expense':
        expense_name = input("What is the name of this expense? ")
        expense_cost = int(input("How much did it cost? "))
        expense_category = input("Choose a category that you would like to group this expense with. Ex) food, entertainment, ect. ")
        user_account.add_expense(expense_name, expense_cost, expense_category)
        print("Your new expense has been added!")
    if user_input == 'show me my balance':
        print(f'Your account balance is: {user_account.get_balance()}')
    if user_input == 'remove expense':
        remove_item = input("Which item would you like to remove? ")
        assure_remove = input(f"Are you sure you want to remove the expense {remove_item}? Enter Y to remove, N to keep the expense. ")
        if assure_remove == 'Y':
            user_account.remove_expense(remove_item)
            print("Your expense has been removed and your account balance has been updated. ")
        if assure_remove == 'N':
            print("Your expense was not removed and you account balance remains unchanged.")
    if user_input == 'add paycheck':
        paycheck_amount = int(input("How much would you like to add to your existing account balance? "))
        user_account.update_balance(paycheck_amount)
        print(f"Your paycheck has been added to your account, and your new balance is {user_account.get_balance()}")
    if user_input == 'quit':
        print("Thanks for using the app!")
        break
    elif user_input != 'show me my balance' and user_input != 'add expense' and user_input != 'remove expense' and user_input != 'add paycheck' and user_input != 'quit':
        print("I'm sorry, but that is not a valid response. Please choose a valid response such as show me my balance, add expense, remove expense, add paycheck, or quit. ")




