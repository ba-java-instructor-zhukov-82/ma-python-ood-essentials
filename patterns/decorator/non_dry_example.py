a_cathetus = None
try:
    a_cathetus = float(input('Please, enter the cathetus:'))
except ValueError:
    a_cathetus = 1.0

b_cathetus = None
try:
    b_cathetus = float(input('Please, enter the cathetus:'))
except ValueError:
    b_cathetus = 1.0

a_cathetus_square = a_cathetus * a_cathetus
b_cathetus_square = b_cathetus * b_cathetus

hypotenuse = a_cathetus_square + b_cathetus_square

print(hypotenuse)
