with open("files.txt") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        line = line.replace("\n", "")
        with open(line, "w") as f:
            f.write("//dummy file " + line)
