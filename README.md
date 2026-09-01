# Face Detection System (OpenCV + Flask)

Image upload karo, app OpenCV ke Haar Cascade classifier se faces detect karke
green box ke saath dikhata hai.

## Folder Structure
```
face-detection-webapp/
├── app.py                 # Flask backend + detection logic
├── requirements.txt
├── templates/
│   └── index.html         # Upload page + result page
└── static/
    ├── uploads/            # user ki original images
    └── results/            # detected faces wali images
```

## 1) Apne computer par run karna (local testing)

1. Python 3.9+ install hona chahiye.
2. Terminal me project folder me jao:
   ```
   cd face-detection-webapp
   ```
3. Virtual environment banao (optional but recommended):
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```
4. Dependencies install karo:
   ```
   pip install -r requirements.txt
   ```
5. App run karo:
   ```
   python app.py
   ```
6. Browser me kholo: **http://127.0.0.1:5000**

Image upload karo aur "Detect Faces" dabao — result niche dikh jayega.

## 2) College ke liye "link" kaise nikale

Teacher ko dikhane ke liye ek public link chahiye ho to 2 aasan options:

### Option A — Render.com (free, permanent link) — recommended
1. GitHub par ek naya repo banao aur ye poora folder push kar do.
2. https://render.com par free account banao → "New Web Service" →
   apna GitHub repo connect karo.
3. Settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. `requirements.txt` me ek line add kar dena: `gunicorn==22.0.0`
5. Deploy hote hi Render ek public URL de dega, jaise
   `https://face-detection-xxxx.onrender.com` — yahi link college me submit karna.

### Option B — ngrok (temporary link, sirf demo ke liye, 2 min me ready)
1. `python app.py` se app local chalao.
2. Ek naya terminal me:
   ```
   ngrok http 5000
   ```
3. ngrok ek temporary public URL dega — wahi copy karke share/submit kar do.
   (Yeh link tab tak chalega jab tak tumhara laptop aur ngrok on hai.)

## Kaise kaam karta hai (viva/explanation ke liye)
- **Haar Cascade Classifier**: OpenCV ka pre-trained ML model hai jo edges aur
  patterns ke combinations se face-like regions dhoondta hai.
- Image pehle grayscale me convert hoti hai (detection fast aur accurate hota hai).
- `detectMultiScale()` alag-alag scale par image scan karke faces dhoondta hai.
- Har detected face ke around green rectangle draw hota hai aur result save/display hota hai.

## Aage improve karne ke liye ideas (agar extra marks chahiye)
- Haar Cascade ki jagah **DNN face detector** (OpenCV's `res10_300x300_ssd_iter_140000.caffemodel`) use karo — zyada accurate hai.
- Webcam se live face detection add karo (`cv2.VideoCapture(0)`).
- Face recognition (naam pehchanna) add karo `face_recognition` library se.
