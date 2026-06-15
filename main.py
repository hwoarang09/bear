from enum import Enum

class State(Enum):
    IDLE      = "idle"
    PIN       = "pin"
    ACCOUNT   = "account"
    MONEY_JOB = "money_job"

class ATM_Error():
    pass

class Bank():
    def __init__(self):
        self.card_pins     = {"card1" : "pin1"}
        self.card_accounts = {"card1" : ("acc1", "acc2")}
        self.balances = {"acc1" : 100, "acc2" : 253}
 
    def validate_pin(self, card_id, pin)->bool:
        if card_id in self._card_pins:
            if self._card_pins[card_id] == pin:
                return True
            else:
                return False
        else:
            return False
        
    def get_accounts(self, card_id)->list[str]:
        return self.card_accounts[card_id]
    
    def get_balance(self, account_id)->int:
        return self.balances[account_id]
    def withdraw(self, account_id, amount)->bool:
        self.balances[account_id] -= amount
    def deposit(self, account_id, amount):
        self.balances[account_id] += amount

class CashBin:
    def __init__(self, money=10000):
        self.money = money
    
    def withdraw(self, amount):
        self.money -= amount

    def show_current_money(self):
        return self.money
    
class ATM():
    def __init__(self, bank, cash_bin):
        self.bank        = bank
        self.cash_bin    = cash_bin
        self.state       = State.IDLE
        self.card_id     = None
        self.accounts    = []
        self.cur_account = None

    def insert_card(self, card_id):
        return 
    
    def check_pin(self, pin):
        return

    def get_accounts():
        return

    def withdraw():
        return
    
    def deposit():
        return
    
    def out_card():
        return
    
if __name__ == "__main__":
    atm = ATM(Bank(), CashBin())
    print("atm created")

    atm.insert_card("card1")
    print('card1 inserted')

    atm.check_pin("pin0")
    print("wrong pin")

    atm.check_pin("pin1")
    print("check success")