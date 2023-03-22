import random

questionSet = []

while True:
    question = input("Write your question or write 'stop' to finish writing questions): ")
    if question.lower() == "stop":
        break

    answerA = input("answer A: ")
    answerB = input("answer B: ")
    answerC = input("answer C: ")
    answerD = input("answer D: ")
    rightAnswer = input("correct answer index (A=1, B=2, C=3, D=4): ")
    votes = [0, 0, 0, 0]
    correctIndex = int(rightAnswer) - 1
    remainingPercent = 100
    for i in range(3):
        vote = random.randint(1, remainingPercent)
        votes[i] = vote
        remainingPercent -= vote
    votes[correctIndex] = remainingPercent
    random.shuffle(votes)

    questionDict = {
        "question": question,
        "A": "a) " + answerA,
        "B": "b) " + answerB,
        "C": "c) " + answerC,
        "D": "d) " + answerD,
        "rightAnswer": rightAnswer,
        "lifelineAudience": f"a) {votes[0]}% b) {votes[1]}% c) {votes[2]}% d) {votes[3]}%"
    }
    questionSet.append(questionDict)

print(questionSet)
