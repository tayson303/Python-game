import random, sys, pprint
from questions import questionSet


print("Welcome in 'Who Wants To Be a Millionaire' - NBA & Basketball Edition!")
print(" ")
print("If you want to use the lifeline just write its number - have fun & good luck!")
print("WARNING - YOU CAN USE ONLY 1 LIFELINE PER QUESTION! - (updates soon! :D )")
print(" ")

"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

awards = ['500', '1 000', '2 000', '5 000', '10 000', '20 000', '40 000', '75 000', '125 000', '250 000', '500 000', '1 000 000', "xxx"]
lifeLines = {1: "Ask the expert", 2: "50/50", 3: "Ask the audience"}
possibleAnswers = ["a", "b", "c", "d","A", "B", "C", "D", "1", "2", "3" ]
usedLifelines = []
expertTalk = ["I am almost sure it's: ", "I guess it's answer: ", "I dont know, but if I were you I would choose... ", "I am completely sure it's answer: "]
numberOfQuestions = 0

while True:
    print("Here comes the question for", awards[0], "zł!")
    print(" ")
    print("Lifelines left:", lifeLines)
    print(" ")

    if numberOfQuestions < 12:
        randomQuestion = random.choice(questionSet)
        question = randomQuestion["question"]
        answers = (randomQuestion["A"], randomQuestion["B"], randomQuestion["C"], randomQuestion["D"])
        rightAnswer = randomQuestion["rightAnswer"]

    elif numberOfQuestions == 12:
        print("Congratulations - you won a 1 million of PLN!")
        sys.exit()

    print("Im reading the question...")
    print(" ")
    print(question)
    for answer_option in answers:
        print(answer_option)
    print(" ")

    userAnswer = input("Your answer is: ")
    answer = userAnswer.capitalize()

    if answer == rightAnswer:
        print("Congratulations, you won", awards[0], "PLN!")
        print(" ")
        awards.remove(awards[0])
        questionSet.remove(randomQuestion)
        numberOfQuestions += 1
    elif answer == "4":
        pprint.pprint(questionSet)
    elif answer not in possibleAnswers:
        userAnswer = input("There is no such answer. Choose your answer CORRECTLY: ")
        answer = userAnswer.capitalize()
        if answer == rightAnswer:
            print("Congratulations, you won", awards[0], "PLN!")
            print(" ")
            awards.remove(awards[0])
            questionSet.remove(randomQuestion)
            numberOfQuestions += 1
        else:
            print("Unfortunately it is the wrong answer. The right answer is: ", rightAnswer)
            sys.exit()
    elif answer == "3" and "Ask the audience" in usedLifelines:
        userAnswer = input("Unfortunately you used that lifeline. Choose your answer (A, B, C or D): ")
        answer = userAnswer.capitalize()
        if answer == rightAnswer:
            print("Congratulations, you won", awards[0], "PLN!")
            print(" ")
            awards.remove(awards[0])
            questionSet.remove(randomQuestion)
            numberOfQuestions += 1
        else:
            print("Unfortunately it is the wrong answer. The right answer is: ", rightAnswer)
            sys.exit()
    elif answer == "3":
        lifelineAudience = randomQuestion["lifelineAudience"]
        print("The lifeline you have chosen is:", lifeLines[3])
        print(" ")
        print("Here are the results of the audience voting: ")
        print(lifelineAudience)
        print(" ")
        usedLifelines.append("Ask the audience")
        del (lifeLines[3])

        userAnswer = input("Your answer is: ")
        answer = userAnswer.capitalize()
        if answer == rightAnswer:
            print("Congratulations, you won", awards[0], "PLN!")
            print(" ")
            awards.remove(awards[0])
            questionSet.remove(randomQuestion)
            numberOfQuestions += 1
        else:
            print("Unfortunately it is the wrong answer. The right answer is: ", rightAnswer)
            sys.exit()

    elif answer == "2" and "50/50" in usedLifelines:
        userAnswer = input("Unfortunately you used that lifeline. Choose your answer (A, B, C or D): ")
        answer = userAnswer.capitalize()
        if answer == rightAnswer:
            print("Congratulations, you won", awards[0], "PLN!")
            print(" ")
            awards.remove(awards[0])
            questionSet.remove(randomQuestion)
            numberOfQuestions += 1
        else:
            print("Unfortunately it is the wrong answer. The right answer is: ", rightAnswer)
            sys.exit()
    elif answer == "2":
        answers = [letter for letter in ["A", "B", "C", "D"]
                    if letter != randomQuestion["rightAnswer"]]
        correct_answer = randomQuestion["rightAnswer"]
        wrong_answer = random.choice(answers)
        results = [randomQuestion[correct_answer],
                    randomQuestion[wrong_answer]]
        fiftyFifty = sorted(results)
        print("The lifeline you have chosen is:", lifeLines[2])
        print(" ")
        del (lifeLines[2])
        usedLifelines.append("50/50")
        for options in fiftyFifty:
            print(options)
        print(" ")

        userAnswer = input("Your answer is: ")
        answer = userAnswer.capitalize()
        if answer == rightAnswer:
            print("Congratulations, you won", awards[0], "PLN!")
            print(" ")
            awards.remove(awards[0])
            questionSet.remove(randomQuestion)
            numberOfQuestions += 1
        else:
            print("Unfortunately it is the wrong answer. The right answer is: ", rightAnswer)
            sys.exit()
    elif answer == "1" and "Ask the expert" in usedLifelines:
        userAnswer = input("Unfortunately you used that lifeline. Choose your answer (A, B, C or D): ")
        answer = userAnswer.capitalize()
        if answer == rightAnswer:
            print("Congratulations, you won", awards[0], "PLN!")
            print(" ")
            awards.remove(awards[0])
            questionSet.remove(randomQuestion)
            numberOfQuestions += 1
        else:
            print("Unfortunately it is the wrong answer. The right answer is: ", rightAnswer)
            sys.exit()
    elif answer == "1":
        print("The lifeline you have chosen is:", lifeLines[1])
        print(" ")

        usedLifelines.append("Ask the expert")
        del (lifeLines[1])

        answers = [letter for letter in ["A", "B", "C", "D"]
                   if letter != randomQuestion["rightAnswer"]]
        correct_answer = randomQuestion["rightAnswer"]
        wrong_answer = random.choice(answers)
        results = [randomQuestion[correct_answer],
                   randomQuestion[wrong_answer]]
        expert = random.choice(expertTalk)

        if numberOfQuestions < 4:
            expertChoice = random.choices(results, weights=[9, 1], k=1)
            print(expert, expertChoice)
        elif numberOfQuestions >= 4 and numberOfQuestions < 8:
            expertChoice = random.choices(results, weights=[6, 4], k=1)
            print(expert, expertChoice)
        elif numberOfQuestions >= 8 and numberOfQuestions:
            expertChoice = random.choices(results, weights=[4, 6], k=1)
            print(expert, expertChoice)

        userAnswer = input("Your answer is: ")
        answer = userAnswer.capitalize()

        if answer == rightAnswer:
            print("Congratulations, you won", awards[0], "PLN!")
            print(" ")
            awards.remove(awards[0])
            questionSet.remove(randomQuestion)
            numberOfQuestions += 1
        else:
            print("Unfortunately it is the wrong answer. The right answer is: ", rightAnswer)
            sys.exit()
    else:
        print("Unfortunately it is the wrong answer. The right answer is: ", rightAnswer)
        sys.exit()
