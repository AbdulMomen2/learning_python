def calculate_area(base, height, shape='triangle'):
    if shape == 'triangle':
        area = (1/2) * base * height
    elif shape == 'rectangle':
        area = base * height
    else:
        area = None
    return area

print(calculate_area(3, 2))  

def print_pattern(num = 5):
    for i in range(num):
        s = ''
        for j in range(i+1):
            s = s + '*'
        print(s)
print("for defult shape 5") 
print_pattern() 
print("for shape 3") 
print_pattern(3)
print("for shape 4") 
print_pattern(4)
