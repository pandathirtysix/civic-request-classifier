import pickle
from utils.ohe import ListOfData
import numpy as np


class ModelsPredictions:
    def __init__(self):
        #models
        self.model_intent = pickle.load(open("MODELS/model_intent.pkl", "rb"))
        self.model_department = pickle.load(open("MODELS/model_department.pkl", "rb"))
        self.model_severity = pickle.load(open("MODELS/model_severity.pkl", "rb"))
        self.model_urgency = pickle.load(open("MODELS/model_urgency.pkl", "rb"))
        self.model_category = pickle.load(open("MODELS/model_category.pkl", "rb"))

        #label encoders
        self.cat_LE = pickle.load(open("MODELS/cat_LE.pkl", "rb"))
        self.dep_LE = pickle.load(open("MODELS/dep_LE.pkl", "rb"))
        self.ug_LE = pickle.load(open("MODELS/ug_LE.pkl", "rb"))
        self.severity_LE = pickle.load(open("MODELS/severity_LE.pkl", "rb"))
        self.intent_LE = pickle.load(open("MODELS/ohe_intent.pkl", "rb"))

        #tfidf
        self.tfidf_eg = pickle.load(open("MODELS/tfidf_english_gloss.pkl", "rb"))



    def model_intent_prediction(self, text):
        text = self.tfidf_eg.transform([text.lower()])
        text = text.toarray()
        prediction = self.model_intent.predict(text)
        result_intent = self.intent_LE.inverse_transform(prediction)
        return result_intent

    def model_department_prediction(self, text):
            text = self.tfidf_eg.transform([text.lower()])
            text = text.toarray()
            prediction = self.model_department.predict(text)
            result_intent = self.dep_LE.inverse_transform(prediction)
            return result_intent

    def model_severity_prediction(self, text):
            text = self.tfidf_eg.transform([text.lower()])
            text = text.toarray()
            prediction = self.model_severity.predict(text)
            result_intent = self.severity_LE.inverse_transform(prediction)
            return result_intent

    def model_urgency_prediction(self, text):
            text = self.tfidf_eg.transform([text.lower()])
            text = text.toarray()
            prediction = self.model_urgency.predict(text)
            result_intent = self.ug_LE.inverse_transform(prediction)
            return result_intent

    def model_category_prediction(self, text):
            text = self.tfidf_eg.transform([text.lower()])
            text = text.toarray()
            prediction = self.model_category.predict(text)
            result_intent = self.cat_LE.inverse_transform(prediction)
            return result_intent
    

        