import random

class Set: # Point with name in tree that the nodes conect
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.upperNeighbours = []
        self.lowerNeighbours = []
    
    def printSet(self):
        print()
        print("Set: ")
        print("ID: " + str(self.ID))
        print("name: " + str(self.name))
        print("upperNeighbours:")
        print(self.upperNeighbours)
        print("lowerNeighbours:")
        print(self.lowerNeighbours)
        print()

def setup(fileName): #makes arr2D of the txt file and sets that are conected with nodes
    #rewrites the file into 2D array spliting by 4 spaces
    with open(fileName, "r") as file:
        arr2D = []
        indexOfLastLineLength1 = 0
        for i, line in enumerate(file):
            line = line.split("    ")
            line[-1] = line[-1][:-1]
            if len(line) == 1:
                indexOfLastLineLength1 = i
            arr2D.append(list(line))

    #delete all comment lines (first lines of the txt file)
    arr2D = arr2D[indexOfLastLineLength1:-1]

    #print(arr2D)

    #make list of nodes
    nodesList = []
    for i, line in enumerate(arr2D):
        if len(line) > 1:
            y = i - 1
            while len(arr2D[y]) != len(line) - 1:
                y -= 1
            nodesList.append([arr2D[y][-1], line[-1]])
    
    #print(nodesList)

    #remove duplicats
    nodesList = list(set(tuple(row) for row in nodesList))

    #print(nodesList)

    setNames = []
    for line in arr2D:
        setNames.append(line[-1])
        #print(line[-1])

    setNames_noRepeantings = []
    for set_ in setNames:
        if set_ not in setNames_noRepeantings:
            setNames_noRepeantings.append(set_)
    setNames = setNames_noRepeantings

    #print(setNames)

    setsList = {}
    for id, setName in enumerate(setNames):
        setsList[setName] = Set(setName, id)
        #print(id)

    for node in nodesList:
        setsList[node[0]].lowerNeighbours.append(node[1])
        setsList[node[1]].upperNeighbours.append(node[0])

    return setsList

def findSetWithID(setsList, ID):
    for set_ in setsList.values():
        if int(set_.ID) == int(ID):
            return set_
    return "X"

def loop(setsList):
    inputTextID = 0
    history = []
    while inputTextID != "X":
        if inputTextID == "<<":
            if len(history) == 1:
                break
            history.pop()
            print("History:")
            print("[ID | text]")
            for id in history:
                print(str(id) + " | " + findSetWithID(setsList, id).name)
            print("____________")
        else:
            history.append(inputTextID)
            print("History:")
            print("[ID | text]")
            for id in history:
                print(str(id) + " | " + findSetWithID(setsList, id).name)
            print("____________")
        set_ = findSetWithID(setsList, history[-1])
        #set_.printSet()
        
        print("upper nodes:")
        print("[ID | text]")
        for neighbour in set_.upperNeighbours:
            print(str(setsList[neighbour].ID) + " | " + neighbour)
        print("\nnode that you currently in:")
        print(set_.name)
        print("\nlower nodes:")
        print("[dice | ID | text]")
        for i, neighbour in enumerate(set_.lowerNeighbours):
            print(str(i+1) + " | " + str(setsList[neighbour].ID) + " | " + neighbour)
        print("\n(roll dice K" + str(i+1) + " or higher to randomise the node)")
        print("(if you roll to big number roll again)")
        randomK = random.randint(1,i+1)
        print("Dice throw simulation outputed: " + str(randomK))
        
        print("________________________________________________________________________")
        inputTextID = input("Write the id of node you want to enter (\"X\" to close or \"<<\" to go back in the history):")

def main():
    inputText = input("Input the name of the tree txt file you want to enter(or \"X\" to close): ")
    while inputText != "X":
        loop(setup(inputText))
        print("==================")
        inputText = input("Input the name of the tree txt file you want to enter(or \"X\" to close): ")
    print("The program has turned off. You can close the console/window")

main()
