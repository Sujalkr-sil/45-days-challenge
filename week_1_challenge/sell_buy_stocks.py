prices=[7,6,4,3,2,1]
min_price=prices[0]
max_price=0
for i in range(1,len(prices)):
    if prices[i]<min_price:
        min_price=prices[i]
        start_index=i
for i in range(start_index,len(prices)):
    if max_price<prices[i]:
        max_price=prices[i]
print(max_price-min_price)
