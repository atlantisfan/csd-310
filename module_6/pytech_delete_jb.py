## Justin Brehms
## CSD310
## Module 6.3
## Deleting rows

## Connect to Database
import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.52yzh.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

students = db.students

student_list = students.find({})

#print out results from query
print("\n  -- DISPLAYING STUDENTS from PYTECH -- ")
for doc in student_list:
	print("\n\n  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")


john = {
	"student_id": "1010",
	"first_name": "John",
	"last_name": "Doe",
	"enrollment": "Active"
		}
john_student_id = students.insert_one(john).inserted_id
print("\n  -- Inserted Record for John Doe -- ")

print("\n  -- RE-DISPLAYING STUDENTS from PYTECH after Insertion-- ")
## Reprint queried information to show changes
student_list = students.find({})
for doc in student_list:
	print("\n\n  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#Delete student John from records
removeStudent = students.delete_one({"student_id": "1010"})

#Requery list
print("\n  -- RE-DISPLAYING STUDENTS from PYTECH after Deletion -- ")
student_list = students.find({})
for doc in student_list:
	print("\n\n  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
