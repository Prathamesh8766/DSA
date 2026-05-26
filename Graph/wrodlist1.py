from queue import Queue
def wordList1(beginWord, end,wordList):
    q = Queue()
    q.put([beginWord,1])
    if beginWord in wordList:
        wordList.remove(beginWord)
    while not q.empty():
        current, level = q.get()
        for i in range(len(current)):

            for ch in range(ord('a'), ord('z') + 1):

                new_char = chr(ch)

                new_word = current[:i] + new_char + current[i+1:]

                if new_word == end and new_word in wordList:
                    return level+1 
                if new_word in wordList:
                    q.put([new_word,level+1])
                    wordList.remove(new_word)
    return 0
                
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

print(wordList1(beginWord,endWord,wordList))

def optimizedWordList1(beginWord, endWord, wordList):

    wordSet = set(wordList)

    if endWord not in wordSet:
        return 0

    q = Queue()
    q.put((beginWord, 1))

    while not q.empty():

        current, level = q.get()

        if current == endWord:
            return level

        for i in range(len(current)):

            for ch in range(ord('a'), ord('z') + 1):

                new_word = ( current[:i] + chr(ch) + current[i+1:]
                )

                if new_word in wordSet:

                    q.put((new_word, level + 1))
                    wordSet.remove(new_word)

    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(optimizedWordList1(beginWord, endWord, wordList))