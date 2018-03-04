import json

# writes a simple log file with entries. Creates the file if it does not exist or appends the log if it does exist
def write_file(file, text):
    try:
        f = open(file, "a+")
        f.write(text + "\n")
        f.close()
        return True
    except:
        print("Error creating/writing the file " + file)
        return False

# writes a simple log file with JSONentries.
# Creates the file if it does not exist or appends the log if it does exist
def write_file_json(file, jobject):
    try:
        with open(file, 'a+') as outfile:
            json.dump(jobject, outfile, ensure_ascii=False)
            outfile.write("\n")
            outfile.close()
            return True
    except:
        print("Error creating/writing the file " + file)
        return False





