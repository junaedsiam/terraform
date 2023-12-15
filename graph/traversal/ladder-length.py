"""
Problem description: 
---------

"""
from queue import Queue


def ladder_length(beginWord: str, endWord: str, wordList):
    # Doing BFS to find the ladder length
    s = set(wordList)

    q = Queue()
    q.put((beginWord, 1))

    s.discard(beginWord)

    while q.qsize():
        word, steps = q.get()

        if word == endWord:
            return steps

        for i in range(len(word)):
            original = word[i]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                word = word[:i] + char + word[i + 1:]
                if word in s:
                    s.discard(word)
                    q.put((word, steps + 1))

            word = word[:i] + original + word[i + 1:]

    return 0


if __name__ == '__main__':
    print(ladder_length("hit", "cog", [
          "hot", "dot", "dog", "lot", "log", "cog"]))
