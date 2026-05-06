#E-commerce Delivery
#Filter only pending orders

orders = ["delivered", "pending", "shipped", "pending", "delivered"]
pending = list(filter(lambda o: o == "pending", orders))
print(pending)