from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

# Replace with your own values
subscription_key = "74eeab0087974f93916b68030e3006df"
endpoint = "https://learncpv.cognitiveservices.azure.com/"

# Create a Computer Vision client
client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Image URL to analyze
image_url = "https://picography.co/wp-content/uploads/2019/09/picography-espresso-sits-on-a-wooden-stool-768x1152.jpg"

# Analyze the image
image_analysis = client.analyze_image(image_url, visual_features=[VisualFeatureTypes.tags])

# Print the tags
print("Tags in the image:")
for tag in image_analysis.tags:
    print(f"- {tag.name} (confidence: {tag.confidence:.2f})")
