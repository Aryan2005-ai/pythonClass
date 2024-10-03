# Dictionary=it can store data in key value pair:-
# example: Name:Aryan Oberoi
# 1.ordered 2.no duplicate 3.changeable
#list identification is [] square brackets.
# dictionary identification is {} curly brackets
# set identification is {} curly brackets


# # myinfo={"name": "Aryan Oberoi",
# # #                  "email": "aryanoberoi2022@gmail.com",
# #                   "mobile": "8595717632",
#                  "age": 33}

# friendsname=["aryan","piyush","ayush"]
# friendsname.append("sam")
# 
myinfo={"name":"aryan oberoi",
        "mobile":"8595717632",
        "age":19, 
        "name":"sam"}
print(type(myinfo))
print(myinfo["mobile"])
print(myinfo["name"])
print(myinfo["age"])
print(f"my name is {myinfo["name"]} my mobile is{myinfo["mobile"]},my age is {myinfo['age']}")

#access the complete dictionary key value
for value in myinfo.values():
    print(value)

for value in myinfo.keys():
    print(value)

myinfo["name"]="piyush"
myinfo["mobile"]="8888888"
myinfo["age"]=22


#to add new field in dictionary.
myinfo.update({"gender":"male"})
#to delete key in dictionary.
myinfo.pop("name")
print(f"my mobile is{myinfo["mobile"]},my age is {myinfo['age']},my gender is {myinfo["gender"]}")

# set it can store multiple data

# unordered 
# no duplicate
# unchangaeble
      
myset={"aryan","ayush","pawan"}
print(myset)

#touple

# it can store multiple data

# mytouple=("pawan","aryan","ayush")






