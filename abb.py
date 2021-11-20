class Square:
    xyz = 0
    
    def __init__(self, some):
        self.xyz += some

square = Square(10)
print(square.xyz)

square1 = Square(5)
print(square1.xyz)


class Square:
    square_list = []
    
    def __init__(self, some):
        self.square_list.append(some)

square = Square(10)
print(square.square_list)

square1 = Square(5)
print(square1.square_list)