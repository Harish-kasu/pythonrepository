# python quiz game

questions = (
    "how many elements are in periodic table?", 
    "which animal lays the largest eggs?", 
    "what is the most abundant gas in earth's atmosphere?", 
    "how many bones are in human body?",
    "which planet in the solar system is the hottest"
)
options = (
    ("A. 118", "B. 108", "C. 128", "D. 98"),
    ("A. ostrich", "B. whale", "C. elephant", "D. giraffe"),
    ("A. oxygen", "B. nitrogen", "C. carbon dioxide", "D. argon"),
    ("A. 206", "B. 208", "C. 210", "D. 212"),
    ("A. mercury", "B. venus", "C. earth", "D. mars")
)

answers = ("A", "A", "B", "A", "B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("guess the option (A,B,C,D):").upper()

    guesses.append(guess)
    if guess == answers[question_num]:
        print("correct")
        score += 1
    else:
        print("incorrect")
        print(f" the correct answer is {answers[question_num]}")
    question_num += 1

print("-----------------------------")
print("RESULTS")
print("-----------------------------")
print(f"your guesses are : {guesses}", end =" ")
print(f" answers are : {answers}",end = " ")

print(f"your score is: {(score/len(answers))*100} %")

      