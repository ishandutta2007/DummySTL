with open("files.txt") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        line = line.replace("\n", "")
        try:
            with open(line, "w") as f:
                f.write("//dummy file " + line)
        except Exception as e:
            print(e)
        line = line.replace(".h", "")
        try:
            with open(line, "w") as f:
                f.write("//dummy file " + line)
        except Exception as e:
            print(e)
