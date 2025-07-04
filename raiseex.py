class InsufficientBalErr(Exception):
    def __init__(self, msg):
        super()
        self.msg = msg
    def withdrawl_amount():
        acc_bal=5000
        amount = int(input("Enter the amount to withdraw: "))
        try:    
            if acc_bal < amount:
                raise InsufficientBalErr("Insufficient balance to withdraw the requested amount.")
            else:
                print("enjoy")
        except InsufficientBalErr as e:
            print(e.msg)
        print("plz follow the rules")

    withdrawl_amount()

  