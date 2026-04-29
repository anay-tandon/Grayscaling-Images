import cv2

image = cv2.imread("piku.png")
cv2.imshow("Piku", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert the image to grayscale using OpenCV's built-in function

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Piku Gray", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert the image to grayscale by averaging the BGR pixel values

img = cv2.imread("piku.png")
(row, col) = img.shape[0:2]

for i in range(row):
    for j in range(col):
        # Find the average of the BGR pixel values
        img[i, j] = sum(img[i, j]) * 0.33

cv2.imshow("Piku Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()