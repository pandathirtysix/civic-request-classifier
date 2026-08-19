# Civic Request Classifier & Public Complaint System

An NLP-powered Streamlit web application designed to streamline the process of receiving, evaluating, and managing public complaints. When a user submits a complaint, the system automatically analyzes the text using machine learning models to categorize and assess its priority.

## Key Features
- **AI-Powered Evaluation**: Automatically predicts five critical aspects of any public complaint:
  - **Category** (e.g., sanitation, transport, etc.)
  - **Department** (the relevant civic agency)
  - **Intent** (identifies if it's a request, complaint, or inquiry)
  - **Severity & Urgency** (helps prioritize attention)
- **Streamlit Interface**: Clean, modern web pages to lodge complaints and display reports.
- **Local Storage**: Automatically appends and saves evaluated complaints to a local database (`database.pkl`).

---

## Project Structure

```
├── MODELS/                           # Serialized machine learning models and encoders
│   ├── cat_LE.pkl                    # Category Label Encoder
│   ├── dep_LE.pkl                    # Department Label Encoder
│   ├── ohe_intent.pkl                # Intent One-hot/Label Encoder
│   ├── model_*.pkl                   # Trained SVM/Random Forest models for prediction
│   └── tfidf_english_gloss.pkl       # Fitted TF-IDF Vectorizer
│
├── datasets/                         # Data storage and local database files
│   ├── dataset/                      # Train/test datasets
│   ├── reportsdata/
│   │   └── database.pkl              # Historical record of all submitted reports (Pandas DataFrame)
│   ├── df_database.py                # Database initialization script
│   └── get_dataset.py                # Script to retrieve source dataset (JadeSamLee/civicdex)
│
├── pages/                            # Multi-page Streamlit routes
│   ├── user_report.py                # Complaint submission form (Lodge Report)
│   └── manage_reports.py             # Admin panel to view/manage reports (View Reports)
│
├── pipeline/
│   └── model_prediction.py           # Evaluation pipeline wrapping pipeline and encoders
│
├── utils/                            # Custom helpers and configurations
│
├── main.py                           # Application entry point/landing page
├── requirements.txt                  # List of Python dependencies
└── README.md                         # Project documentation
```

---

## Getting Started

### Prerequisites
Make sure you have Python 3.8+ installed on your system.

### 1. Installation
Clone the repository and install the required dependencies:
```bash
pip install -r requirements.txt
```

### 2. Database Initialization
If you need to initialize or reset the reports database:
```bash
python datasets/df_database.py
```

### 3. Running the Web Application
Launch the Streamlit app from the root directory:
```bash
streamlit run main.py
```
Open the local URL displayed in your terminal (typically `http://localhost:8501`) to interact with the application.

---

## Machine Learning Pipeline

The application loads six pickled resources at startup:
- **TF-IDF Vectorizer**: Translates raw text description into numeric features.
- **5 Classifiers**: Predict intent, department, severity, urgency, and category.
- **Label Encoders**: Decode the numeric predictions back into human-readable strings.

All predictions are calculated in real-time when the submit button is pressed within `pages/user_report.py`.
