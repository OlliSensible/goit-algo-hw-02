import queue
import random

def generate_request():
    number = random.randint(1, 1000)
    data = "Application №" + str(number)
    return data.lower()

def process_request(request):
    print(
        f"\x1b[35mProcessed application № {request}\x1b[0m"
    ) 

queue = queue.Queue()

while True:
    request = generate_request()
    queue.put(request)
    process_request(queue.get())

    answer = input(
        f"\x1b[32mContinue? (Yes/No or +/-) ==> \x1b[0m"
    ) 
    answer = answer.replace(" ", "").lower()
    while answer not in ("yes", "no", "+", "-"):
        answer = input(
            f"\x1b[31mInvalid command. Enter one of the following commands: Yes, No, +, - ==> \x1b[0m"
        ) 

    if answer in ("yes", "no", "+", "-"):
        if answer == "no" or answer == "-":
            break

    if answer == "no" or answer == "-":
        break
