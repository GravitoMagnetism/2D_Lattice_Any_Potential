

def Coordinate_To_Index(x,y,n_y):
    I=(x*n_y)+y
    return int(I)

def Index_To_Coordinate(I,n_y):
    y=I%n_y
    x=(I-y)/n_y
    return [int(x),int(y)]

def Test_System(n_x,n_y):
    for i in range(n_x*n_y):
        if i!=Coordinate_To_Index(Index_To_Coordinate(i,n_y)[0],Index_To_Coordinate(i,n_y)[1],n_y):
            print(i, "'Doesn't work', in the timeless words of Paul.")
            return False
            break
    return True

n_x=10
n_y=10
if Test_System(n_x,n_y)==True:
    print("For an array of this size, this code works!")
else:
    print("For an array of this size, this code does not work, but you probably already figured that out.")