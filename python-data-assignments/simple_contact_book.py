contact_book={"Ravi":6598743215,
              "Anita":5369741289,
              "Rakesh":5964123574}
choice=int(input("Choose your Choice: \n1.Print Contact Book \n2.Search a Contact \n ENter an option:"))
if(choice==1):
  print(contact_book)
elif(choice==2):
  sname=input("ENter a Name to Search:")
  if sname in contact_book:
      print(f"{contact_book[sname]}")
  else:
      print("Contact Not Found")
else:
  print("Inavlid Choice")