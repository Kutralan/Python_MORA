import cv2
import numpy as np

# Canvas setup
# We create a separate black image canvas to store our drawing lines permanently
canvas = None
draw_color = (0, 0, 255)  # Starts as Red (BGR format)
color_name = "Red"
xp, yp = 0, 0  # Previous coordinates to draw continuous lines

cap = cv2.VideoCapture(0)
print("Air Canvas Running! Press 'c' to clear, 'b/g/r' to change colors, 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
        
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    
    # Initialize canvas size once we know the frame dimensions
    if canvas is None:
        canvas = np.zeros((h, w, 3), dtype=np.uint8)
        
    # Bounding box setup
    cv2.rectangle(frame, (250, 100), (600, 420), (0, 255, 0), 2)
    roi = frame[100:420, 250:600]
    
    # Process image to find hand outline
    blur = cv2.GaussianBlur(roi, (3, 3), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    kernel = np.ones((5, 5))
    mask = cv2.dilate(mask, kernel, iterations=4)
    mask = cv2.GaussianBlur(mask, (5, 5), 100)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        max_contour = max(contours, key=lambda x: cv2.contourArea(x))
        if cv2.contourArea(max_contour) > 2000:
            # Find the absolute top-most pixel point of the hand outline contour
            # This serves as our pen tip!
            top_point = min(max_contour, key=lambda item: item[0][1])[0]
            
            # Convert ROI local coordinates to overall screen coordinates
            cx, cy = top_point[0] + 250, top_point[1] + 100
            
            # Draw a visual pen pointer on the live stream
            cv2.circle(frame, (cx, cy), 10, draw_color, cv2.FILLED)
            
            # If this is the start of a stroke, initialize the tracking pointer
            if xp == 0 and yp == 0:
                xp, yp = cx, cy
                
            # Draw a line on our permanent canvas from the last position to the current position
            cv2.line(canvas, (xp, yp), (cx, cy), draw_color, 7)
            
            # Update history positions
            xp, yp = cx, cy
    else:
        # Reset tracking coordinates if the hand leaves the tracking space
        xp, yp = 0, 0

    # Combine the live webcam stream and our digital canvas drawing together
    # Convert canvas to grayscale, threshold it, invert it, and overlay it
    img_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
    
    # Merge frames seamlessly
    frame = cv2.bitwise_and(frame, img_inv)
    frame = cv2.bitwise_or(frame, canvas)
    
    # On-screen interface overlay
    cv2.putText(frame, f"Color: {color_name}", (35, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, draw_color, 2)
    cv2.putText(frame, "Controls: C = Clear | B = Blue | G = Green | R = Red", (35, 460), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    cv2.imshow("Air Canvas (Python 3.14)", frame)
    
    # Keyboard listener mechanics
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        canvas = np.zeros((h, w, 3), dtype=np.uint8)  # Clear drawing layer
    elif key == ord('b'):
        draw_color = (255, 0, 0)
        color_name = "Blue"
    elif key == ord('g'):
        draw_color = (0, 255, 0)
        color_name = "Green"
    elif key == ord('r'):
        draw_color = (0, 0, 255)
        color_name = "Red"
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()