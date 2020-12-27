# Sibel Akayoğlu
# HW2 - USER ID PROGRAM

user_info=[]
user_info.append(input("First Name : "))
user_info.append(input("Last Name : "))
user_info.append(input("Age : "))
user_info.append(input("Birth Date (Year) : "))


print("\nPersonal Informations\n")
for x in user_info:
    print(x)

if int(user_info[2]) <= 18:
    print("\nYou cannot go out bcoz its too dangerous")
elif int(user_info[2]) > 18:
    print("\nYou can go out to the street.")
