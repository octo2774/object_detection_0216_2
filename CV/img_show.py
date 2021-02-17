import cv2
import sys

img = cv2.imread("039.png" , cv2. IMREAD_GRAYSCALE)

if img is None :
    print("Image load failed!")
    sys.exit()

cv2.namedWindow('banana Image')
cv2.imshow("banana Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


