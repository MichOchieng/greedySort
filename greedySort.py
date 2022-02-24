import re
import sys

class greedySort:
    def __init__(self) -> None:
        self.initialize()

    PERMUTATION = (list)
    STEP_NUMBER = 0

    def initialize(self):
        try:
            with open(sys.argv[1]) as file:
                lines            = file.readlines()
                self.PERMUTATION = lines[1].replace('(','').replace(')','').split()
                # self.PERMUTATION.insert(0,0)
                # self.PERMUTATION.append(len(self.PERMUTATION))
        except OSError:
            print("Could not open file " + sys.argv[1])
        except IndexError:
            print("Please enter a file name.")

    def greedySort(self):
        n = len(self.PERMUTATION)
        for x in range(n):
            if(x != int(self.PERMUTATION[x])):
                # Find where the correct value is 
                # Reverse everything in the path up to that value
                pass

    def displayPermutation(self):
        self.STEP_NUMBER += 1
        print("(" + str(self.STEP_NUMBER) + ")", end=" ")
        for val in self.PERMUTATION:
            print(val, end=" ")

    def run(self):
        self.displayPermutation()

if __name__ == "__main__":
    program = greedySort()
    program.run()