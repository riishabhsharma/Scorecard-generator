from bs4 import BeautifulSoup
import json

# Load the file
file_path = r"C:\Learn\Projects\sources\DL01129290_2083O24353S16D61488E1.html"
with open(file_path, "r", encoding="utf-8") as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Prepare a list to hold extracted data
extracted_data = {}

# Find all question panels
question_panels = soup.find_all("div", class_="question-pnl")

# Loop through each question panel and extract required data
for panel in question_panels:
    question_id_tag = panel.find("td", string="Question ID :")
    chosen_option_tag = panel.find("td", string="Chosen Option :")

    if question_id_tag and chosen_option_tag:
        question_id = question_id_tag.find_next_sibling("td").text.strip()
        chosen_option = chosen_option_tag.find_next_sibling("td").text.strip()

        # Skip unattempted questions
        if chosen_option != "--":
            option_id_tag = panel.find("td", string=f"Option {chosen_option} ID :")
            if option_id_tag:
                answer_id = option_id_tag.find_next_sibling("td").text.strip()
                extracted_data[question_id]=answer_id

extracted_data
# print(extracted_data)
# print(len(extracted_data))
# print(type(extracted_data))

with open("answerkey.json", "r") as file:
    answer_key=json.load(file)
marks=0
correct_answer=0
wrong_answer=0
total_attempt=0
for key in answer_key:
    if key not in extracted_data:
        continue
    user_value=extracted_data[key]
    if(user_value==answer_key[key]):
        print(f"{key}: correct")
        marks+=4
        correct_answer+=1
        total_attempt+=1

    else:
        print(f"{key}:wrong (your answer {user_value}, correct:{answer_key[key]})")
        marks-=1
        wrong_answer+=1
        total_attempt+=1

print(marks)
print(correct_answer)
print(wrong_answer)
print(total_attempt)