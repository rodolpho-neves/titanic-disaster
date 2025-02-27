# Titanic Disaster

## Descrição
Neste repositório você terá acesso a uma forma de resolver o problema do Titanic Disaster do Kaggle.
É realizado um processo limpeza, imputação e padronização dos dados, em notebooks diferentes. Além disso, ainda é utilizado uma serialização com pipeline para condensar o processo estes processos de transformação dos dados de entrada e salvar o modelo com Pickle (.pkl).

## API para acesso
Um arquivo app.py implementa uma API em Flask para utilizar o modelo treinado. A API carrega o arquivo 'model-titanic-pipeline.pkl' e pode ser acessada em dois endpoints.

### URL base
O endereço URL para acessar a API está configurado como padrão local `[http://127.0.0.1:5000]`.

### Endpoints
- 'GET /': para verificar o status da API e ir para a página inicial.
- 'POST /predict': Para enviar dados conforme o modelo de entrada do Titanic, em formato de dicionário, com uma ou mais entradas. A resposta da chamada será um dicionário com os valores enviados e uma coluna adicional com a resposta do modelo. Exemplo de dado que pode ser enviado

```python
dados = [{"Pclass": 3,"Name": "John Tribiani",
        "Sex": "male","Age": 22,"SibSp": 1,
        "Parch": 0,"Ticket": "A/5 21171",
        "Fare": 7.25,"Cabin": "","Embarked": "S"},
        {"Pclass": 1,"Name": "Ted Mosby",
        "Sex": "male","Age": 35,"SibSp": 0,
        "Parch": 1,"Ticket": "A/15 12345",
        "Fare": 17.25,"Cabin": "","Embarked": "S"}]
```
