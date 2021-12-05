import os

def main():

    sonar_array = []
    increases_1 = 0
    increases_2 = 0

    with open('sonar.txt', 'r') as f:
        lines = f.readlines()
        for x in lines:
            sonar_array.append(int(x))
        f.close()
    
    # Part 1
    # Number of increases
    for x in range(len(sonar_array[1:])):
        if x > 0 and sonar_array[x] > sonar_array[x-1]:
            increases_1 += 1
    print(increases_1)


    # Part 2
    # 3bies
    for x in range(len(sonar_array)):
        if x>=3 and sonar_array[x]+sonar_array[x-1]+sonar_array[x-2] > sonar_array[x-1]+sonar_array[x-2]+sonar_array[x-3]:
            increases_2 += 1
    print(increases_2)

if __name__ == "__main__":
    main()
