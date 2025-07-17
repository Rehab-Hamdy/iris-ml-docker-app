Fixed Solutions Internship - Task 1

# 🌸 Iris Flower Classifier — API, Interface & Docker Deployment

## 📘 Original Project Summary

This project is based on the repository: [AchilleasKn/flask_api_python](https://github.com/AchilleasKn/flask_api_python), which demonstrates how to:

- Train a machine learning model (Logistic Regression) on the Iris dataset.  
- Save the model using `pickle`.  
- Build a Flask REST API to serve predictions.  
- Containerize the API using Docker for easy deployment.  
- Test the API using Postman with JSON input.  

---

## 💠 Enhancements and Additions I Made

### 🔍 1. Model Update

- Replaced the Logistic Regression model with an **SVM (Support Vector Machine)** classifier.  
- Trained the model on the same Iris dataset and saved it as `iris_model.pkl`.  

---

### 💡 2. API Testing with Postman

- Used **Postman** to test the `/predict` endpoint with various inputs and confirmed proper JSON responses.  

---

### 🖥️ 3. Added a Web Interface

- Developed a modern, user-friendly **HTML + CSS form interface**.  
- Users can input flower measurements (sepal & petal dimensions) to classify the Iris species.  
- Predicts and displays the Iris species name.  

---

### 🔀 4. Flask App Enhancement

Separated the project into two parts for better organization and deployment:
- Backend Flask API:
    - /predict handles JSON-based POST requests and returns the predicted Iris species.
- Frontend Interface:
    - Provides an HTML/CSS form for users to input flower measurements.
Sends the data to the backend and displays the prediction result in the browser. 

---

### 🐳 5. Docker Deployment

This project uses Docker Compose to run both the Flask backend (API) and the HTML/CSS frontend together.

#### 🧱 What I Did:

✅ Created two Dockerfiles:  
- One for the Flask backend  — runs the API and handles predictions.  
- One for the frontend  — serves the HTML and CSS files.  

✅ Used **Docker Compose** to run both services at the same time and connect them.

#### ▶️ How to Run:

1. Open a terminal inside the project folder.  
2. Run this command:  
   ```bash
   docker-compose up --build
3. Open your browser at:
   👉 http://localhost:8080
  You'll see the Iris Flower Classifier interface. Enter flower measurements to get the predicted Iris species.

### 🌐 6. Public Access via Ngrok

* Use **Ngrok** to expose the Dockerized app publicly for testing.
```bash
ngrok http 8080
```

### 📱 7. Mobile Testing

* Accessed and tested the deployed Ngrok link directly on a **mobile phone**, verifying the full functionality and responsive behavior of the interface.
