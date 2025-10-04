from google.generativeai import list_models
models = list_models()
for model in models:
    print(model.name)

