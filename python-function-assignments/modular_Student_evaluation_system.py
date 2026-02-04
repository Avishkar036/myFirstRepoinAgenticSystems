def greet(n):
  return f"Hello, {n}"

def num_and_average(m):
  length=len(m)
  total=0
  for i in m:
    total+=i
  average=total/length
  return length, average

def pass_fail(avge):
  if(avge>=50):
    return f"Pass"
  else:
    return f"Fail"

def main():
 name=greet(input("Enter your name:"))
 marks=[75,90,81]
 subjects,average_score=num_and_average(marks)
 result=pass_fail(average_score)
 print(name)
 print(f"Subjects: {subjects}")
 print(f"Average Score: {average_score}")
 print(f"Result:{result}")

main()