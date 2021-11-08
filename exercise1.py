print("Welcome in Luigi's store.")

product_name = input("product name: ")
product_price = float(input("product price net: "))
client_email = input("client email: ")
client_phone = int(input("client phone: "))

product_price = float(product_price)
tax = 0.23
product_gross = (product_price * tax) + product_price

print("Your basket: ")
print(product_name, product_price, product_gross, client_email, client_phone)

try:
    product_name = input("product name: ")
    product_price = float(input("product price net: "))
    client_email = input("client email: ")
    client_phone = int(input("client phone: "))
    product_gross = (product_price * tax) + product_price
    print("Your basket: ")
    print("product_name", "product_gross", "client_email", "client_phone")
    print(product_name, product_price, product_gross, client_email, client_phone)
except:
    print("Process interrupted. Bad data type.")
    exit()



