import time
import pickle
from .utils.utils import clean_data

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

class Model:
    vectorizer = pickle.load(open("./models/tfidfVectorizer.pickle", "rb"))
    model = pickle.load(open("./models/lrModel.pickle", "rb"))

def get_review_sentiment(review, vectorizer, model):
    review = clean_data(review)
    review = vectorizer.transform([review])
    sentiment = model.predict(review)
    probability = model.predict_proba(review)

    return {
        "sentiment" : "Positive" if sentiment==1 else "Negative",
        "positive prediction" : probability[0][1],
        "negative prediction" : probability[0][0]
        }


app = FastAPI(title="Deploying a ML Model with FastAPI")

origins = [
    "http://localhost:3000",
    "localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return "The API is working ..."

@app.get("/predict/")
async def prediction(review:str):
    try:
        start = time.time()
        result = get_review_sentiment(review, Model.vectorizer, Model.model)
        duration = time.time() - start
        result["time"] = duration

        return {
            "success": True,
            "result": result
        }

    except Exception as error:
        return {
            "success": False,
            "errors": [str(error)]
        }
