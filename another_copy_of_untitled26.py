# -*- coding: utf-8 -*-
"""Another copy of Untitled26.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pom5_nbpGryZznYCEkN3vyBsa4ujeZez

1.
In this Queation we have given that the size of the metrix is (n,k)and (k,m)        

So, if we do the multiplication of this metrix so ve got the resulten metrix of size(n,m)                                 


for that matrix,

To multiply a
(𝑛,𝑘) matrix 𝐴 with a (𝑘,𝑚) matrix B, the total number of operations required are:

          Multiplications: n×m×k
          Additions:    n×m×(k−1)
"""

#2
import time
def matrix_multiply_lists(A,B):
  n=len(A)
  k=len(A[0])
  m=len(B[0])

  C=[[0]*m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      C[i][j]=sum(A[i][l] * B[l][j] for l in range(k))
  return C
A=[
      [1,2,3],
      [4,5,6]
  ]
B=[[7,8],
   [9,10],
   [11,12]]

start_time=time.time()
C_list=matrix_multiply_lists(A, B)
end_time=time.time()
print("Matrix C (list of lists):",C_list)
print("Time using list of lists:", end_time -start_time)

#3
import numpy as np
A_np=np.array([
    [1,2,3],
    [4,5,6]
               ])
B_np= np.array([
    [7,8],
    [9,10],
    [11,12]
                ])
start_time=time.time()
C_np=np.dot(A_np,B_np)
end_time=time.time()
print("Matrix C (NumPy):")
print(C_np)
print("Time using Numpy:",end_time-start_time)

#5
import jax
import jax.numpy as jnp
import numpy as np

def calss(x, y):
    return (x**2 * y) + (y**3 * jnp.sin(x))

def find_gradient(x, y):
    df_dx = 2 * x * y + y**3 * jnp.cos(x)
    df_dy = x**2 + 3 * y**2 * jnp.sin(x)
    return df_dx, df_dy

def jax_function(x, y):
    return calss(x, y)

grad_function = jax.grad(jax_function, (0, 1))

x_val = np.random.uniform(-10, 10)
y_val = np.random.uniform(-10, 10)

analytical_grad_x, analytical_grad_y = find_gradient(x_val, y_val)

jax_grad = grad_function(x_val, y_val)

print(f"Random x value: {x_val}")
print(f"Random y value: {y_val}")
print(f"Analytical Gradient: (dx: {analytical_grad_x}, dy: {analytical_grad_y})")
print(f"JAX Gradient: (dx: {jax_grad[0]}, dy: {jax_grad[1]})")

print(f"Gradients match: {np.allclose(analytical_grad_x, jax_grad[0]) and np.allclose(analytical_grad_y, jax_grad[1])}")

#6
import sympy as sp
import jax
import jax.numpy as jnp
import numpy as np

x, y = sp.symbols('x y')
f_sympy = x**2 + y**2

grad_f_sympy = [sp.diff(f_sympy, var) for var in (x, y)]
grad_f_sympy

def f(x, y):
    return x**2 + y**2

grad_f_jax = jax.grad(lambda xy: f(xy[0], xy[1]))

def analytical_grad_f_sympy(x_val, y_val):
    grad = [g.subs({x: x_val, y: y_val}) for g in grad_f_sympy]
    return np.array(grad, dtype=float)

random_values = np.random.rand(3, 2)

for xy in random_values:
    x_val, y_val = xy
    grad_jax = grad_f_jax(jnp.array([x_val, y_val]))
    grad_sympy = analytical_grad_f_sympy(x_val, y_val)
    print(f"Random values: x = {x_val}, y = {y_val}")
    print(f"JAX Gradient: {grad_jax}")
    print(f"SymPy Analytical Gradient: {grad_sympy}\n")

#7
registration = {
    '1.2022': {
        '1.Branch 1': [
            {
                'Roll Number': 1,
                'Name': 'N',
                'Marks': {
                    '1.Maths': 100,
                    '2.English': 70
                }
            }
        ],
        '2.Branch 2': {}
    },
    '2.2023': {
        '1.Branch 1': {},
        '2.Branch 2': {}
    },
    '3.2024': {
        '1.Branch 1': {},
        '2.Branch 2': {}
    },
    '4.2025': {
        '1.Branch 1': {},
        '2.Branch 2': {}
    }
}

print(registration)

#9

import matplotlib.pyplot as plt
import numpy as np
#1.
x = np.arange(0.5, 100.0, 0.5)
y = x

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph')
plt.show()

#2
y1= x**2
plt.plot(x,y1)
plt.show()

#3
y2=(x**30)/100
plt.plot(x,y2)
plt.show()

#4
y3=np.sin(x)
plt.plot(x,y3)
plt.show()

#5
y3=np.sin(x)/x
plt.plot(x,y3)
plt.show()

#6
y4=np.log(x)
plt.plot(x,y4)
plt.show()

#7
y5=np.exp(x)
plt.plot(x,y5)
plt.show

#10
import numpy as np
import pandas as pd

matrix = np.random.uniform(1, 2, size=(20, 5))
df = pd.DataFrame(matrix, columns=['a', 'b', 'c', 'd', 'e'])
column_with_highest_std = df.std().idxmax()
row_with_lowest_mean = df.mean(axis=1).idxmin()

print("DataFrame:")
print(df)
print("\nColumn with the highest standard deviation:", column_with_highest_std)
print("Row with the lowest mean:\n", df.loc[row_with_lowest_mean])

#11
df['f']=df.sum(axis=1)
# print("DataFrame with new column 'f':\n", df)
df['g']=df['f'].apply(lambda x: 'LT8' if x<8 else 'GT8')
# print("Dataframe with new column'g':\n",df)
lt8_count=df[df['g']== 'LT8'].shape[0]
print("Number of rows where the value in column 'g' is 'LT8':",lt8_count)
stanterd_deviation1=df[df['g']=='LT8']['f'].std()
standerd_deviation2=df[df['g']=='GT8']['f'].std()
print("Standerd deviation of column 'f' where 'g' is 'LT8':", stanterd_deviation1)
print("Standerd deviation of column 'f' where 'g' is 'GT8';", standerd_deviation2)

#12
import numpy as np

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

vector = np.array([1, 0, 1, 0])
result = matrix + vector

print("Matrix:")
print(matrix)
print("\nVector:")
print(vector)
print("\nResult of broadcasting addition:")
print(result)

