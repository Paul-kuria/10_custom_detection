import cv2 
import numpy as np 
from object_detection import ObjectDetection
from obj_parser import parse_video 

source = parse_video()
od = ObjectDetection() 

# Load video
cap = cv2.VideoCapture(source) 

# Initialize count
count = 0
center_points = []

while True:
    ret,frame = cap.read()

    count += 1
    if not ret:
        break 

    # Detect objects on frame
    (class_ids, scores, boxes) = od.detect(frame)
    for box in boxes:
        (x, y, w, h) = box # Draw rectangle
        print("frame #: ", count)
        print("Coord: ", x, y, w, h)
        cx = int((x + x + w)/2)
        cy = int((y+y+h)/2)
        center_points.append((cx, cy))
        print("cp:: ", center_points)
        cv2.rectangle(
            frame, 
            (x, y), 
            (x+w, y+h), 
            (0,255,0),
            2
            ) # Top left and bottom right points
        
    # Center point of each bounding box
    for pt in center_points:
        first_pt = center_points[0]
        #cv2.circle(frame, pt, 4, (0,0,255), -1)
        cv2.line(frame, pt, pt, (0,0,255), 2 )


    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()