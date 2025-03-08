import sys

def main():
    n = int(input())
    names = []
    for _ in range(n):
        names.append(input())

    for name in names:
        print(f"Hello, {name}!")
    



if __name__ == "__main__":
    main()
