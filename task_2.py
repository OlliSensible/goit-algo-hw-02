from collections import deque
import re

def is_palindrome(string):
    string = string.lower()
    string = re.sub(r"[^\w\s]", "", string) 
    queue = deque(string)
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

print(is_palindrome("тут")) 
print(is_palindrome("madam"))
print(is_palindrome("Дід і дід"))
print(is_palindrome("Паліндром"))
