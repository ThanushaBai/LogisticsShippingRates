#shipping cost calculator

##input package weight and shipping rate
weight = float(input("enter the package weight in kilogram: "))
rate = float(input("enter the shipping rate per kilogram: "))

##calculate shipping cost
shipping_cost = weight * rate

##display the result
print(f"shipping cost: {shipping_cost} USD")
