# balance = 0, owner, accountnumber(unique, autoincrement)
# deposit(), withdraw()
class BankAccount():
    latest_id = 0

    def __init__(self,owner):
        self.__balance = 0 # private or public?
        self.__owner = owner
        BankAccount.latest_id += 1
        self.accountnumner = BankAccount.latest_id
        print(f"created a bank account for {self.owner} with accountNumber {self.accountnumner}")

    def deposit(self, amount):
        self.__balance += amount

    @property # this allows us to call abraham.balance as if it was a variable
    def balance(self): # this is a public function
        print("inside balance function")
        return self.__balance # returns balance
    
    @property 
    def owner(self):
        print("inside owner function")
        return f'Owner is {self.__owner}' # returns owner
        

abraham = BankAccount("Abraham")
yajnee = BankAccount("Yajnee")
abraham.deposit(3000)
# abraham.balance
print(abraham.balance)
print(abraham.owner)