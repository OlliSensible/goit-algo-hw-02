import queue
import random
import uuid

def generate_request_id():
    return uuid.uuid4().hex

def generate_request():
    request_id = generate_request_id()
    number = random.randint(1, 1000)
    data = f"Application №{request_id} ({number})"
    return data.lower()

def process_request(request):
    print(f"\x1b[38;2;210;88;113mProcessed request: {request}\x1b[0m")

request_queue = queue.Queue(maxsize=10)

try:
    while True:
        request = generate_request()
        request_queue.put(request)  
        process_request(request_queue.get())  
except KeyboardInterrupt:
    print("\x1b[38;2;255;0;0m\nExiting the application...\x1b[0m")