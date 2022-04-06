

def main():
    # f = open("file.txt", "w")
    # f.write("hello\n" + 1)
    # f.close()

    with open("file.txt", "w") as f:
        f.write("Hello world\n")

    with open("file.txt", "a") as f:
        f.write("hello again\n")

    with open("file.txt", "r") as f:
        print(f.readlines())

    with open("file.txt", "r") as f:
        print(f.read())

    with open("file.txt", "r") as f:
        print(f.read(7))

    with open("demo_files.py", "r") as f:
        # print(1, f.readline())
        # print(2, f.readline())
        # print(3, f.readline())
        for line in f:
            print("line", line)
            if "open" in line:
                break


if __name__ == "__main__":
    main()
