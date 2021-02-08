## Connect to Database
import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.52yzh.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

students = db.students

student_list = students.find({})

#print out results from query
for doc in student_list:
	print("\n\n\t  Student ID: " + doc["student_id"] + "\n\t  First Name: " + doc["first_name"] + "\n\t  Last Name: " + doc["last_name"] + "\n")


#Update student 1007 to last name of Smith
students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})
#Update student 1008 to first name of Tony
students.update_one({"student_id": "1008"}, {"$set": {"first_name": "Tony"}})
#Update student 1009 to last name of Thompson
students.update_one({"student_id": "1009"}, {"$set": {"last_name": "Thompson"}})

## Query Data just changed
student1 = students.find_one({"student_id": "1007"})
student2 = students.find_one({"student_id": "1008"})
student3 = students.find_one({"student_id": "1009"})

#Print in nice format
print("\n\t  Student ID: " + student1["student_id"] + "\n\t  First Name: " + student1["first_name"] + "\n\t  Last Name: " + student1["last_name"] + "\n")
print("\n\t  Student ID: " + student2["student_id"] + "\n\t  First Name: " + student2["first_name"] + "\n\t  Last Name: " + student2["last_name"] + "\n")
print("\n\t  Student ID: " + student3["student_id"] + "\n\t  First Name: " + student3["first_name"] + "\n\t  Last Name: " + student3["last_name"] + "\n")

