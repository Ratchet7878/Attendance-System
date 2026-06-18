from firebase_admin import credentials
from firebase_admin import db


ref = db.reference('Students')

data = {
    "8632136385":{
        "name" : "Test",
        "studentID" : "1TE251215R"
    }
}