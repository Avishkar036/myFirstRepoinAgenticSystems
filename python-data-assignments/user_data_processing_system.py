def calculate_average(scores):
  total=0
  for score in scores:
    total+=score
  average=total/len(scores)
  return average

def is_admin(roles):
  return "admin" in roles

def  main():
  users=[
  {
    "name":"A",
    "score":[70,69,65],
    "role":{"admin","editor"}
  },
  {
    "name":"B",
    "score":[89,90,99],
    "role":{"viewer"}
  },
  {
    "name":"C",
    "score":[70,78,80],
    "role":{"editor"}
  }
]
  
  for user in users:
    name=user["name"]
    score=user["score"]
    role=user["role"]
    
    avg_score=calculate_average(score)
    admin_acc=is_admin(role)
    
    print(f"Name: {name}")
    print(f"Average Score:{avg_score}")
    print(f"Admin Access:{admin_acc}")
    
main()