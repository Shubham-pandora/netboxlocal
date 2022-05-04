with open('hostname.txt') as f:
    for line in f:
        x = line.split(" ")
        # print(x)
        # print("--------")
        print(x[0],x[1])
        print("--------")