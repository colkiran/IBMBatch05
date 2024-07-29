

def outerFun(fnc):

    def helper(amt):
        print("Logging into the Account ......")
        fnc(amt)
        print("Logged out of the Account......")
        print("-" * 60)

    return helper


@outerFun            # deposit = outerFun(deposit)
def deposit(amt):
    print(f"Amount {amt} credited into the account ending XXXX")

@outerFun
def withdraw(amt):
    print(f"Amount {amt} debited from the account ending XXXX")



deposit(85000)

withdraw(45000)
