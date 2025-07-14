# 🗣️ Lisa - Your Personal AI Voice Assistant

Lisa is a Python-based AI voice assistant that helps you perform various tasks like opening websites, playing music, and answering questions using natural language. Think of it as your own mini Alexa! 🎙️

---

## 🚀 Features

✅ Wake word detection ("Lisa", "Hey Lisa", "Hi Lisa", "Ok Lisa")  
✅ Open popular websites like Google, YouTube, Facebook, etc.  
✅ Play music from a pre-defined library  
✅ Ask general questions powered by **Groq API** (LLaMA 3 Model)  
✅ Female voice support (Hindi and English)  
✅ Environment variables support for API keys  

---

## 📂 Project Structure

```

├── main.py               # Main script for Lisa
├── musicLibrary.py       # Your custom music library dictionary
├── .env.example          # Example environment file for API keys
├── requirements.txt      # Python dependencies
└── README.md             # This file

````

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/shivanidevi789/Project_2-Lisa.git

cd Project_2-Lisa
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

* **Windows**:

  ```bash
  venv\Scripts\activate
  ```
* **Linux/Mac**:

  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up API Key

* Get your **Groq API Key** from [groq.com](https://groq.com).
* Create a `.env` file in the project root:

```
YOUR_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## ▶️ Run Lisa

```bash
python main.py
```

Say **"Lisa"**, and your assistant will start listening! 🎧

---

## 🎤 Example Commands

* **"Lisa, open Google"**
* **"Lisa, play tera zikr"**
* **"Lisa, what is the capital of France?"**
* **"Lisa, open YouTube"**

---

## 📜 Requirements

* Python 3.7+
* Internet Connection
* [Groq API Key](https://groq.com)

---

## 👩‍💻 Author

Made with ❤️ by Shivani ( https://github.com/shivanidevi789 )

---

## 📜 License

This project is licensed under the MIT License.

--- 
