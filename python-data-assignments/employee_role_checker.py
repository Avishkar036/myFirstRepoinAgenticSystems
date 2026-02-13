emp=("101","Ravi","IT")
roles={"admin","editor","viewer"}
print(f"Employee Information:\n ID:{emp(0)}\n Name:{emp(1)}\n Deaprtment:{emp(2)}")
if "admin" in roles:
  print("Admin Access: Yes")
else:
  print("Admin Access: No")
