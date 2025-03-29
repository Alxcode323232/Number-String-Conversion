class Conversion:
    def __init__(self):
        self.numDict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, 
            "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eightteen":18, "nineteen":19, "twenty":20,
            "thirty":30, "fourty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90, "hundred":100,
            "thousand":1000, "million":1000000, "billion":1000000000
            }
        self.hundreds = ["hundred", "thousand", "million", "billion"]
        pass
    def convertToNum(self):
        string = self.string
        string = string.lower()
        strList = string.split()
        answer = 0
        i = 0
        while i < len(strList):
            if strList[i] not in self.hundreds:
                subAnswer = self.numDict[strList[i]]
                k = i + 1
                while k < len(strList):
                    if strList[k % len(strList)] not in self.hundreds and strList[k - 1] in self.hundreds:
                        break
                    elif strList[k % len(strList)] not in self.hundreds and strList[k - 1] not in self.hundreds:
                        subAnswer += self.numDict[strList[k]]
                        i += 1
                    else:
                        subAnswer *= self.numDict[strList[k]]
                    k += 1
                answer += subAnswer
            i += 1
        return answer
