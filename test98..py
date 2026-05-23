import cv2
import numpy as np
import math

# Start video capture
cap = cv2.VideoCapture(0)

print("Running Python 3.14 Pure-OpenCV Tracker. Press 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
        
    frame = cv2.flip(frame, 1)
    # Define a bounding box region to place your hand into
    cv2.rectangle(frame, (300, 100), (600, 400), (0, 255, 0), 2)
    roi = frame[100:400, 300:600]
    
    # 1. Blurring and converting color spaces to isolate skin color
    blur = cv2.GaussianBlur(roi, (3, 3), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    
    # Range for typical skin-tones in HSV spectrum
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    # Dilate and erode to fill in missing gaps in the hand mask
    kernel = np.ones((5, 5))
    mask = cv2.dilate(mask, kernel, iterations=4)
    mask = cv2.GaussianBlur(mask, (5, 5), 100)
    
    # 2. Find shapes/contours inside our masked region
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Assume the largest detected shape in the box is the hand
        max_contour = max(contours, key=lambda x: cv2.contourArea(x))
        
        if cv2.contourArea(max_contour) > 2000:
            # 3. Calculate the bounding wrapper (Convex Hull) around the hand shape
            hull = cv2.convexHull(max_contour, returnPoints=False)
            defects = cv2.convexValidity = cv2.convexityDefects(max_contour, hull)
            
            # Draw the green outline matching your skeleton structure
            cv2.drawContours(roi, [max_contour], -1, (0, 255, 0), 2)
            
            finger_count = 0
            
            if defects is not None:
                # 4. Analyze the deep "valleys" (defects) between fingers to locate fingertips
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(max_contour[s][0])
                    end = tuple(max_contour[e][0])
                    far = tuple(max_contour[f][0])
                    
                    # Compute triangle lengths to measure finger spacing angles
                    a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                    b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
                    c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
                    
                    # Cosine rule to check if the valley angle belongs to extended fingers
                    angle = math.acos((b**2 + c**2 - a**2) / (2 * b * c)) * 57
                    
                    if angle <= 90:
                        finger_count += 1
                        # Place Red dots at the base valley of extended fingers
                        cv2.circle(roi, far, 5, (0, 0, 255), -1)
                    
                    # Highlight the tip points
                    cv2.circle(roi, start, 5, (0, 0, 255), -1)
                
                # Dynamic text feedback on your stream
                cv2.putText(frame, f"Fingers Detected: {finger_count + 1}", (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('Python 3.14 Native Hand Tracker', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()