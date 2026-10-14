# NumPy arrays
# https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp

# 3-D NumPy Arrays
# https://stackoverflow.com/questions/62734866/how-to-create-a-3d-array-in-python-with-numpy

#Elementwise operations in NumPy
# https://medium.com/@jennycoreholt/understanding-numpy-elementwise-operations-universal-functions-and-broadcasting-f772a37ecc22


import numpy as np

def relative_luminance(r, g, b):
    RsRGB = r/255
    GsRGB = g/255
    BsRGB = b/255

    linear_r = toLinear(RsRGB)
    linear_g = toLinear(GsRGB)
    linear_b = toLinear(BsRGB)

    y = (0.2126*linear_r) + (0.7152 *linear_g) + (0.0722*linear_b)
    return y

def toLinear(val):
    if(val <= 0.03928):
        return val/12.92
    else:
        return ((val+0.055)/1.055)**2.4

def arrayToLinear(array):
    return np.where(array <= 0.03928, array/12.92, ((array+0.055)/1.055)**2.4)

def luminance_map(frame):
    blue_vals = frame[:, :, 0]/255
    green_vals = frame[:, :, 1]/255
    red_vals = frame[:, :, 2]/255

    linear_blue = arrayToLinear(blue_vals)
    linear_green = arrayToLinear(green_vals)
    linear_red = arrayToLinear(red_vals)

    y = (0.2126*linear_red) + (0.7152 *linear_green) + (0.0722*linear_blue)
    return y