from collections import deque

def search(lines, perttern, history=5):
    dev_history = deque(maxlen=history)
    for line in lines:
        if perttern in line:
            yield line, dev_history
        dev_history.append(line)


if __name__ == "__main__":
    with open("salom.txt") as f:
        for line, pre in search(f, "python", 5):
            for n in pre:
                print(n, end='')
            print(line, end='')
            print('-'*20)