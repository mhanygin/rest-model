from django.apps import apps

modelName = dict()

for m in apps.get_models():
    modelName[m.__name__.lower()] = m
print(modelName)
