import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time


ref = db.reference('Students')

data = {
    "8632136385":{
        "name" : "Dung",
        "studentID" : "1TE251215R",
        "major" : "EECS",
        "year" : 4,
        "total_attendance" : 12,
        "standing" : "A"
    }
}

for key, val in data.items():
    ref.child(key).set(val)