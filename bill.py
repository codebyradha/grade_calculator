#restuarnt bill calculation
#using lambda function
prices=[100,200,300]
bill=list(map(lambda x:x*1.18,prices))
print(bill)



#using normal function
def add_gst(price):
    return price*1.18
prices=[100,200,300]
bill=list(map(add_gst,prices))
print(bill)