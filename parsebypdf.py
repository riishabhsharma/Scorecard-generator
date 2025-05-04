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
    given_answer_tag= panel.find("td", string="Given Answer :")
    #MCQ 
    if question_id_tag and chosen_option_tag:
        question_id = question_id_tag.find_next_sibling("td").text.strip()
        chosen_option = chosen_option_tag.find_next_sibling("td").text.strip()

        # Skip unattempted questions
        if chosen_option != "--":
            option_id_tag = panel.find("td", string=f"Option {chosen_option} ID :")
            if option_id_tag:
                answer_id = option_id_tag.find_next_sibling("td").text.strip()
                extracted_data[question_id]=answer_id
    #Integer based   
    if question_id_tag and given_answer_tag:
        question_id=question_id_tag.find_next_sibling("td").text.strip()
        given_answer=given_answer_tag.find_next_sibling("td").text.strip()
        if given_answer != "--":
            extracted_data[question_id]=given_answer

#ANSWER KEY FILE 
with open("answerkey.json", "r") as file:
    answer_key=json.load(file)


shift_key=answer_key["shift"]
physics_key=shift_key["physics"]
chemistry_key=shift_key["chemistry"]
maths_key=shift_key["math"]


#Physics Section
physics_marks=0
physics_pos_marks=0
physics_neg_marks=0
physics_total_attempt=0

#Physics loop for evaluation
for key in physics_key:
    #Condition for drop
    if physics_key[key]=="Drop":
        physics_marks+=4
        continue
    if key not in extracted_data:
        continue
    user_value=extracted_data[key]
    if(user_value==physics_key[key]):
        print(f"{key}: correct")
        physics_marks+=4
        physics_pos_marks+=4
        physics_total_attempt+=1

    else:
        print(f"{key}:wrong (your answer {user_value}, correct:{physics_key[key]})")
        physics_marks-=1
        physics_neg_marks-=1
        physics_total_attempt+=1

#Chemistry Section
chemistry_marks=0
chemistry_pos_marks=0
chemistry_neg_marks=0
chemistry_total_attempt=0

#Chemistry loop for evaluation
for key in chemistry_key:
    if chemistry_key[key]=="Drop":
        chemistry_marks+=4
        continue
    if key not in extracted_data:
        continue
    user_value=extracted_data[key]
    if(user_value==chemistry_key[key]):
        print(f"{key}: correct")
        chemistry_marks+=4
        chemistry_pos_marks+=4
        chemistry_total_attempt+=1

    else:
        print(f"{key}:wrong (your answer {user_value}, correct:{chemistry_key[key]})")
        chemistry_marks-=1
        chemistry_neg_marks-=1
        chemistry_total_attempt+=1


#Mathmatics Section 
maths_marks=0
maths_pos_marks=0
maths_neg_marks=0
maths_total_attempt=0

#Maths loop for evaluation
for key in maths_key:
    if maths_key[key]=="Drop":
        maths_marks+=4
        continue
    if key not in extracted_data:
        continue
    user_value=extracted_data[key]
    if(user_value==maths_key[key]):
        print(f"{key}: correct")
        maths_marks+=4
        maths_pos_marks+=4
        maths_total_attempt+=1

    else:
        print(f"{key}:wrong (your answer {user_value}, correct:{maths_key[key]})")
        maths_marks-=1
        maths_neg_marks-=1
        maths_total_attempt+=1

total_marks=(chemistry_marks)+(physics_marks)+(maths_marks)
print(f"Physics marks:{physics_marks}")
print(f"Physics positive score:{physics_pos_marks}")
print(f"Physics Negitive score:{physics_neg_marks}")
print(f"Chemistry marks:{chemistry_marks}")
print(f"Chemistry positive score:{chemistry_pos_marks}")
print(f"Chemistry Negitive score:{chemistry_neg_marks}")
print(f"Maths marks:{maths_marks}")
print(f"Maths positive score:{maths_pos_marks}")
print(f"Maths Negitive score:{maths_neg_marks}")
print(total_marks)
