print("===== celsius_to_fahrenheit =====")
def converter(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
    
print(converter(0))
print(converter(25))
print(converter(100))

print("===== celsius_to_fahrenheit with *args =====")
def converter(*celsius):
    fahrenheit = []
    for n in celsius:
        calculation = (n * 9/5) + 32
        fahrenheit.append(calculation)
    return fahrenheit
    
print(converter(0, 25, 100))  

print("===== celsius_to_fahrenheit with *args and f string =====")
def converter(*celsius):
    fahrenheit = []
    for n in celsius:
        calculation = (n * 9/5) + 32
        fahrenheit.append(calculation)
        print(f"{n} celsius is {calculation} fahrenheit")
    return fahrenheit

print(converter(0, 25, 100))   
 
print("=============Discount calculator with default================")
def apply_discount(price, discount_percent=10):
    discount_amount = price * discount_percent/100
    final_price = price - discount_amount
    return final_price

print(apply_discount(150))
print(apply_discount(150,20))