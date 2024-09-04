import cv2
import numpy as np
from matplotlib import pyplot as plt

# load image
img = cv2.imread("dsa1.png")

# convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equal = cv2.equalizeHist(gray)
blurred = cv2.GaussianBlur(gray, (7,7), 0)
median = cv2.medianBlur(gray,9)
bm = cv2.medianBlur(blurred,7)
ret3,th3 = cv2.threshold(median,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
edge = cv2.Canny(th3, 0, 255)

cv2.imwrite('gausblur.png', blurred)
cv2.imwrite('median.png', median)
cv2.imwrite('blurmedian.png', bm)
cv2.imwrite('equalized.png', equal)
cv2.imwrite('ostu_threshold.png', th3)
cv2.imwrite('edge.png', edge)

# write result to disk
#cv2.imwrite("thresh.png", thresh)

#cv2.imshow("THRESH", thresh)
#cv2.imshow("RESULTS", results)
#plt.hist(dst.ravel(),256,[0,256]); plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
