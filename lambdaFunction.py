# SYNTAX ---> lambda arguments: expression

# EXAMPLE 1
add = lambda x, y : x + y
result = add(3,5)
print(result)

# EXAMPLE 2
points = [(5,2),(3,1),(4,3),(8,5)]
sorted_points = sorted(points, key=lambda point:point[1])
print(sorted_points)

# EXAMPLE 3 
numbers = [1, 2, 3, 4]
square = list(map(lambda x: x**2,numbers))
print(square)