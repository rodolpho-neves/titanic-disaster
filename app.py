from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# carregar o modelo que sera utilizado para a predicao
model_name = 'model-titanic-pipeline.pkl'
with open(model_name, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods=['GET'])
def home():
    message = """<h1>Bem-vindo à API de predição do Titanic Survival!</h1>
    <p>Este servidor foi desenvolvido e mantido pelos pesquisadores do</p> 
    <h3>Núcleo Interdisciplinar de Análise de Sinais (NIAS)</h3>
    <h3>Universidade Federal de Viçosa (UFV)</h3>"""
    return message

@app.route('/predict', methods=['POST'])
def predict():
    dados = request.get_json(force=True)
    if np.size(dados) < 2:
        features = pd.DataFrame(data=dados, index=[0])
    else:
        features = pd.DataFrame(data=dados)
    prediction = model.predict(features)
    output = prediction.tolist()
    return jsonify(pd.concat([features, pd.DataFrame({'Survived': output}, index=range(len(output)))], axis=1).to_dict(orient='dict'))

if __name__ == '__main__':
    app.run(debug=True)