import numpy as np
from PIL import Image

# Task 1: Convert Fahrenheit to Celsius using numpy.vectorize
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

temperatures_f = np.array([32, 68, 100, 212, 77])
vectorized_f_to_c = np.vectorize(fahrenheit_to_celsius)
temperatures_c = vectorized_f_to_c(temperatures_f)

# Task 2: Custom power function with numpy.vectorize
def power_func(base, exp):
    return base ** exp

bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
vectorized_power = np.vectorize(power_func)
powered_values = vectorized_power(bases, exponents)

# Task 3: Solve the system of equations
A1 = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
b1 = np.array([7, 4, 5])
x1 = np.linalg.solve(A1, b1)

# Task 4: Solve the electrical circuit equations
A2 = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
b2 = np.array([12, -5, 15])
x2 = np.linalg.solve(A2, b2)

# Image Manipulation with NumPy and PIL
def flip_image(image_array):
    return np.flipud(np.fliplr(image_array))

def add_noise(image_array):
    noise = np.random.randint(-30, 30, image_array.shape)
    return np.clip(image_array + noise, 0, 255)

def brighten_channels(image_array, value=40):
    image_array[:, :, 0] = np.clip(image_array[:, :, 0] + value, 0, 255)  # Red channel
    return image_array

def apply_mask(image_array, size=100):
    h, w, _ = image_array.shape
    start_h, start_w = h // 2 - size // 2, w // 2 - size // 2
    image_array[start_h:start_h+size, start_w:start_w+size] = 0
    return image_array

# Load image
image_path = 'images/birds.jpg'
image = Image.open(image_path)
image_array = np.array(image, dtype=np.int16)

# Apply transformations
flipped_image = flip_image(image_array.copy())
noisy_image = add_noise(image_array.copy())
brightened_image = brighten_channels(image_array.copy())
masked_image = apply_mask(image_array.copy())

# Save images
Image.fromarray(np.uint8(flipped_image)).save('images/birds_flipped.jpg')
Image.fromarray(np.uint8(noisy_image)).save('images/birds_noisy.jpg')
Image.fromarray(np.uint8(brightened_image)).save('images/birds_brightened.jpg')
Image.fromarray(np.uint8(masked_image)).save('images/birds_masked.jpg')

