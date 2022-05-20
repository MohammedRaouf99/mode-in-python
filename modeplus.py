
numbers = [2, 2, 2, 2, 3, 3, 3,  3, 4, 4, 4, 4, 4,  5, 5, 5, 5]
def mode(x):

    x = 0
    v = 1
    try:
        while True:
            if len(numbers) == 1:
                z = numbers[x]
                break
            if len(numbers) == x+1:

                break

            s = (numbers.count(numbers[x]))

            if s > v:
                v = s
                z = numbers[x]

            x += 1

        return f"the mode is {z} repeated {v} times"

    except ValueError:
        return "the list is empty"


mode(numbers)
