# Medical Insurance Prediction App

## Overview

This project is a web application that predicts medical insurance charges based on user inputs such as age, BMI, number of children, and smoking status. Built using **FastAPI** and deployed on **Render**, it leverages a trained **XGBoost** model to deliver accurate predictions. The app features a user-friendly interface styled with **Tailwind CSS**, making it accessible and visually appealing. This project demonstrates my skills in data science, machine learning, and web development, combining predictive modeling with practical deployment for real-world use.

## Features

- **Predictive Modeling**: Uses an XGBoost model trained on a dataset of 1,338 records to predict insurance charges with an R² score of ~0.90 on test data.
- **Web Interface**: A responsive front-end built with HTML and Tailwind CSS, allowing users to input data and receive predictions seamlessly.
- **API Backend**: Powered by FastAPI, providing a robust and scalable API for predictions.
- **Deployment**: Hosted on Render, accessible via a public URL for real-time interaction.

## Live Demo

Try the app here: [Medical Insurance Predictor](https://medical-insurance-predictor.onrender.com)

*Note*: The app is hosted on Render's free tier, so there may be a brief delay on the first request due to idle timeout.

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Machine Learning**: XGBoost, Scikit-learn, Pandas, NumPy
- **Deployment**: Render
- **Other Tools**: Jinja2 (for templating), Git, GitHub

## Project Structure
![image](https://github.com/user-attachments/assets/9e8137b1-5ec2-4e48-a749-74b2525ab2b0)



## How It Works

1. The app loads a pre-trained XGBoost model (`model.pkl`) that was developed by analyzing a dataset of insurance charges.
2. Users input their details (age, sex, BMI, children, smoker status, region) via a web form.
3. The backend processes the input, dropping irrelevant features (sex, region) as identified during model training, and predicts charges using the model.
4. The predicted insurance charge is displayed to the user in the browser.

## Model Development

The model was developed using a Jupyter notebook (`Medical_Insurance_Prediction.ipynb`, not included in the deployment). Key steps included:

- **Data Exploration**: Analyzed `insurance.csv` to understand feature distributions and relationships.
- **Preprocessing**: Converted categorical variables (e.g., smoker status) to numerical values.
- **Feature Selection**: Identified smoker, BMI, and age as key predictors; dropped sex and region based on feature importance.
- **Training**: Used XGBoost with hyperparameter tuning via GridSearchCV, achieving high predictive accuracy.
- **Evaluation**: Achieved R² scores of ~0.87 (training) and ~0.90 (testing), with a cross-validation mean of ~0.86.

## Deployment

The app is deployed on **Render** using a `render.yaml` configuration:

- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`

## Limitations

- The free tier on Render may cause delays due to idle timeouts.
- The model does not handle edge cases (e.g., invalid inputs) robustly—future improvements could include input validation.

## About Me

I am a data science enthusiast with a strong foundation in predictive modeling, data analysis, and web development. This project showcases my ability to bridge machine learning with practical applications, a skill I aim to leverage in data science roles. I am also pursuing a **Dental Hygienist License** to deepen my understanding of healthcare systems, complementing my technical expertise with domain knowledge.




