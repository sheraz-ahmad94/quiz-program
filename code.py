quiz = {
    "question 1": {
        "question": "Capital of France?",
        "answer": "Paris"
    },
    "question 2": {
        "question": "Capital of Afghanistan?",
        "answer": "Kabul"
    },
    "question 3": {
        "question": "Capital of Pakistan?",
        "answer": "Islamabad"
    },
    "question 4": {
        "question": "Capital of India?",
        "answer": "Delhi"
    },
    "question 5": {
        "question": "Capital of Iran?",
        "answer": "Tehran"
    },
    "question 6": {
        "question": "Capital of Turkey?",
        "answer": "Istanbul"
    },
    "question 7": {
        "question": "Capital of England?",
        "answer": "London"
    },
    "question 8": {
        "question": "Capital of America?",
        "answer": "Washington"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer (Enter S to skip): ')

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print('Score = ', score)

    elif answer.lower() == 's':
        score = score + 0

    else: 
        print('Wrong Answer')
        print('Correct Answer is: ', value['answer'])
        if score >= 0.25:
            score = score - 0.25
        print('Score = ', score)

print('Final Score = ', score)
print('Percentage: ', (score*100)/8)