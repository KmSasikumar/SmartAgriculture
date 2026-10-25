
# Smart Agriculture Management System (SAMS)
## Live demo

**Live demo:** https://smart-agriculture-sasi.onrender.com

Hosted on Render's free tier (Singapore region) from the main branch. The service sleeps when idle, so the first visit after a while may take up to a minute to wake.

**Demo note:** The app runs on the SQLite database shipped in the repo, so accounts or data created on the live demo do not persist across restarts/redeploys.

**Deployment notes:**

- Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate --noinput`
- Start command: `gunicorn smart_agriculture.wsgi:application --bind 0.0.0.0:$PORT`
- Static files are served via WhiteNoise.
- Configuration via the `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`, and `DJANGO_SECRET_KEY` environment variables.

**Empowering Farmers with Data-Driven Decisions and AI Analysis**

## 📖 Project Overview
Smart Agriculture Management System (SAMS) is a comprehensive digital platform designed to solving the problem of decentralized farming information. It provides a single hub for farmers to monitor crop health, estimate yields, and calculate financial viability using real-time market data.

By integrating **Django** for secure data management and **TensorFlow.js** for client-side AI, SAMS bridges the gap between traditional farming and modern technology.

## 🚀 Key Features
- **🌿 AI-Based Soil Classification**: Instant soil type identification using an on-device Machine Learning model (TensorFlow.js). Zero latency, no server processing required.
- **💰 Crop Yield & Financial Calculator**: dedicated reporting tools to estimate yield per acre, projected revenue, and profit margins.
- **📊 Personalized Dashboard**: Secure user accounts track historical farming data, allowing seasonal comparisons.
- **🚜 Knowledge Hub**: Centralized access to government schemes (MOVCDNER, MIDH) and modern techniques (Hydroponics, Aeroponics).

## 🛠️ Technical Stack
| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | Python & Django | Business logic, Authentication, Database ORM |
| **Frontend** | HTML5, CSS3, JavaScript | Responsive UI |
| **AI / ML** | **TensorFlow.js** | Client-side Image Classification (Soil Analysis) |
| **Database** | SQLite | Relational data storage (Development) |
| **Environment** | Windows / Cross-platform | |

## 🏗️ System Architecture
The application uses a hybrid architecture:
1.  **Server-Side**: Django handles user sessions, database transactions (Yield/Production records), and serves the application views.
2.  **Client-Side**: The Soil Classification feature runs entirely in the user's browser using a pre-trained TF.js model.

> See [architecture.md](./Architecture.md) for detailed diagrams and database schemas.

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Pip (Python Package Installer)

### Steps
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/KmSasikumar/SmartAgriculture.git
    cd SmartAgriculture
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    For a deployed instance, set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`
    and `DJANGO_ALLOWED_HOSTS` in the environment (see
    `smart_agriculture/settings.py`).

3.  **Run Migrations**
    Initialize the database:
    ```bash
    python manage.py migrate
    ```

4.  **Start the Server**
    ```bash
    python manage.py runserver
    ```

5.  **Access the App**
    Open your browser and navigate to: `http://127.0.0.1:8000/`

## 🌟 Engineering Highlights
- **Zero-Latency AI**: Implemented `soil-classification.html` with direct TF.js integration, allowing offline-capable inference.
- **Data-Driven Financials**: Custom views (`views.py`) calculate user-specific profit/loss metrics based on variable inputs like land area and user costs.
- **Modular Design**: Separated static educational resources from dynamic user applications for better scalability.

---
## 👨‍💻 Author

| Information | Details |
| :--- | :--- |
| **Name** | **K. SasiKumar** |
| **Registration No** | **22BCE11638** |
| **Email** | Kommamani012@gmail.com |

*Built for the future of Smart Farming.*
