try:
    file_content = input("Enter text to write to the file: ")
    if file_content.isdigit():
        file_content = ''
    file1 = open('output.txt', "r+")
    if file_content != '':
        writing_file = file1.write(file_content + "\n")
    else:
       writing_file = file1.write(file_content)
    file1.close()
    print('Data successfully written to output.txt.')
    file1.close()
    append_text = input("Enter text to append to the file: ")
    file1 = open('output.txt', "a")
    append_file = file1.write(append_text)
    print('Data successfully appended')
    file1.close()
    file1 = open('output.txt', "r+")
    reading_file = file1.read()
    file1.close()
    print('Final content of the output:' + '\n' + reading_file)

except FileNotFoundError:
    print("The file 'output.txt' was not found.")