import cv2
import numpy as np


drawing = False
ix, iy = -1, -1


def draw_on_click(event, x, y, flags, param):
	global ix, iy, drawing

	#BLUE GREEN RED
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix = x
		iy = y
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing:
			cv2.rectangle(img, (ix, iy), (x,y), (120, 50, 170), 10)
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		cv2.rectangle(img, (ix, iy), (x,y), (120, 50, 170), 10)
		ix, iy = -1, -1
	elif event == cv2.EVENT_RBUTTONDOWN:
		cv2.circle(img, (x,y), 100, (255,0,0),-1)



img = np.zeros((512,512,3))
cv2.namedWindow(winname="my_drawing")
cv2.setMouseCallback("my_drawing", draw_on_click)

while True:

	cv2.imshow("my_drawing", img)

	if cv2.waitKey(20) & 0xFF == 27:
		break

cv2.destroyAllWindows()