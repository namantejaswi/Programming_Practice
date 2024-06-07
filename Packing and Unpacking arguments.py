

if __name__ == "__main__":
    def display(a, b, c) -> None:
        print(a)
        print(b)
        print(c)


    arr = [4, 5, 6]
    display(*arr)

    lis = [3, 7, 8]


    def show(*arguments) -> None:
        print(*arguments)
        ar = list(arguments)
        print(ar)


    show(lis)
