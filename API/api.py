from fastapi import FastAPI,File,UploadFile
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import model_from_json
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

# # load json and create model
json_file = open('BDMedileaves\\model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("BDMedileaves\\mymodel.weights.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
class_names = ['Bohera', 'Devil backbone', 'Horitoki', 'Lemon grass', 'Nayon Tara','Neem','Pathor kuchi','Thankuni','Tulsi','Zenora']
@app.get("/ping")
async def ping():
    return "Hello, i am alive"

   
def read_file_as_image(data) -> np.ndarray:
    data = np.array(Image.open(BytesIO(data)))
    return data

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read()) 
    print(image.shape)
    image = np.expand_dims(image, axis=0)
    predictions = loaded_model.predict(image)
    return {"class": class_names[np.argmax(predictions[0])], "confidence":  float(np.max(predictions[0]))}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)