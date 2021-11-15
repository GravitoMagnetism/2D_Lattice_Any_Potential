from Coordinate_Index_Conversion_Functions import Coordinate_To_Index
from Coordinate_Index_Conversion_Functions import Index_To_Coordinate

def Grad_Squared(psi,x_max,y_max):
    Grad_Squared_out=[]
    for i in range(x_max*y_max):
        x=Index_To_Coordinate(i,y_max)[0]
        y=Index_To_Coordinate(i,y_max)[1]
        if x==0:
            if y==0:
                Grad_Squared_out[i]=(psi[Coordinate_To_Index(x+1,y,y_max)]-(2*psi[Coordinate_To_Index(x,y,y_max)]))+(psi[Coordinate_To_Index(x,y+1,y_max)]-(2*psi[Coordinate_To_Index(x,y,y_max)]))
            elif y==y_max:
                Grad_Squared_out[i]=(psi[Coordinate_To_Index(x+1,y,y_max)]-(2*psi[Coordinate_To_Index(x,y,y_max)]))+(-(2*psi[Coordinate_To_Index(x,y,y_max)])+psi[Coordinate_To_Index(x,y-1,y_max)])
            else:
                Grad_Squared_out[i]=(psi[Coordinate_To_Index(x+1,y,y_max)]-(2*psi[Coordinate_To_Index(x,y,y_max)]))+(psi[Coordinate_To_Index(x,y+1,y_max)]-(2*psi[Coordinate_To_Index(x,y,y_max)])+psi[Coordinate_To_Index(x,y-1,y_max)])
        elif x==x_max:
            if y==0:
                Grad_Squared_out[i]=(-(2*psi[Coordinate_To_Index(x,y,y_max)])+psi[Coordinate_To_Index(x-1,y,y_max)])+(psi[Coordinate_To_Index(x,y+1,y_max)]-(2*psi[Coordinate_To_Index(x,y,y_max)]))
            elif y==y_max:
                Grad_Squared_out[i]=(-(2*psi[Coordinate_To_Index(x,y,y_max)])+psi[Coordinate_To_Index(x-1,y,y_max)])+(-(2*psi[Coordinate_To_Index(x,y,y_max)])+psi[Coordinate_To_Index(x,y-1,y_max)])
            else:
                Grad_Squared_out[i]=(-(2*psi[Coordinate_To_Index(x,y,y_max)])+psi[Coordinate_To_Index(x-1,y,y_max)])+(psi[Coordinate_To_Index(x,y+1,y_max)]-(2*psi[Coordinate_To_Index(x,y,y_max)])+psi[Coordinate_To_Index(x,y-1,y_max)])
        else:
            if y==0:
                Grad_Squared_out[i]=(psi[Coordinate_To_Index(x+1,y,y_max)]-(2*psi[Coordinate_To_Index(x,y,y_max)])+psi[Coordinate_To_Index(x-1,y,y_max)])+(psi[Coordinate_To_Index(x,y+1,y_max)]-(2*psi[Coordinate_To_Index(x,y,y_max)]))
            elif y==y_max:
                Grad_Squared_out[i]=(psi[Coordinate_To_Index(x+1,y,y_max)]-(2*psi[Coordinate_To_Index(x,y,y_max)])+psi[Coordinate_To_Index(x-1,y,y_max)])+(-(2*psi[Coordinate_To_Index(x,y,y_max)])+psi[Coordinate_To_Index(x,y-1,y_max)])
            else:
                Grad_Squared_out[i]=(psi[Coordinate_To_Index(x+1,y,y_max)]-(2*psi[Coordinate_To_Index(x,y,y_max)])+psi[Coordinate_To_Index(x-1,y,y_max)])+(psi[Coordinate_To_Index(x,y+1,y_max)]-(2*psi[Coordinate_To_Index(x,y,y_max)])+psi[Coordinate_To_Index(x,y-1,y_max)])
    return Grad_Squared_out

def Test_Grad_Squared(m,x,y):
    Grad_Squared_M=Grad_Squared(m,x,y)
    return Grad_Squared_M

m=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
x=5
y=5
print(Test_Grad_Squared(m,x,y))