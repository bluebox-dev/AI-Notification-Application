from ultralytics import YOLO
import cv2
import requests

# ====== CONFIG ======
BOT_TOKEN = "8219233364:AAF_cZc7E0SKIOtQdTNITA0R7fqcINpICSs"
CHAT_ID = "8347692850"
CONF_THRESHOLD = 0.5
TARGET_CLASSES = ["1", "5","10"]  # Coin Object Classes
# ====================

model = YOLO("best.pt")

# โหลดภาพ
img_path = "image-test.jpg"
results = model(img_path)[0]

detected = False
img = cv2.imread(img_path)

for box in results.boxes:
    conf = float(box.conf)
    cls = int(box.cls)
    label = model.names[cls]

    if conf > CONF_THRESHOLD and label in TARGET_CLASSES:
        detected = True
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f"{label} {conf:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (0, 255, 0), 2)

if detected:
    cv2.imwrite("detected.jpg", img)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    files = {"photo": open("detected.jpg", "rb")}
    data = {
        "chat_id": CHAT_ID,
        "caption": "🚨 YOLO ตรวจพบวัตถุ"
    }

    requests.post(url, data=data, files=files)
    print("📨 Sent to Telegram")
else:
    print("❌ No target detected")
