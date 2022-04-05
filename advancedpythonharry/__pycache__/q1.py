#write a program that will read the files and handles the error if any file is mising
def readme(filename):
    try:

        with open(filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f'file {filename} is not found')

readme("1.txt")
readme("2.txt")
readme("3.txt")

