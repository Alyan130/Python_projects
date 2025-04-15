import os
import json

DB_FILE = "data.json"

def load_data():
  if os.path.exists(DB_FILE):
    with open(DB_FILE,"r") as file:
      return json.load(file)
  return {}


def save_data(data):
  with open(DB_FILE,"w") as file:
    json.dump(data,file,indent=4)

