#  Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'thar', 'maruti']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'Subaru','Bcmw', 'Iaudi', 'HHtoyota', 'ubaru']
cars.sort()
print(cars)   #['Bcmw', 'HHtoyota', 'Iaudi', 'Subaru', 'audi', 'bmw', 'toyota', 'ubaru']

#  Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)