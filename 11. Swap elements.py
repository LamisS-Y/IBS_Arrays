# - Create a variable named `orders`
#   with the following content: `["first", "second", "third"]`
# - Swap the first and the third element of `orders`

orders = ["first", "second", "third"]
temp = orders [0] # we need to save what the first element was before switchin it to keep the information stored.
orders [0] = orders [2]
orders [2] = temp
print(orders)
