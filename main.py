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
        self._card_pins     = {"card1" : "pin1"}
        self._card_accounts = {"card1" : ("acc1", "acc2")}
        self._balances = {"acc1" : 100, "acc2" : 253}
 
    def validate_pin(self, card_id, pin)->bool:
        if card_id in self._card_pins:
            if self._card_pins[card_id] == pin:
                return True
            else:
                return False
        else:
            return False
        
    def get_accounts(self, card_id)->list[str]:
        return
    def get_balance(self, account_id)->int:
        return
    def withdraw(self, account_id)->bool:
        return
    def deposit(self, account_id)->bool:
        return

class ATM():
    def __init__(self, bank, bin):
        self.bank        = bank
        self.bin         = bin
        self.state       = State.IDLE
        self.card_id     = None
        self.accounts    = []
        self.cur_account = None

    def insert_card():
        return 
    
    def check_pin():
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
    print('bear test')