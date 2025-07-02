# AI Face Detector with Email Notification

This project is a Python-based real-time face detection system that uses OpenCV Haar cascades to detect faces through a webcam. When a face is detected, it automatically sends an email notification to a specified address.

The project also includes a simple GUI (built with `tkinter`) to start and stop face detection and view logs.

---

## 🚀 Features

- Real-time face detection using Haar cascades  
- Sends email alerts when a face is detected  
- Tkinter-based GUI with Start/Stop buttons  
- Log window showing detection events and email status  
- Easy to expand to other alerts (SMS, WhatsApp, MQTT, etc.)

---

## 📂 Project Structure

```

Face_Detector
├── main.py
└── README.md

````

---

## 🛠 Requirements

- Python 3.8+  
- Packages:  
  - opencv-python  
  - tkinter (included in Python by default)

Install OpenCV with:

```bash
pip install opencv-python
````

---

## ⚙️ Setup Instructions

1. Clone or download the project folder.

2. Enable **2-step verification** on your Gmail account and generate an **App Password** for Python SMTP (recommended for security).

3. Replace the following variables in `main.py`:

```python
sender_email = "youremail@gmail.com"
sender_password = "your_app_password"
receiver_email = "receiveremail@example.com"
```

4. Run the app:

```bash
python main.py
```

5. Click **Start Detection** on the GUI window.

6. The webcam window will open and start detecting faces. Logs will appear in the GUI, and an email will be sent if a face is detected.

7. Press **q** on the webcam window or click **Stop Detection** on the GUI to stop.

---

## 💡 Notes

* The `smtplib` module is built into Python, no need to install it.
* Haar cascades are included with OpenCV, no separate download is required.
* Gmail’s standard password may not work. You **must** use an App Password if you have 2FA enabled.

---

## 🛡 Security Tips

✅ Never commit your app password to GitHub.
✅ Use environment variables or a `.env` file if you plan to share the code publicly.
✅ Consider switching to a more secure mail service or token-based alerts for production.

---

## 📈 Future Enhancements

* Upgrade to YOLO or SSD for higher accuracy
* Add SMS or WhatsApp alerts
* Cloud integration (MQTT / Firebase)
* Face recognition to identify known people

---

## 🙌 Acknowledgements

* [OpenCV](https://opencv.org)
* [Python SMTP Library](https://docs.python.org/3/library/smtplib.html)
* Haar Cascade models by OpenCV

---

**Happy coding! 🎉**

```

