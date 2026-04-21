from google import genai
from dotenv import load_dotenv
from PIL import Image
import os
load_dotenv()
my_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=my_key)

def generate_response(images):
    pmt = """You are a helpful and precise assistant for identifying medicines. 
    I will provide you with images of medicines, then check if the image is actually a image of a medicine, if not then say give a proper image of medicine,
    if yes you will analyze them to identify the medicine's name, its uses, side effects, and precautions. 
    Please provide detailed information based on the images provided. also give the response in Bangla language. 
    If you are unable to identify the medicine, please respond with 'Sorry, I cannot identify this medicine based on the provided image.
    """

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents= [images, pmt]
    )
    return response.text
