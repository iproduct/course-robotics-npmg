
def find_count(substring, string):
    counter = 0
    index = string.find(substring)
    while index >= 0:
        counter += 1
        index = string.find(substring, index + 1)
    return counter

if __name__ == "__main__":
    """main script"""
    with open("read_write_file.py", "rt") as f: # read file with automatic closing
        with open("comments.txt", "wt") as out:
            for line in f: # read one line
                start_of_comment = line.find("#")
                str_start = line[:start_of_comment]
                quote_count = find_count("'", str_start)
                double_quote_count = find_count('"', str_start)
                find_count('"', str_start) % 2 == 0
                if start_of_comment > 0 and quote_count % 2 == 0 and double_quote_count % 2 == 0:
                    comment = line[start_of_comment:] # get comment only string
                    print(comment, end="") # print comment
                    out.write(line) # write to file
