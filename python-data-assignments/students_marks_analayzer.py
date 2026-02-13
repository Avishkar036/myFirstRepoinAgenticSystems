marks=[78,85,90,65,71,88,92,80]
first_three=marks[:3]
last_three=marks[5:]
highest=max(marks)
lowest=min(marks)
average=sum(marks)/len(marks)
print(f"First 3 marks: {first_three}")
print(f"Last 3 marks: {last_three}")
print(f"Highest:{highest}")
print(f"Lowest:{lowest}")
print(f"Average: {average}")