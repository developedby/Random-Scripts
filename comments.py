# comments.py - function for creating annoying unnoriginal comments
# inspired by annoying youtube comments

# prints a snake-like, ladder-like, triangle wake-like repetition of a message
def snake(message, period=10, indentation=1, n_cycles=1):
    for i in range(n_cycles):
        for j in range(period):
            if j < period/2:
                print(' '*j + message)
            else:
                print(' '*(period-j) + message)
    print(message)

# prints pyramids (a horizontal A shape) or reverse pyramids (a horizontal V shape) with the letters from the message
# each line one more letter is shown or ommited
def pyramid(message, n_cycles=1, order="small to big"):
    if order.lower() == "small to big":
        for cycle in range(n_cycles):
            for i in range(1, len(message)+1):
                print(message[:i])
            for i in reversed(range(2, len(message))):
                print(message[:i])
        print(message[0])
    elif order.lower() == "big to small":
        for cycle in range(n_cycles):
            for i in reversed(range(1, len(message)+1)):
                print(message[:i])
            for i in range(2, len(message)):
                print(message[:i])
        print(message)
    else:
        print("Parameter 'order' must be either \"small to big\" or \"big to small\"")