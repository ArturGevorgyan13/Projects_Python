def print_question(question):

    print(f"{question["question"]}")

    for key,value in question["options"].items():

        print(f"{key}) {value}")

def checker(question,answer):

    if question["answer"]==answer:

        return True
    
    else:

        return False

print("* * * * * * * * * * * * * * * * * * * * * * * * * * * *")

print("                Welcome to my QuizGame                 ")

print("* * * * * * * * * * * * * * * * * * * * * * * * * * * *")

quiz=[
    {
        "question":"What is the capital of France?",
        "options":{
            "A":"Madrid",
            "B":"Berlin",
            "C":"Paris",
            "D":"Rome"
        },
        "answer":"C"
    },
    {
        "question":"What does CPU stand for?",
        "options":{
            "A":"Central Process Unit",
            "B":"Central Processing Unit",
            "C":"Computer Personal Unit",
            "D":"Control Program Unit"
        },
        "answer":"B"
    },
    {
        "question":"Which planet is known as the Red Planet?",
        "options":{
            "A":"Venus",
            "B":"Earth",
            "C":"Mars",
            "D":"Jupiter"
        },
        "answer":"C"
    },
    {
        "question":"Who wrote the play Romeo and Juliet?",
        "options":{
            "A":"Charles Dickens",
            "B":"William Shakespeare",
            "C":"Mark Twain",
            "D":"Jane Austen"
        },
        "answer":"B"
    },
    {
        "question":"What is 5 * 6?",
        "options":{
            "A":"30",
            "B":"11",
            "C":"56",
            "D":"25"
        },
        "answer":"A"
    }
]

SCORE=0

QUESTION_NUMBER=0

for question in quiz:

    print_question(question)
    
    QUESTION_NUMBER+=1

    answer=input("Enter your answer(A/B/C/D): ")

    if checker(question,answer):

        SCORE+=1

        print("Correct answer") 

        print(f"Your current score is {SCORE}/{QUESTION_NUMBER}")

    else:

        print("Incorrect answer")

        print(f"The correct answer is {question["answer"]}")

        print(f"Your current score is {SCORE}/{QUESTION_NUMBER}")

print(f"You have given {SCORE} correct answers.")

score=SCORE*100/QUESTION_NUMBER

print(f"Your score is {score}%") 