import cv2
import smtplib
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading

# send email
def send_email(log_callback):
    sender_email = "bipronathsaha@gmail.com"
    sender_password = "gaxtgvpsvgeyfaot "  
    receiver_email = "sahabipronath@gmail.com"

    message = MIMEText("Face detected on your camera!")
    message['Subject'] = "Face Detection Alert"
    message['From'] = sender_email
    message['To'] = receiver_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        log_callback("Email sent successfully.")
    except Exception as e:
        log_callback(f"Error sending email: {e}")

# face detection function
def face_detection(log_callback, stop_event):
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )
    cap = cv2.VideoCapture(0)

    notified = False

    while not stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            log_callback("Error: Could not read video frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        if len(faces) > 0 and not notified:
            log_callback("Face detected!")
            send_email(log_callback)
            notified = True

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        cv2.imshow("Face Detector", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    log_callback("Face detection stopped.")

# GUI class
class FaceDetectorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("AI Face Detector with Notification")
        self.master.geometry("500x400")

        self.start_btn = tk.Button(master, text="Start Detection", command=self.start_detection)
        self.start_btn.pack(pady=10)

        self.stop_btn = tk.Button(master, text="Stop Detection", command=self.stop_detection, state=tk.DISABLED)
        self.stop_btn.pack(pady=5)

        self.log = scrolledtext.ScrolledText(master, width=60, height=15)
        self.log.pack(pady=10)

        self.stop_event = threading.Event()
        self.detector_thread = None

    def log_message(self, msg):
        self.log.insert(tk.END, f"{msg}\n")
        self.log.see(tk.END)

    def start_detection(self):
        self.log_message("Starting face detection...")
        self.stop_event.clear()
        self.detector_thread = threading.Thread(target=face_detection, args=(self.log_message, self.stop_event))
        self.detector_thread.start()
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)

    def stop_detection(self):
        self.log_message("Stopping detection...")
        self.stop_event.set()
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)

# main
if __name__ == "__main__":
    root = tk.Tk()
    app = FaceDetectorGUI(root)
    root.mainloop()
