# Type-casting = Process of converting one data type into another data type
# str(), int(), float(), bool() 

name = "kush"
age = 20
height = 5.9
is_student = True

print(type(height))  # Output: <class 'float'>

# Type-casting examples
# 1. Converting float to int

float = int(height)  # Converting float to int
print (float) 
print(type(float))  # Output: <class 'int'>

# 2. COnverting int to string

age = str(age)  # Converting int to string
print(age)
print(type(age))  # Output: <class 'str'>

# 3. Converting string to boolean

name = bool(name)
print(name)
print(type(name))

