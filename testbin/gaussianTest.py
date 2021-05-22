import random

if __name__ == '__main__':
    sample_size = 100
    count = 0

    pos = 0
    neg = 0
    zero = 0

    s_space = []

    while count < sample_size:
        rand = round(random.gauss(0, 12))
        s_space.append(rand)

        if rand > 0:
            pos += 1
        elif rand < 0:
            neg += 1
        else:
            zero += 1

        count += 1

    print(f"Sample Size: {sample_size}:\n{s_space}\nPositive Count: {pos}\nNegative Count: {neg}\nZero Count: {zero}")