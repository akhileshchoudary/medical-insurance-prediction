from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pickle
import pandas as pd

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize FastAPI app
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Define input data model
class InsuranceInput(BaseModel):
    age: int
    # sex: str
    bmi: float
    children: int
    smoker: str
    #region: str

# Home route
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Prediction route
@app.post("/predict")
def predict_charges(input_data: InsuranceInput):
    new_data = pd.DataFrame({
        "age": [input_data.age],
        #"sex": [input_data.sex],
        "bmi": [input_data.bmi],
        "children": [input_data.children],
        "smoker": [input_data.smoker],
        #"region": [input_data.region]
    })
    new_data["smoker"] = new_data["smoker"].map({"yes": 1, "no": 0})
    new_data = new_data[["age", "bmi", "children", "smoker"]]  # Use only important features
    prediction = model.predict(new_data)[0]
    return {"predicted_charges": round(float(prediction), 2)}