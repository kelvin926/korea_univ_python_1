def patternmatch(pattern, correctAns, wrongAns):
    
    for i in range(len(pattern)):
        print(pattern[i], end=" ")
        
    guessAns = int(input("다음 수는 무엇일까요? "))
    
    if guessAns == pattern[len(pattern)-1]:
        correctAns = correctAns + 1
        print("잘 했어요. 축하해요")
    else:
        wrongAns = wrongAns + 1
        print("정답은 %d입니다" %(pattern[len(pattern)-1]))
    return correctAns, wrongAns

correctAns = 0
wrongAns = 0

pattern1 = [2, 4, 6, 8]
pattern2 = [13, 16, 19, 22]
pattern3 = [2, 3, 5, 7, 11]
pattern4 = [1, 1, 2, 3, 5, 8]
pattern5 = [31, 28, 31, 30]

correctAns, wrongAns = patternmatch(pattern1, correctAns, wrongAns)
correctAns, wrongAns = patternmatch(pattern2, correctAns, wrongAns)
correctAns, wrongAns = patternmatch(pattern3, correctAns, wrongAns)
correctAns, wrongAns = patternmatch(pattern4, correctAns, wrongAns)
correctAns, wrongAns = patternmatch(pattern5, correctAns, wrongAns)

print("%d개 패턴 중 %d개 맞았어요" %(correctAns + wrongAns, correctAns))