import cv2
import math
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# x = width // 2
# y = height // 2

# w = width // 4
# h = height // 4

def draw_circle(event, x, y, flags, param):
	global pt1, pt2, click, release, radius_found

	if event == cv2.EVENT_LBUTTONDOWN:
		if click and release:
			pt1 = (0,0)
			pt2 = (0,0)
			click = False
			release = False
			radius_found = False
		else:
			pt1 = (x,y)
			pt2 = (x,y)
			click = True
	elif event == cv2.EVENT_LBUTTONUP:
		if click:
			pt2 = (x,y)
			radius_found = True
			release = True
	elif click and not release:
		pt2 = (x,y)	

	


pt1 = (0,0)
pt2 = (0,0)
click = False
release = False
radius_found = False

cap = cv2.VideoCapture(0)
cv2.namedWindow("Test")
cv2.setMouseCallback("Test", draw_circle)

while True:

	ret, frame = cap.read()

	# cv2.rectangle(frame, (x,y), (x+w,y+h), color=(0,0,255), thickness=4)


	if click:
		cv2.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=-1)

		if not release or radius_found:
			r = math.sqrt( (pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2 )
			r = int(r)
			cv2.circle(frame, center=pt1, radius=r, color=(0,0,255), thickness=5)
	
	cv2.imshow("Test", frame)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()