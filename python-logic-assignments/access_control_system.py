age  = int(input("Enter your age:"))
id_card = bool(input("Do you have an ID (True/False ONLY):"))
if(age>=18):
  if(id_card != True or id_card !=False):
    id_card=bool(input("Do you have an ID (True/False ONLY):"))
    if(id_card==True):
      print("Entry Allowed")
    else:
     print("Entry Not Allowed")
else:
  print("Entry Not Allowed")