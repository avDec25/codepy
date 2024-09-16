from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []

        for log in logs:
            log = log.split(' ')
            key = log[0]
            log = log[1:]

            if log[0].isdigit():
                digit.append(key + " " + " ".join(log))
            else:
                letter.append((" ".join(log), key))

        letter.sort()
        logs = []
        for log, key in letter:
            logs.append(key + " " + log)

        return logs + digit


logs = ["dig1 8 1 5 1", "let1 art zero can", "dig2 3 6", "let2 own kit dig",
        "let3 art zero"]
print(Solution().reorderLogFiles(logs))
