numbers=[]

with open("numbers.txt","r") as file:
  with open("logfile.log","a") as log:
   log.write("File opened Successfully\n")
  for i in file:
    content=i.strip()
    if content:
      convert=int(content)
      numbers.append(convert)

len_of_numbers = len(numbers)
sum_of_numbers = sum(numbers)
if len_of_numbers==0:
  average_of_numbers=0
else:
  average_of_numbers=sum_of_numbers/len_of_numbers
  
  
with open("logfile.log","a") as log:
  log.write(f"Read {length_of_numbers} numbers\n")
  log.write("Computation completed\n")
  log.write(f"Sum: {sum_of_numbers}\n")
  log.write(f"Average: {average_of_numbers}\n")
  log.write("Processing completed\n\n")