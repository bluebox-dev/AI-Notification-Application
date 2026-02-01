from ultralytics import YOLO
import cv2
import requests
import time

# ====== CONFIG ======
BOT_TOKEN = "8219233364:AAF_cZc7E0SKIOtQdTNITA0R7fqcINpICSs"
CHAT_ID = "8347692850"

CONF_THRESHOLD = 0.5
TARGET_CLASSES = ["1", "5", "10"]   # ชื่อ class ตาม model.names
COOLDOWN_SECONDS = 10
# ====================

if not BOT_TOKEN or not CHAT_ID:
    print("❌ Please set TG_BOT_TOKEN and TG_CHAT_ID")
    exit()

model = YOLO("best.pt")

print("📦 Model classes:", model.names)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Cannot open webcam")
    exit()

last_sent_time = 0
object_present = False   # ใช้เช็คเข้าใหม่

def send_telegram(image_path, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(image_path, "rb") as img:
        requests.post(
            url,
            data={"chat_id": CHAT_ID, "caption": text},
            files={"photo": img},
            timeout=10
        )

print("🎥 Webcam started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)[0]
    detected_now = False
    detected_labels = []

    for box in results.boxes:
        conf = float(box.conf)
        cls = int(box.cls)
        label = str(model.names[cls])  # แปลงให้ชัวร์

        if conf >= CONF_THRESHOLD and label in TARGET_CLASSES:
            detected_now = True
            detected_labels.append(f"{label} ({conf:.2f})")

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame,
                f"{label} {conf:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    cv2.imshow("YOLO Coin Detection", frame)

    current_time = time.time()

    # ===== ส่ง Telegram เฉพาะ "เข้าใหม่" =====
    if detected_now and not object_present:
        if current_time - last_sent_time >= COOLDOWN_SECONDS:
            last_sent_time = current_time
            object_present = True

            output_image = "detected.jpg"
            cv2.imwrite(output_image, frame)

            caption = "🚨 Detected coin:\n" + "\n".join(detected_labels)
            send_telegram(output_image, caption)
            print("📨 Sent to Telegram")

    # reset เมื่อไม่เจอแล้ว
    if not detected_now:
        object_present = False

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
print("🛑 Webcam stopped")
