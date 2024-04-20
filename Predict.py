from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import cv2
import numpy as np

# Replace with your own values
prediction_key = "??????"
endpoint = "https://westeurope.api.cognitive.microsoft.com/"
project_id = "??????"
published_name = "??????"

# Create a prediction client
credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(endpoint, credentials)

# Image URL to predict
# image_url = "url.."

# Read the local image (replace 'test.jpg' with your image path)
image_path = "local_image.jpg"
img = cv2.imread(image_path)
img = cv2.resize(img, (320, 240))
img = img / 255.0  # Normalize pixel values

# Reshape the image for prediction
img = np.reshape(img, [1, 320, 240, 3])

# Make a prediction against the published model
result = predictor.classify_image(project_id, published_name, img)

# Get predictions from an image url
# result = predictor.classify_image(project_id, published_name, url=image_url)

# Print the top predicted class
if result.predictions:
    top_prediction = result.predictions[0]
    print(f"Predicted class: {top_prediction.tag_name} (confidence: {top_prediction.probability:.2f})")
else:
    print("No predictions found.")

# Remember to replace the placeholders with your actual values.
