# This file initializes the gbmodel package.

model_backend = 'cloud_datastore'

if (model_backend == 'sqlite3'):
    from .model_sqlite3 import model
elif (model_backend == 'cloud_datastore'):
    from .model_datastore import model
else:
    raise ValueError("No database backend configured.")

appmodel = model()

def get_model():
    return appmodel