balance = int(input("Balance: "))
withdrwal = int(input("Withdral: "))
verification = bool(input("Verified: "))
if(verification == "True" and withdrwal<=balance):
     print("Withdrawal Successful")  
else:
  print("Transaction Denied")