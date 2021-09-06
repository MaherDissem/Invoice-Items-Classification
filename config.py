import os

vect_path = os.environ.get('VECTORIZER_PATH', './dumps/vectorizer.pkl')
lab_map_path = os.environ.get('LABEL_MAP_PATH', './dumps/label_map.pkl')
model_path = os.environ.get('MODEL_PATH', './dumps/')
