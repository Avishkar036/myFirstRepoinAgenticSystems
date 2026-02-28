import json

response='''
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''

parsed_data=json.loads(response)

request_id=parsed_data["id"]
status=parsed_data["status"]
text=parsed_data["result"]["text"]
confidence=parsed_data["result"]["confidence"]

print(f"Request ID:{request_id}")
print(f"Status:{status}")
print(f"Text: {text}")
print(f"Confidence:{confidence}")
if confidence<0.9:
  print(f"Warning")
  
follow_up={
  "request_id":request_id,
  "Status":status,
  "Resopnse":"Process Successfull"
  }

json_output=json.dumps(follow_up, indent=4)  
with open(r"E:\Agentic AI Material\Module 1\myFirstRepoinAgenticSystems\python-json-assignment\response.json","w") as f:
  f.write(json_output)

