try:
    age=int(input("Enter your age : "))

    if age<0:
        raise ValueError("Age can't be negetive")
    
except ValueError as error:
    print(f"Opps, invaild age: {error}")

else:
    print(f"Awesome! You are {age} years old")

finally:
    print("Program ends....")