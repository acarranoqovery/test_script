import json

print ("Hello World - JOB")

output = {
    "db_password": {
    "sensitive": True,
    "value": "notasecurepassword"
  },
  "db_username": {
    "sensitive": False,
    "value": "admin2"
  },
  "db_host": {
    "sensitive": False,
    "value": "mydbhostname"
  }
}

print("My output:")
print (output)

with open("/qovery-output/qovery-output.json", "w") as outfile:
    json.dump(output, outfile)
