import cv2
import numpy as np

def laplacian_pyramid_decomposition(image, levels):
    pyramid = []
    temp = image.copy()

    for _ in range(levels):
        blurred = cv2.GaussianBlur(temp, (5, 5), 0)
        upsampled = cv2.resize(blurred, (temp.shape[1], temp.shape[0]), interpolation=cv2.INTER_LINEAR)
        laplacian = temp - upsampled
        pyramid.append(laplacian)
        temp = blurred

    pyramid.append(temp)  # Append the final approximation

    return pyramid

def gaussian_pyramid_decomposition(image, levels):
    pyramid = [image]

    for _ in range(levels):
        downsampled = cv2.pyrDown(pyramid[-1])
        pyramid.append(downsampled)

    return pyramid

def laplacian_fusion(laplacian_visible, laplacian_nir, gaussian_weights_visible, gaussian_weights_nir):
    fused_pyramid = []

    for lv, ln, gwv, gwn in zip(laplacian_visible, laplacian_nir, gaussian_weights_visible, gaussian_weights_nir):
        fused_layer = gwv * lv + gwn * ln
        fused_pyramid.append(fused_layer)

    return fused_pyramid

def collapse_pyramid(pyramid):
    collapsed_image = pyramid[-1]

    for layer in reversed(pyramid[:-1]):
        expanded = cv2.resize(collapsed_image, (layer.shape[1], layer.shape[0]), interpolation=cv2.INTER_LINEAR)
        collapsed_image = expanded + layer

    return collapsed_image


# Load visible and NIR images
visible_image = cv2.imread('path/to/visible_image.jpg', cv2.IMREAD_GRAYSCALE)
nir_image = cv2.imread('path/to/nir_image.jpg', cv2.IMREAD_GRAYSCALE)

# Resize images to the desired size

visible_image = cv2.resize(visible_image, (640, 480))
nir_image = cv2.resize(nir_image, (640, 480))

# Perform Laplacian pyramid decomposition on visible and NIR images
laplacian_visible = laplacian_pyramid_decomposition(visible_image, levels=1)
laplacian_nir = laplacian_pyramid_decomposition(nir_image, levels=1)

# Perform Gaussian pyramid decomposition on normalized weight maps
gaussian_weights_visible = gaussian_pyramid_decomposition(normalized_weight_map_visible, levels=1)
gaussian_weights_nir = gaussian_pyramid_decomposition(normalized_weight_map_nir, levels=1)

# Fuse the Laplacian pyramids using the Gaussian pyramids as weights
fused_laplacian = laplacian_fusion(laplacian_visible, laplacian_nir, gaussian_weights_visible, gaussian_weights_nir)

# Collapse the fused Laplacian pyramid to obtain the fused image
fused_image = collapse_pyramid(fused_laplacian)

# Display the fused image
cv2.imshow('Fused Image', fused_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
