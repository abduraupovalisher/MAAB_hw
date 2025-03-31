import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Basic Plotting
x = np.linspace(-10, 10, 100)
y = x**2 - 4*x + 4
plt.figure()
plt.plot(x, y, label='$f(x) = x^2 - 4x + 4$', color='b')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Quadratic Function')
plt.legend()
plt.grid()
plt.show()

# 2. Sine and Cosine Plot
x = np.linspace(0, 2*np.pi, 100)
plt.figure()
plt.plot(x, np.sin(x), label='sin(x)', linestyle='-', color='r')
plt.plot(x, np.cos(x), label='cos(x)', linestyle='--', color='b')
plt.xlabel('x')
plt.ylabel('Function value')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.grid()
plt.show()

# 3. Subplots
x = np.linspace(-2, 2, 100)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].plot(x, x**3, 'r')
axs[0, 0].set_title('f(x) = x^3')
axs[0, 1].plot(x, np.sin(x), 'g')
axs[0, 1].set_title('f(x) = sin(x)')
axs[1, 0].plot(x, np.exp(x), 'b')
axs[1, 0].set_title('f(x) = e^x')
x_pos = np.linspace(0, 2, 100)
axs[1, 1].plot(x_pos, np.log(x_pos + 1), 'm')
axs[1, 1].set_title('f(x) = log(x+1)')
plt.tight_layout()
plt.show()

# 4. Scatter Plot
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
plt.figure()
plt.scatter(x, y, c='purple', marker='o', alpha=0.6)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Random Scatter Plot')
plt.grid()
plt.show()

# 5. Histogram
data = np.random.normal(0, 1, 1000)
plt.figure()
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normally Distributed Data')
plt.show()

# 6. 3D Plotting
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
plt.colorbar(surf)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Surface Plot: cos(x^2 + y^2)')
plt.show()

# 7. Bar Chart
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
plt.figure()
plt.bar(products, sales, color=['red', 'blue', 'green', 'purple', 'orange'])
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales of Different Products')
plt.show()

# 8. Stacked Bar Chart
time_periods = ['T1', 'T2', 'T3', 'T4']
category_A = [10, 15, 20, 25]
category_B = [5, 10, 15, 20]
category_C = [8, 12, 18, 22]
plt.figure()
plt.bar(time_periods, category_A, label='Category A', color='red')
plt.bar(time_periods, category_B, bottom=category_A, label='Category B', color='blue')
plt.bar(time_periods, category_C, bottom=np.array(category_A) + np.array(category_B), label='Category C', color='green')
plt.xlabel('Time Periods')
plt.ylabel('Values')
plt.title('Stacked Bar Chart')
plt.legend()
plt.show()
