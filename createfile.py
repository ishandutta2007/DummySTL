with open('filename') as f:
    lines = f.readlines()
    for line in lines:
    print(line)
    with open(line, 'w') as f:
        f.write('Create a new text file!')
