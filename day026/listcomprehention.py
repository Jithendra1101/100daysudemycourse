

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

## list comprehension

square_numbers = [ n*n for n in numbers]
print(square_numbers)

#with is condition 
even_numbbers_square = [ n*n for n in numbers if n%2 == 0]
print(even_numbbers_square)
odd_numbbers_square = [ n*n for n in numbers if n%2 != 0]
print(odd_numbbers_square)