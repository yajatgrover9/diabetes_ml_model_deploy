from fastapi import FastAPI
import uvicorn
import pickle
from models import Diabetes
app=FastAPI()
model=pickle.load(open("model.pkl","rb"))

@app.get("/")
def greet():
    return{"Hello! Welcome to Yajat's ML model"}
@app.get("/{name}")
def hello(name):
    return("Hello {}!".format(name))

@app.post("/predict")
def predict(req:Diabetes):
    preg=req.pregnancies
    glucose=req.glucose
    bp=req.bp
    skinthickness=req.skinthickness
    insulin=req.insulin
    bmi=req.bmi
    dpf=req.dpf
    age=req.age
    features=list([preg,glucose,bp,skinthickness,insulin,bmi,dpf,age])
    pred=model.predict([features])
    if (predict == 1):
        return {"Ans": "You have been tested positive"}
    else:
        return {"Ans": "You have been tested negative"}




if __name__=="__main__":
    uvicorn.run(app)
