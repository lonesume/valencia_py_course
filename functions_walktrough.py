def getInput():
    scores = []
    score = int(input("Can you please enter a score. (-1 to exit): "))

    while score != -1:
        while score < 0 or score > 300:
            score = int(input("Can you please enter a valid score.(0-300)"))
        scores.append(score)
        print(f"Score: {score} accepted")
        score = int(input("Can you please enter another score.(-1 to exit): "))
    return scores


def getAverage(scores):
    average = sum(scores) / len(scores)
    return average


def displayResults(scores, average):
    print("You Bowled The follwing scores")
    for s in scores:
        print(str(s))
    print("your bowling average is {:.0f}".format(average))


bowlingScores = getInput()
average = getAverage(bowlingScores)
displayResults(bowlingScores, average)
