def get_file(path):
    f = open(path, 'r')
    data = f.readlines()
    parsedData = []
    for line in data:
        parsedData.append(line.split() + [0])
    return (parsedData)
