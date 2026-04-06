import cv2
import mediapipe as mp
import webbrowser
import time
import collections

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

tip_ids = [4, 8, 12, 16, 20]

tabs = 0
last_action_time = 0
cooldown = 2

# Stability buffer
history = collections.deque(maxlen=5)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    total_fingers = 0

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm_list = []

            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            fingers = []

            # 👍 THUMB (right hand logic)
            if lm_list[4][0] > lm_list[3][0]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 👍 OTHER FINGERS (IMPROVED LOGIC)
            for i in range(1, 5):
                tip_y = lm_list[tip_ids[i]][1]
                pip_y = lm_list[tip_ids[i] - 2][1]
                dip_y = lm_list[tip_ids[i] - 3][1]

                # multi-joint + margin check
                if tip_y < pip_y - 20 and tip_y < dip_y - 10:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total_fingers = fingers.count(1)

            # 🔥 STABILITY FILTER
            history.append(total_fingers)
            total_fingers = max(set(history), key=history.count)

            # Draw hand
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            # Show count
            cv2.putText(img, f"Fingers: {total_fingers}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            current_time = time.time()

            # 🔥 COOLDOWN + TAB LIMIT
            if current_time - last_action_time > cooldown:

                if total_fingers == 1 and tabs < 8:
                    webbrowser.open("http://google.com")
                    tabs += 1
                    last_action_time = current_time

                elif total_fingers == 2 and tabs < 8:
                    webbrowser.open("http://facebook.com")
                    tabs += 1
                    last_action_time = current_time

                elif total_fingers == 3 and tabs < 8:
                    webbrowser.open("http://youtube.com")
                    tabs += 1
                    last_action_time = current_time

                elif total_fingers == 4:
                    tabs = 0  # reset

    cv2.imshow("Hand Gesture (MediaPipe)", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()