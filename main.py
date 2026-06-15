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


if __name__ == "__main__":
    print('bear test')