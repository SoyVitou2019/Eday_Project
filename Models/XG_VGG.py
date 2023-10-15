

# import gradio as gr
import cv2
import numpy as np
from keras.applications.vgg16 import VGG16
import pickle
from sklearn import preprocessing

def XG_boosting_prediction(input_img):
    SIZE = 256 # Resized Image
    img = cv2.imread(input_img, cv2.IMREAD_COLOR)
    print(len(input_img))
    # Captures test/validation data and labels into respective lists
    img_resized = cv2.resize(img, (SIZE, SIZE))
    img_cvt = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

    pred_images = []
    pred_images.append(img_cvt)

    # Convert lists to arrays numpy
    pred_images = np.array(pred_images)

    # Normalize pixel values to between 0 and 1
    x_pred = pred_images / 255.0

    # Load feature extraction model (VGG16)
    vgg_model = VGG16(weights='imagenet', include_top=False, input_shape=(SIZE, SIZE, 3))
    # Send test data through feature extraction process
    x_pred_features = vgg_model.predict(x_pred)
    x_pred_features = x_pred_features.reshape(x_pred_features.shape[0], -1)

    # Load the XGBoost model
    with open(r"E:\Project Practicum\Eday_Project\Data GMB\GMB5.pkl", "rb") as f:
        loaded_model = pickle.load(f)
    all_class = loaded_model.classes_
    prediction = loaded_model.predict(x_pred_features)
    
    
    
    # # Open the text file in read mode
    file_path = r"D:\90 image dataset\name of the animals.txt"
    with open(file_path, 'r') as file:
        file_contents = file.readlines()
    classes = [line.strip() for line in file_contents]
    
    
    lebels = classes[40:50]
    # Encode labels from text to integers.
    le = preprocessing.LabelEncoder()
    le.fit(lebels)
    predict_text = le.inverse_transform([prediction])
    return predict_text