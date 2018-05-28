# Read in 1st 30
TESTSIZE = 30
ENDFLAG = '999'
scoreFile = open("scores.txt", 'r')
firstLine = True
CORRECT = 1
WRONG = -1
NOANSWER = "x"
GETCORRECTANSWER = 0
GETSTUDENTANSWER = 1
GETSTUDENTID = 0

for line in scoreFile:
    marks = 0

    if firstLine:
        correctAnswers = line.strip().split(" ")
        if correctAnswers[GETSTUDENTID] == ENDFLAG: break
        firstLine = False
    else:
        studentScore = line.strip().split(" ")
        if studentScore[GETSTUDENTID] == ENDFLAG: break
        studentId = studentScore[GETSTUDENTID]
        # create a tuple of (Correct answer, student answer)
        result = list(zip(correctAnswers, studentScore[1:]))
        for i in range(TESTSIZE):
            if result[i][GETCORRECTANSWER] == result[i][GETSTUDENTANSWER]:
                marks += CORRECT
            elif result[i][GETCORRECTANSWER] != result[i][GETSTUDENTANSWER] and result[i][GETSTUDENTANSWER] != NOANSWER:
                marks -= WRONG
        print(studentId, marks, "marks")
scoreFile.close()
