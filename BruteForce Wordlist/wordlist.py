import os
import string
from itertools import product

character = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

min_len = int(input("Enter min length of pass:"))
max_len = int(input("Enter max length of pass:"))

create_new_file = input("Do you want to create a new wordlist file? ( ͡❛ ͜ʖ ͡❛) (yes/no): ")

if create_new_file.lower() == "yes":
    # Specify the directory path where you want to create the file
    directory_path = r"C:\Users\ROG\Desktop\All Work\Python\Python Projects\BruteForce Wordlist"  #เปลี่ยนpathได้here!
    file_path = os.path.join(directory_path, "wordlist.txt")

    if not os.path.exists(file_path):
        with open(file_path, "w") as file_open:
            counter = 0
            for i in range(min_len, max_len + 1):
                for j in product(character, repeat=i):
                    word = "".join(j)
                    file_open.write(word)
                    file_open.write('.\n')
                    counter += 1
        
        print("Wordlist of {} passwords created in 'wordlist.txt'.".format(counter))
    else:
        print("File 'wordlist.txt' already exists in the directory.")
else:
    print("No new file created na kub.")