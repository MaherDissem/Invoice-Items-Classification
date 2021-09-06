from fastapi import APIRouter
import pickle
from numpy import argmax
from tensorflow.keras.models import load_model
import os

from config import vect_path, lab_map_path, model_path
from cleaning.text_cleaning import clean_text

# loading models
vectorizer = pickle.load(open(vect_path, 'rb'))
label_map = pickle.load(open(lab_map_path, 'rb'))
model = load_model(model_path)

router = APIRouter()


@router.post('/predict', tags=['Category prediction'])
def predict(invoice: dict):
    """
    returns the predicted category for each item in an invoice
    @param invoice: DocFile
    @return: output: dict
    """

    # concatenation of product name and supplier name for each item
    items = []
    supplier = invoice['data']['ocr_results']['supplier_name']
    products = invoice['data']['ocr_results']['product_designation']
    for item in products:
        items.append(item['transcript'] + " " + supplier)

    # text cleaning
    test = [clean_text(str(item)) for item in items]

    # embedding and prediction
    embeddings = vectorizer.transform(test)
    y_pred = [label_map[argmax(model.predict(vector))] for vector in embeddings]

    # output dict
    for e, item in enumerate(test):
        invoice['data']['ocr_results']['product_designation'][e]['class'] = y_pred[e]

    return invoice


