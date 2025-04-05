# Imports
import cv2
import time
import requests
from ultralytics import YOLO

# Configs
title = "@evandanendraa - sidek v4"
model = YOLO("best_ncnn_model", task="detect")

GRID_DETECTION_THRESHOLD = 5
CONFIDENCE_THRESHOLD = 0.25
OPTIMIZE = True

TELEGRAM_BOT_TOKEN = 'SECRET'
TELEGRAM_CHAT_ID = '-1002575296321'
TELEGRAM_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'

fps = 0
frame_count = 0
start_time = time.time()

show_class_names = True

# Functions
def send_telegram_message(message):
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    try:
        response = requests.post(TELEGRAM_URL, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")

# Codes
cap = cv2.VideoCapture(0)
notification_sent = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, show=False, conf=CONFIDENCE_THRESHOLD, stream=OPTIMIZE)

    frame_count += 1
    elapsed_time = time.time() - start_time
    if elapsed_time > 0:
        fps = frame_count / elapsed_time

    detected_grids = set()
    height, width, _ = frame.shape

    for result in results:
        boxes = result.boxes
        classes = result.names
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            conf = box.conf[0]
            cls = int(box.cls[0])
            label = f"{classes[cls]}: {conf:.2f}"

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

            if show_class_names:
                cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            grid_x = int((x1 + x2) / 2) // (width // 3)
            grid_y = int((y1 + y2) / 2) // (height // 3)
            detected_grids.add((grid_x, grid_y))

    cv2.putText(frame, f'FPS: {fps:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    grid_color = (255, 255, 255)
    grid_thickness = 1

    for i in range(1, 3):
        x = int(i * width / 3)
        cv2.line(frame, (x, 0), (x, height), grid_color, grid_thickness)

    for i in range(1, 3):
        y = int(i * height / 3)
        cv2.line(frame, (0, y), (width, y), grid_color, grid_thickness)

    if len(detected_grids) >= GRID_DETECTION_THRESHOLD:
        if not notification_sent:
            text = "GRID LIMIT"
            text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
            x_center = (width - text_size[0]) // 2
            y_center = height // 2
            cv2.putText(frame, text, (x_center, y_center), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            send_telegram_message(f"[⚠️] LIMIT {len(detected_grids)}/9 | TARGET = {GRID_DETECTION_THRESHOLD}")
            notification_sent = True
    else:
        notification_sent = False

    cv2.putText(frame, f'Filled Grids: {len(detected_grids)}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow(title, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()