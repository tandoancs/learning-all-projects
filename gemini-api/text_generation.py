import google.generativeai as genai

import PIL.Image

genai.configure(api_key="AIzaSyAs3OP01_WptOspVPl6VTF0zfCzFTDbqsM")

model = genai.GenerativeModel("gemini-1.5-flash")
organ = PIL.Image.open("media/organ.jpg")
response = model.generate_content(["Tell me about this instrument", organ])
print(response.text)