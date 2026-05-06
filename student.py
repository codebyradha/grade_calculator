#select passed student
#using lambda 
marks=[20,45,67,30,89]
passed=list(filter(lambda m:m>=35,marks))
print(passed)

#using normal function
def is_pass(marks):
    return marks>=35
marks=[20,45,67,30,89]
passed=list(filter(is_pass,marks))
print(passed)