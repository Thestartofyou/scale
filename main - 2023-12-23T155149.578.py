import cv2
import numpy as np

def calculate_square_footage(mask, scale):
    # Assuming scale is in meters per pixel
    square_meter_per_pixel = scale ** 2
    total_pixels = np.count_nonzero(mask)
    total_square_meters = total_pixels * square_meter_per_pixel
    total_square_feet = total_square_meters * 10.764  # 1 square meter = 10.764 square feet
    return total_square_feet

# Load binary mask of buildings (white pixels represent buildings)
mask = cv2.imread('building_mask.png', cv2.IMREAD_GRAYSCALE)

# Set the scale in meters per pixel
scale = 0.5  # Change this value based on your specific satellite imagery

square_footage = calculate_square_footage(mask, scale)

print(f'Total Square Footage: {square_footage} square feet')
