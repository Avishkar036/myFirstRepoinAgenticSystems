def even_odd(n):
  if(n%2==0):
    return f"Even"
  else:
    return f"Odd"

def main():
  num=int(input("Enter thr number:"))
  result=even_odd(num)
  print(f"Number is {result}")

main()