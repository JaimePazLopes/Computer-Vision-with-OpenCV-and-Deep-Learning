import cv2

# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# x = width // 2
# y = height // 2

# w = width // 4
# h = height // 4

def draw_rectangle(event, x, y, flags, param):
	global pt1, pt2, topLeft_clicked, botRigh_clicked

	if event == cv2.EVENT_LBUTTONDOWN:
		if topLeft_clicked and botRigh_clicked:
			pt1 = (0,0)
			pt2 = (0,0)
			topLeft_clicked = False
			botRigh_clicked = False
		elif topLeft_clicked:
			pt2 = (x,y)
			botRigh_clicked = True
		else:
			pt1 = (x,y)
			topLeft_clicked = True



pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
botRigh_clicked = False

cap = cv2.VideoCapture(0)
cv2.namedWindow("Test")
cv2.setMouseCallback("Test", draw_rectangle)

while True:

	ret, frame = cap.read()

	# cv2.rectangle(frame, (x,y), (x+w,y+h), color=(0,0,255), thickness=4)


	if topLeft_clicked:
		cv2.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=-1)

		if botRigh_clicked:
			cv2.rectangle(frame, pt1, pt2, (0,0,255), 3)
	
	cv2.imshow("Test", frame)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()