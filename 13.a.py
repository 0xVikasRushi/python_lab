prices ={'APPLE': 45.23,
         'ORANGE': 612.78,
         'MANGO': 205.55,
         'BLUEBERRY': 37.20,
         'STRAWBERRY': 10.75}
# similar to hashmap in java
max_key = max(prices, key=prices.get)

print(max_key)