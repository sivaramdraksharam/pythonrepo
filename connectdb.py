from pymongo import MongoClient
from datetime import datetime
#1.establish connection to mongodb
client = MongoClient("mongodb://localhost:27017")
#2. Access the database
db = client["user_management"]
#3.access user collection
users_collection = db["users"]
#4. verify by printing the database name
print("Connected to database:",db.name)

#create
def register_user(name,email,age):
    user_document = {
        "name" : name,
        "email" : email,
        "age" : age,
        "registration_date" : datetime.now() 
    }
    
    #insert one doc into users collection
    user_id = users_collection.insert_one(user_document).inserted_id
    
    print("User registered with ID:",user_id)

#read
def get_user_by_email(email):
    user = users_collection.find_one({"email":email})
    if user:
        print("User found",user)
    else:
        print("User not found!")

#get all users
def get_all_users():
    users = users_collection.find()
    for user in users:
        print(user)

#call functions
#register_user("shivaram","shivaram786@gmail.com",50)
get_user_by_email("shivaram786@gmail.com")

#update
def update_user_age(email,new_age):
    result = users_collection.update_one(
        {"email": email},
        {"$set" : {"age": new_age}}
    )
    if result.modified_count > 0:
        print("User's age updated successfully")
    else:
        print("User not found or age is the same!")

#call update
update_user_age("shivaram786@gmail.com",48)
             
#delete
def delete_user_by_email(email):
    result = users_collection.delete_one({"email":email})
    if result.deleted_count > 0:
        print("User deleted successfully")
    else:
        print("User not found!")
delete_user_by_email("rahul123@gmail.com")


