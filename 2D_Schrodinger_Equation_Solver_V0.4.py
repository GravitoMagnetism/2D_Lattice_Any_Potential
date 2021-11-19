from Coordinate_Index_Conversion_Functions import Coordinate_To_Index
from Coordinate_Index_Conversion_Functions import Index_To_Coordinate
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import scipy.linalg as la

def Laplacian(x_max,y_max):
    I_max=x_max*y_max
    Lap=[[0]*I_max]*I_max
    array=[]
    for i in range(I_max):
        row=[]
        for j in range(I_max):
            if j==i:
                Lap[i][j]=-4
            elif j==i+1 and j<=I_max:
                Lap[i][j]=1
            elif j==i-1 and j>=0:
                Lap[i][j]=1
            elif j==i+y_max and j<=I_max:
                Lap[i][j]=1
            elif j==i-y_max and j>=0:
                Lap[i][j]=1
            else:
                Lap[i][j]=0
            row.append(Lap[i][j])
        array.append(row)
    return array


def Generate_Potential(x_max,y_max,a):
    I_max=x_max*y_max
    V=[[0]*I_max]*I_max
    array=[]
    for i in range(I_max):
        row=[]
        x=a*Index_To_Coordinate(i,y_max)[0]
        y=a*Index_To_Coordinate(i,y_max)[1]
        for j in range(I_max):
            if i==j:
                V[i][j]=0
            else:
                V[i][j]=0
            row.append(V[i][j])
        array.append(row)
    return array

def Hamiltonian(Laplacian,V,x_max,y_max,a):
    I_max=x_max*y_max
    H=[]
    for i in range(I_max):
        row=[]
        for j in range(I_max):
            col=0
            col=(a*Laplacian[i][j])+V[i][j]
            row.append(col)
        H.append(row)
    return H
                
def Matrixify(prob,x_max,y_max):
    prob_matrix=[]
    for i in range(x_max):
        prob_row=[]
        for j in range(y_max):
            prob_row.append(prob[Coordinate_To_Index(i,j,y_max)])
        prob_matrix.append(prob_row)
    return prob_matrix

a=1
Width=64
Height=64
eigenfunction=1

Lap=Laplacian(Width,Height)
Pot=Generate_Potential(Width,Height,a)
Ham=Hamiltonian(Lap,Pot,Width,Height,a)
#print(np.matrix(Lap))
#print(Pot)
#print(Ham)

eigenvalues, eigenvectors = la.eig(Ham)
func=eigenvectors[:,0]
prob_line=[]
for i in range(len(func)):
    prob_line.append(abs(func[i])**2)

prob=Matrixify(prob_line,Width,Height)
#print(np.matrix(prob))

print("The number of valid eigenfunctions in this system is", len(prob_line))
#print(prob)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
#ax = Axes3D(fig)
x=np.arange(0, Width, 1)
y=np.arange(0, Height, 1)
X, Y = np.meshgrid(x, y)
Z=np.matrix(prob[eigenfunction])
#print(Z)
#zs = np.array(prob[0])
#Z = zs.reshape(X.shape)

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
#ax.plot_surface(X, Y, Z)
#ax.set_zlim(0, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Probability Density')
ax.zaxis.set_major_formatter('{x:.02f}')
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

print('Beep! The particle has been simulated!')