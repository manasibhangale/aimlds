### Assignment 4: Generator Expression

#Create a generator expression that generates the squares of numbers from 1 to 10. Iterate over the generator and print each value.
squares = (x * x for x in range(1, 11))

# Test
for square in squares:
     print(square)