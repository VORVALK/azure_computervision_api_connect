from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

# Replace with your own values
subscription_key = "??????"
endpoint = "??????/"

# Create a Computer Vision client
client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Image URL to analyze
image_url = "https://image.jpg"

# Analyze the image
image_analysis = client.analyze_image(image_url, visual_features=[VisualFeatureTypes.tags])

# Print the tags
print("Tags in the image:")
for tag in image_analysis.tags:
    print(f"- {tag.name} (confidence: {tag.confidence:.2f})")
