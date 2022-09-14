class Solution:
    def sortSentence(self, s: str):
        words = s.split()
        wordsDict = {}
        outputSentence = ''
        for word in words: 
            orderNum = int(word[-1])
            wordsDict[orderNum] = word[:-1]
        for i in range(1, len(words)+1):
            currentWord = wordsDict[i]
            outputSentence += currentWord
            if i < len(words):
                outputSentence += ' '
               
        return outputSentence