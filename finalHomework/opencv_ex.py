import numpy as np
import cv2 as cv

img = np.zeros((430, 350, 3), dtype='uint8')

# Vẽ đường tròn
center = (175, 200)
radius = 150
color = (37, 108, 240)
thickness = 3
cv.circle(img, center, radius, (255, 255, 255), -1, cv.LINE_AA)
cv.circle(img, center, radius, color, thickness, cv.LINE_AA)

# Chèn chữ HIT
text = 'HIT'
org = (80, 240)
font_face = cv.FONT_HERSHEY_SIMPLEX
font_scale = 4
font_thickness = 15
text_color = (37, 108, 240)
cv.putText(img, text, org, font_face, font_scale, text_color, font_thickness, cv.LINE_AA)

# Chèn dòng dưới cùng
text_1 = 'CLB TIN HOC DH CNHN'
org_1 = (87, 280)
font_scale_1 = 0.5
font_thickness_1 = 1
cv.putText(img, text_1, org_1, cv.FONT_HERSHEY_DUPLEX, font_scale_1, text_color, font_thickness_1, cv.LINE_AA)

# Vẽ chữ club
img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
text_2 = 'CLUB'
org_2 = (185, 265)
font_scale_2 = 0.85
font_thickness_2 = 2
cv.putText(img, text_2, org_2, font_face, font_scale_2, text_color, font_thickness_2, cv.LINE_AA)
img = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)

# Vẽ chuột
center_1 = (175, 125)
axes = (13, 18)
angle = 90     
start_angle = 0      
end_angle = 360      
thickness = 2
cv.ellipse(img, center_1, axes, angle, start_angle, end_angle, text_color, thickness, cv.LINE_AA)

x1 = (182, 114)
y1 = (182, 137)
x2 = (182, 125)
y2 = (202, 125)
x3 = (203, 123)
y3 = (203, 105)
cv.line(img, x1, y1, text_color, 2, cv.LINE_AA)
cv.line(img, x2, y2, text_color, 2, cv.LINE_AA)
cv.circle(img, (202, 123), 0, text_color, 2, cv.LINE_AA)
cv.line(img, x3, y3, text_color, 2, cv.LINE_AA)
cv.circle(img, (204, 104), 0, text_color, 2, cv.LINE_AA)

cv.imshow('Logo of HITclub', img)
# def mouse_callback(event, x, y, flags, param):
#     if event == cv.EVENT_LBUTTONDOWN:
#         print("Tọa độ chuột:", x, y)
# cv.setMouseCallback("Logo of HITclub", mouse_callback)
cv.waitKey()
cv.destroyAllWindows