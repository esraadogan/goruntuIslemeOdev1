import cv2
import numpy as np

image=cv2.imread("esraresim.webp")
cv2.imshow("resim",image)
import matplotlib.pyplot as plt
from PIL import Image
image = Image.open("esraresim.webp")
image = image.convert("L")

width, height = image.size


histogram = [0] * 256


for y in range(height):
    for x in range(width):
        pixel_value = image.getpixel((x, y))
        histogram[pixel_value] += 1


plt.bar(range(256), histogram)
plt.title("Histogram")
plt.xlabel("Piksel Değeri")
plt.ylabel("Piksel Sayısı")
plt.show()