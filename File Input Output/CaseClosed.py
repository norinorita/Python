with open("text.txt", "w") as my_file:
    my_file.write("I'm going to Canada!")

if my_file.closed == False:
    my_file.close()

print my_file.closed
