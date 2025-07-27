import cv2
import mediapipe as mp
import pyautogui
import win32gui, win32con

# Function to keep OpenCV window always on top
def make_window_always_on_top(window_name):
    hwnd = win32gui.FindWindow(None, window_name)
    if hwnd:
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

# Initialize MediaPipe & camera
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

screen_w, screen_h = pyautogui.size()

# Smoothing setup
prev_x, prev_y = pyautogui.position()
smooth_factor = 0.3  # Adjust between 0.1 (very smooth) to 1 (instant)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        gesture = "No Hand"

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                landmarks = hand_landmarks.landmark
                finger_tips = [8, 12, 16, 20]
                fingers_open = 0
                for tip in finger_tips:
                    if landmarks[tip].y < landmarks[tip - 2].y:
                        fingers_open += 1

                # Get hand center
                cx = int(landmarks[9].x * screen_w)
                cy = int(landmarks[9].y * screen_h)

                # Clamp position to screen
                cx = max(0, min(cx, screen_w))
                cy = max(0, min(cy, screen_h))

                # Smooth movement
                smoothed_x = prev_x + (cx - prev_x) * smooth_factor
                smoothed_y = prev_y + (cy - prev_y) * smooth_factor
                pyautogui.moveTo(smoothed_x, smoothed_y)
                prev_x, prev_y = smoothed_x, smoothed_y

                # Gesture actions
                if fingers_open == 0:
                    gesture = "Fist (Hold)"
                    pyautogui.mouseDown()
                elif fingers_open >= 3:
                    gesture = "Open Palm (Release)"
                    pyautogui.mouseUp()
                else:
                    gesture = "Partial"

        # Show gesture name
        cv2.putText(frame, gesture, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        window_name = "Gesture Control"
        cv2.imshow(window_name, frame)
        make_window_always_on_top(window_name)  # Keep this window on top

        # Exit on ESC
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
