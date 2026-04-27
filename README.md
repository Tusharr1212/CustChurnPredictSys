Customer Churn Prediction System

This project is an end-to-end Machine Learning system that predicts whether a customer is likely to churn (leave a service) based on their demographic and service usage data.

The system takes customer information as input and returns:
- Whether the customer will churn or not
- The probability of churn

It is built as a complete production-style pipeline with:
- Machine Learning model
- REST API backend
- Interactive web UI

UI & API Preview
<img width="1433" height="796" alt="API1" src="https://github.com/user-attachments/assets/2cbb8833-addf-432b-877a-0025a94576ef" />
<img width="1433" height="871" alt="API2" src="https://github.com/user-attachments/assets/a312c3c7-6116-40cc-839a-a3c6b3a99b79" />
<img width="1319" height="873" alt="UI1" src="https://github.com/user-attachments/assets/3b3ace71-4419-42fb-9603-102875eedfba" />
<img width="1263" height="880" alt="UI2" src="https://github.com/user-attachments/assets/2be0cf0d-a8e4-46ff-9dec-822f0f47a08d" />

Tech Stack

- Python 🐍  
- Pandas & NumPy  
- Scikit-learn 🤖  
- FastAPI ⚡  
- Streamlit 🎨  
- Joblib

How to Run This Project
1. Clone the Repository

2. Create virtual env
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3.Install Dependencies
pip install -r requirements.txt

4.Run FastAPI backend
- In terminal->uvicorn app.main:app --reload
- Then In browser->http://127.0.0.1:8000/docs

5. Run Streamlit UI
In terminal->streamlit run frontend/streamlit_app.py
Press enter and the UI should launch automatically.


👨‍💻 Author
Tushar Purohit
MS Computer Science @ TU Dresden

