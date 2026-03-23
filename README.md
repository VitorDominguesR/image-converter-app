# Image Converter App

A lightweight, blazing-fast Django web application designed to convert JPEG images to PNG format on the fly. 

Built with performance in mind, this app utilizes **OpenCV** to process image conversions entirely in your server's RAM (in-memory). This means no temporary files are saved to your hard drive, keeping your storage clean and your application fast.

## Features
* **In-Memory Processing:** Uses `io.BytesIO` and OpenCV to read, convert, and serve the image without touching the disk.
* **Minimalistic UI:** A clean, easy-to-use web interface for file uploads.
* **Automatic Downloads:** The converted PNG is instantly served back to the user as a downloadable attachment.
* **Format Validation:** Ensures only `.jpg` and `.jpeg` files are processed.

## Tech Stack
* **Framework:** Python / Django
* **Image Processing:** OpenCV (`opencv-python-headless`) & NumPy

## Installation

Follow these steps to get the development environment running locally:

**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/image-converter-app.git
cd image-converter-app
```

**2. Set up a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Apply migrations and start the server:**
```bash
python manage.py migrate
python manage.py runserver
```

## Usage
1. Open your browser and navigate to `http://127.0.0.1:8000/`.
2. Click **"Browse"** to select a JPEG image from your computer.
3. Click **"Convert and Download"**.
4. The converted PNG file will automatically begin downloading.

---

## ⚠️ TODO / Known Issues

* [ ] **URGENT:** Fix the app! It is currently breaking and throwing server errors during the conversion process in certain environments. Need to investigate to resolve the crashes.
* [ ] Add unit tests for the conversion view.
* [ ] Improve the UI/UX with CSS frameworks 
