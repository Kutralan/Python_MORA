import cv2
import numpy as np
import math
import random
import time

# Game setup variables
choices = ["Rock", "Paper", "Scissors"]
computer_choice = ""
user_choice = ""
result_text = "Press SPACE to Play!"
score_user = 0
score_comp = 0

cap = cv2.VideoCapture(0)
print("Game running on Python 3.14. Press SPACE to play a round, 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
        
    frame = cv2.flip(frame, 1)
    
    # 1. Bounding box setup for hand tracking
    cv2.rectangle(frame, (300, 100), (600, 400), (0, 255, 0), 2)
    roi = frame[100:400, 300:600]
    
    # 2. Process image to find skin/hand outline
    blur = cv2.GaussianBlur(roi, (3, 3), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    kernel = np.ones((5, 5))
    mask = cv2.dilate(mask, kernel, iterations=4)
    mask = cv2.GaussianBlur(mask, (5, 5), 100)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Track calculated finger counts
    finger_count = 0
    
    if contours:
        max_contour = max(contours, key=lambda x: cv2.contourArea(x))
        if cv2.contourArea(max_contour) > 2000:
            hull = cv2.convexHull(max_contour, returnPoints=False)
            defects = cv2.convexityDefects(max_contour, hull)
            cv2.drawContours(roi, [max_contour], -1, (0, 255, 0), 2)
            
            if defects is not None:
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(max_contour[s][0])
                    end = tuple(max_contour[e][0])
                    far = tuple(max_contour[f][0])
                    
                    a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                    b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
                    c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
                    angle = math.acos((b**2 + c**2 - a**2) / (2 * b * c)) * 57
                    
                    if angle <= 90:
                        finger_count += 1
                        cv2.circle(roi, far, 5, (0, 0, 255), -1)
                    cv2.circle(roi, start, 5, (0, 0, 255), -1)
    
    # 3. Determine actual move based on finger count thresholding
    # Offset by 1 because the baseline count reads the index start point
    total_fingers = finger_count + 1 if contours and cv2.contourArea(max_contour) > 2000 else 0
    
    if total_fingers <= 1:
        current_detected_move = "Rock"
    elif 2 <= total_fingers <= 3:
        current_detected_move = "Scissors"
    else:
        current_detected_move = "Paper"
        
    # 4. Draw HUD Text / Information Matrix onto the main frame
    cv2.putText(frame, f"Your Move: {current_detected_move}", (35, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    
    # Game Status Box
    cv2.putText(frame, f"Match: {result_text}", (35, 430), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(frame, f"Comp chose: {computer_choice}", (35, 465), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)
    
    # Scoreboards
    cv2.putText(frame, f"YOU: {score_user}", (35, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"CPU: {score_comp}", (35, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Rock Paper Scissors Game (Python 3.14)", frame)
    
    # 5. Handle Keyboard Controls
    key = cv2.waitKey(1) & 0xFF
    
    # Press SPACEBAR to register a choice
    if key == ord(' '):
        user_choice = current_detected_move
        computer_choice = random.choice(choices)
        
        # Win / Loss evaluating Matrix
        if user_choice == computer_choice:
            result_text = "IT'S A TIE!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result_text = "YOU WIN! 🎉"
            score_user += 1
        else:
            result_text = "YOU LOSE! ❌"
            score_comp += 1
            
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()