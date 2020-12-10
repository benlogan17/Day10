import math

class Day10:
    def puzzel1(self):
        f = open("adapters.txt", "r")
        line = f.readline()
        list = []
        while line:
            list.append(int(line))
            line = f.readline()

        diffOne = 0
        diffThree = 0
        diffTwo = 0
        list.sort()
        list.insert(0, 0)
        for i in range(1,len(list)):
            if list[i] - list[i-1] == 3:
                diffThree += 1
            elif list[i] - list[i-1] == 1:
                diffOne += 1
            else:
                diffTwo += 1
        diffThree += 1
        print(diffThree * diffOne)
    def puzzel2(self):
        f = open("adapters.txt", "r")
        line = f.readline()
        list = []
        while line:
            list.append(int(line))
            line = f.readline()
        list.sort()

        diffs = []
        for i in range(1,len(list)):
            diffs.append(list[i] - list[i-1])

        probs = self.splitList(diffs)
        number = 1
        for i in probs:
            if len(i) == 1:
                number *= 2
            elif len(i) == 2:
                number *= 4
            elif len(i) == 3:
                number *= 7
        print(number)
    def splitList(self, list):
        newList = []
        temp = []
        i = 0
        while i < len(list):
            if i >= 90:
                here = 0
            if list[i:i + 2] == [3, 1]:
                if len(temp) > 0:
                    newList.append(temp)
                temp = []
                i += 1
            elif list[i] == 1:
                temp.append(1)
            elif list[i] == 3:
                if len(temp) > 0:
                    newList.append(temp)
                temp = []
            if len(temp) == 3:
                newList.append(temp)
                temp = []
                if i < len(list) - 1:
                    if list[i + 1] == 1:
                        i += 1
            i += 1
        if len(temp) > 0:
            newList.append(temp)
        return newList



day10 = Day10()
day10.puzzel2()