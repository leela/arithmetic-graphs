from fastapi import FastAPI
import pandas as pd
import random
import json

app = FastAPI()

@app.get("/numbers")
def numbers():
    """Generates an array of size 10.
    """
    df = pd.DataFrame(random.sample(range(100), 10), columns=['A'])
    return json.loads(df.to_json())
