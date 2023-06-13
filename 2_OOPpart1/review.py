# List
new_list = [10,20,20,30,40,40,40]
# Dict left is key, right is value
new_dict = {"key": 10}
print(new_dict["key"])
# Set
new_set = {10 ,20 ,30}
list_to_set = set(new_list)
print(list_to_set)
# Using range()
for i in range(5):
    # print(i)
    pass
# Using type()
if type(new_list) is list and type(new_dict) is dict:
    print("It is a list")
# Comparing type, using and,is, or
# Listifying strings
string = "hello"
print(list(string))
# Raise an error (raise https://docs.python.org/3/library/exceptions.html)
if type(new_dict) is not list:
    raise Exception("Error!")