# invoice-document-classification

Classify invoice items received from the invoice recognition service into predefined categories.

The current model is based on the CountVectorizer embeddings and a dense neural network. But once more data is available, other models might perform better, so the following notebooks should be used to edit the model.

- **data_preparation.ipynb** used to generate training data from the OCR output.

- **models.ipynb** 
-- Exploratory analysis
-- text cleaning
-- testing & evaluating different classification models on the TF-iDF embeddings. (Multi Naive Bayes, XGB classifier, SVM, Logistic regression, Dense neural network)

- **embeddings.ipynb**  
 -- testing & evaluating different text embedding techniques (TF-iDF, CountVectorizer, Fasttext, Hierarchical embeddings, seq-Bert, bi-LSTM)
 -- model hyperparameters fine-tuning using Grid-search
 -- models' interpretation using Lime
 
 - **pyTorch.ipynb** re-write of the whole pipeline using pyTorch

- **prod.ipynb** train and save the chosen models to be used in the API


The rest is self-explanatory.
