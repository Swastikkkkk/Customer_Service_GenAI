import google.generativeai as genai
from sql import *

genai.configure(api_key=" GEMINI API KEY ")

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])

stress_forms = [
    "Physical",
    "Emotional",
    "Psychological",
    "Work-related",
    "Financial",
    "Academic",
    "Family-related",
    "Relationship",
    "Environmental",
    "Social",
    "Chronic",
    "Acute",
    "Interpersonal",
    "Cognitive",
    "Traumatic",
    "Daily hassles",
    "Burnout",
    "Post-traumatic disorder (PTSD)",
    "Anxiety",
    "Depression",
    "Due to uncertainty",
    "Health-related",
    "Technology-induced",
    "Time-related",
    "Sleep deprivation-induced",
    "Nutrition-related",
    "Sexual harassment"
    "NULL"
]

def get_Chat_response(text,userid):
    define_keyword(text,userid)
    convo.send_message("Respond like a therapist under 50 words whose patient said:" + text)
    return str(convo.last.text)

def define_keyword(text,userid):
    convo.send_message("Given category=" + str(stress_forms) + "define the statement " + text + " using category in the list and return single word from the list")
    add_keyword(userid,str(convo.last.text))

def get_1st(userid):
    keyword = get_keyword(userid)
    if keyword == "null":
      return "Hey there! What is bothering you today!"
    else:
      convo.send_message("Given the context of: " + str(keyword) + "return a calming response under 20 words like a therapist")
      return str(convo.last.text)

