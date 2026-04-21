# 💊 MediBondhu — Your Personal Medicine Assistant

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat-square&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

MediBondhu is an AI-powered web application that identifies medicines from images and provides detailed information including the medicine's name, uses, side effects, and precautions — all in seconds.

---

## ✨ Features

- **Image-based Medicine Identification** — Upload a photo of any medicine (strip, bottle, box, or blister pack) and let the AI do the rest.
- **Detailed Medicine Info** — Get structured output covering name, uses, side effects, and precautions.
- **Multi-image Support** — Analyse up to 3 medicine images in a single session.
- **Clean, Modern UI** — Glassmorphism design with smooth animations built with custom Streamlit CSS.

---

## 🖥️ Demo

> Upload a medicine image → Click **Identify** → Get instant AI-generated details.

---

## 🗂️ Project Structure

```
medi_bondhu/
├── app.py              # Main Streamlit application & UI
├── api_calling.py      # AI API integration & response generation
├── background.png      # Background image for the UI
├── requirements.txt    # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/medi-bondhu.git
   cd medi-bondhu
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**

   Create a `.env` file in the root directory and add your AI API key:
   ```env
   API_KEY=your_api_key_here
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. Open your browser and go to `http://localhost:8501`

---

## 📦 Dependencies

```
streamlit
Pillow
python-dotenv
```

> See `requirements.txt` for the full list with pinned versions.

---

## 🧠 How It Works

1. The user uploads an image of a medicine (JPG, JPEG, or PNG).
2. The image is passed to `generate_response()` in `api_calling.py`, which sends it to an AI vision model.
3. The model analyses the image and returns structured information about the medicine.
4. The result is rendered back in the Streamlit UI under **Medicine Details**.

---

## ⚠️ Disclaimer

> MediBondhu is intended for **informational purposes only**. It is **not** a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider before taking any medication.

---

## 🛣️ Roadmap

- [ ] Bangla language support
- [ ] Medicine interaction checker (multi-drug analysis)
- [ ] Export results as PDF
- [ ] Mobile-optimised layout
- [ ] Medication reminders

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
  Made with ❤️ for better healthcare accessibility
</div>
