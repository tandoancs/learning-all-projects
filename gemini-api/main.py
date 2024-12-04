import google.generativeai as genai

genai.configure(api_key="AIzaSyAs3OP01_WptOspVPl6VTF0zfCzFTDbqsM")
model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Explain how blockchain work")
# print(response.text)

response = model.generate_content("Write a story about a magic backpack.")
print(response.text)