# import the class FastAPi
from fastapi import FastAPI
# Declare an instance of a class
app = FastAPI()
# the decorator @ tell python that will use the function below
# the get method read something in the web page

@app.get("/")
async def root():
     return {"message": "Hello World"}