import re
import sys

class greedySort:
    def __init__(self) -> None:
        self.initialize()

    PERMUTATION = (list)

    def initialize(self):
        try:
            with open(sys.argv[1]) as file:
                lines            = file.readlines()
                # Convert strings into ints
                self.PERMUTATION = list(
                            map(
                                int,
                                lines[1].replace('(','').replace(')','').split()
                                )
                            )
                self.PERMUTATION.insert(0,0)
                self.PERMUTATION.append(len(self.PERMUTATION))
        except OSError:
            print("Could not open file " + sys.argv[1])
        except IndexError:
            print("Please enter a file name.")

    def greedySort(self):
        print(self.PERMUTATION)

    def run(self):
        self.greedySort()

if __name__ == "__main__":
    program = greedySort()
    program.run()