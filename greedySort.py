import re
import sys

class greedySort:
    def __init__(self) -> None:
        self.initialize()

    PERMUTATION = []
    STEP_NUMBER = 0

    def initialize(self):
        try:
            with open(sys.argv[1]) as file:
                lines            = file.readlines()
                self.PERMUTATION = lines[1].replace('(','').replace(')','').split()
        except OSError:
            print("Could not open file " + sys.argv[1])
        except IndexError:
            print("Please enter a file name.")

    def greedySort(self):
        n = len(self.PERMUTATION)
        for i in range(n):
            if(i+1 != abs(int(self.PERMUTATION[i])) ):
                # Find where the correct value is
                distance = 0
                for j in self.PERMUTATION:
                    distance += 1
                    if(abs(int(j)) == (i+1)):
                        # Reverse everything in the path up to that value
                        self.PERMUTATION[i:distance] = self.PERMUTATION[i:distance][::-1]
                        # Reverse signs of values
                        for k in range(distance-i):
                            if(int(self.PERMUTATION[i+k]) < 0):
                                temp = "+" + str(abs(int(self.PERMUTATION[i+k])))
                                self.PERMUTATION[i+k] = temp
                            else:
                                temp = "-" + str(abs(int(self.PERMUTATION[i+k])))
                                self.PERMUTATION[i+k] = temp
                        self.displayPermutation()
                # Switch the sign of the number if needed
                if(int(self.PERMUTATION[i]) < 0 and abs(int(self.PERMUTATION[i])) == (i+1)):
                    temp = "+" + str(abs(int(self.PERMUTATION[i])))
                    self.PERMUTATION[i] = temp
                    self.displayPermutation()
            else:
                # If the value is in the correct position but has an incorrect sign flip the sign
                if(int(self.PERMUTATION[i]) < 0):
                    temp = "+" + str(abs(int(self.PERMUTATION[i])))
                    self.PERMUTATION[i] = temp
                    self.displayPermutation()

    def displayPermutation(self):
        self.STEP_NUMBER += 1
        print("(" + str(self.STEP_NUMBER) + ")", end=" ")
        for val in self.PERMUTATION:
            print(val, end=" ")
        print()

    def run(self):
        self.greedySort()

if __name__ == "__main__":
    program = greedySort()
    program.run()