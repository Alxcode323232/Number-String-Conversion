numDict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, 
            "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eightteen":18, "nineteen":19, "twenty":20,
            "thirty":30, "fourty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90, "hundred":100,
            "thousand":1000, "million":1000000, "billion":1000000000
            }
hundreds = ["hundred", "thousand", "million", "billion"]

def convertNum(string, stringToNum):
    string = string.lower()
    strList = string.split()

    
    answer = 0
    i = 0
    #You can uncomment comments to see how the code is working
    #print(strList)
    while i < len(strList):
        if strList[i] not in hundreds:
            subAnswer = numDict[strList[i]]
            k = i + 1
            #print("SubAnswer:", subAnswer)
            while k < len(strList):
                if strList[k % len(strList)] not in hundreds and strList[k - 1] in hundreds:
                    break
                elif strList[k % len(strList)] not in hundreds and strList[k - 1] not in hundreds:
                    subAnswer += numDict[strList[k]]
                    i += 1
                else:
                    subAnswer *= numDict[strList[k]]
                #print("SubAnswer:", subAnswer, "k:", k)
                k += 1
            #print(answer, ' + ', subAnswer)
            answer += subAnswer
        i += 1
    return answer
stringToNum = True
string = input("Enter a string: ")
print(convertNum(string, stringToNum))