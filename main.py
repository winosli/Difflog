# put in the same file 2 log files (txt format) and the script will create a new txt file with all the different between the files
# The script ignores the time on each line and display
import glob, os

# Find 2 logs in this folder
counter_files = 0
nameFile1 = None # File 1
nameFile2 = None # File 2
for file in glob.glob("*.txt"):
    if "result" not in file and "lines_only_in_" not in file:
        counter_files += 1
        if counter_files == 1:
            nameFile1 = file
        elif counter_files == 2:
            nameFile2 = file
        print(file)
print('Total txt files: ' + str(counter_files))
if counter_files != 2:
    print('[-] Please put exactly 2 txt files in order to compare between them (without the "result" word)')
    exit()

# Read the files and check if some sentences existing in 1 file and not in the other one
print("---")

# Split the content of file 1 to groups of 4 words and check if it exists in the other file
lines_1 = None
lines_2 = None

with open(nameFile1, encoding="utf8", errors='ignore') as f:
    lines_1 = f.readlines()
   # print(lines_1)

with open(nameFile2, encoding="utf8", errors='ignore') as f:
    lines_2 = f.readlines()
    # print(lines_2)



def checkDiff(content_1, content_2, fileName):
    counter_diff = 0
    offset = 32 # Use 32 for android logs (to ignore the date and the time)
    offset = 0
    f = open(fileName, "a")
    print("*******")
    for line in content_1:  # Check if line exist in lines_2
        line_without_time = line[offset:]  # Starting from character 30 to avoid the data and the time
        is_exist = False
        try:
            for element in content_2:
                if line_without_time in element:
                    is_exist = True
            if is_exist == False:
                is_ok = False
                if white_keywords != None:
                    for white in white_keywords:
                        if white in line:
                            is_ok = True

                if black_keywords != None:
                    for black in black_keywords:
                        if black in line:
                            is_ok = False

                if white_keywords == None and black_keywords == None:
                    is_ok = True

                if is_ok:
                    print("--- ")
                    counter_diff += 1
                    print("Different: " + str(counter_diff))
                    print(line)
                    f.write(line)
        except KeyboardInterrupt as ex:
            print("Exception occur: " + str(ex))

    f.close()


# Use black and white keywords for filtering
# black_keywords = ["wifi"]
# white_keywords = ["error", "exception"]
black_keywords = None
white_keywords = None

print("\n[+] These lines do not exist in txt file " + nameFile2 + " and exist in " + nameFile1 + "\n")
checkDiff(content_1=lines_1, content_2=lines_2, fileName="lines_only_in_" + nameFile1)
print("\n[+] These lines do not exist in txt file " + nameFile1 + " and exist in " + nameFile2 + "\n")
checkDiff(content_1=lines_2, content_2=lines_1, fileName="lines_only_in_" + nameFile2)

# print all of that inside a new txt file..
