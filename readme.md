🚀 AI Smart Decision Assistant

An intelligent web-based application that helps users make real-time decisions based on their situation.
It supports both:

- 🛡 Safety Analysis (crowd, risk, help suggestions)
- 🛒 Product Recommendations (phones, laptops, etc.)

---

📌 Project Overview

The AI Smart Decision Assistant is designed to analyze user input and provide:

- 🔍 Context-aware safety insights
- 📍 Nearby help recommendations using location
- 🛒 Smart product suggestions based on user needs

This project combines AI-based semantic search with a simple and interactive UI.

---

🧠 Features

🛡 Safety Mode

- Detects real-world situations (crowd, night, unsafe areas)
- Provides:
  - Crowd Level
  - Risk Level
  - Confidence Score
  - Action Suggestions
  - Help Type (Police, Safe Area, etc.)
- Shows nearby help using Google Maps
- Option to book Rapido

---

🛒 Product Recommendation Mode

- Detects product-related queries like:
  - "best phone for camera"
  - "budget laptop under 50000"
- Displays:
  - Product Name
  - Price
  - Platform (Amazon/Flipkart)
- Provides Buy Now option

---

⚙️ Tech Stack

- Frontend: HTML, CSS (Responsive UI)
- Backend: Python (Flask)
- AI Model: Sentence Transformers ("all-MiniLM-L6-v2")
- Libraries:
  - NumPy
  - Scikit-learn
  - Sentence Transformers
- APIs:
  - Geolocation API (Browser)
  - Google Maps Embed

---

📂 Project Structure

AI_Decision_Assistant/
│
├── templates/
│   └── index.html
│
├── app.py
├── endee_engine.py
├── decision_engine.py
├── data.json          # Safety dataset
├── products.json      # Product dataset
├── requirements.txt

---

🚀 How It Works

1. User enters input (e.g., "crowded railway station" or "best phone for camera")
2. System detects:
   - Safety query OR Product query
3. If Safety:
   - Uses AI model to find closest context
4. If Product:
   - Searches product dataset
5. Displays results dynamically on UI

---

▶️ How to Run

1️⃣ Install Dependencies

pip install -r requirements.txt

2️⃣ Run the Application

python app.py

3️⃣ Open in Browser

http://127.0.0.1:5000

---

🧪 Example Inputs

Safety:

- "crowded market"
- "empty road at night"
- "unsafe street alone"

Product:

- "best phone for photography"
- "budget phone under 20000"
- "best laptop for coding"

---

⚠️ Limitations

- Some external websites (Amazon, Google) cannot be embedded in iframe due to security restrictions
- Product recommendations are based on predefined dataset

---

🔮 Future Enhancements

- 🔔 Real-time price tracking
- 📊 Advanced recommendation system using ML
- 🌐 Live API integration (Flipkart/Amazon)
- 📱 Mobile responsive UI
- 🧾 User personalization

---

👩‍💻 Author

Akhila Cuddapah
B.Tech CSE Student
Passionate about AI, Web Development & Smart Systems

---

⭐ Conclusion

This project demonstrates how AI can be used to assist users in both safety and daily decision-making, making it a unique and impactful application.

---