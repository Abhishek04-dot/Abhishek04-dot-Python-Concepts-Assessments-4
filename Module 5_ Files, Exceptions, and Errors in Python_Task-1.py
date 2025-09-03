try:
    file1 = open('sample.txt','r+')
    Reading = file1.read()
    file1.close()
    print(Reading)
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")
