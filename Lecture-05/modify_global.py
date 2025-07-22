counter = 7

def increment():
    global counter
    counter += 8

increment()
increment()

print(counter)