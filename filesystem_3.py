
#Directory class
# holds a name, a header directory node, a list of directorys, and a list of fileNames
class Directory:

    def __init__(self, name):
        self.name = name
        self.subDirs = []
        self.headDir = None
        self.files = []

    #sets the header for new directories
    #I avoided this in the constructor for the home directory edge case
    def setHeader(self, newHead):
        self.headDir = newHead

    #makes a new directory
    #creates the direcotry, sets the current directory as a header, and appends to list of sub directorys
    def mkdir(self, newName):
        newDir = Directory(newName)
        newDir.setHeader(self)
        self.subDirs.append(newDir)

    #lists all directories and file
    #concatinates all directory and filenames to a string, the prints the string
    def ls(self):
        dirList = ""

        for dir in self.subDirs:
            dirList += dir.name + " "

        for file in self.files:
            dirList += file + " "

        print(dirList)


    #changes the direcotry
    #returns either the disired directory, or the current directory
    def cd(self, dirName, curDir):

        #parent direcotry
        if dirName == "..":
            return self.headDir


        isDirectory = False
        iterator = 0

        #iterates through all sub directories
        #checks if the sub directory exists
        while not isDirectory and iterator < len(self.subDirs):
            if self.subDirs[iterator].name == dirName:
                isDirectory = True
            else:
                iterator += 1

        #returns the directory if it exists, returns current if it does not
        if not isDirectory:
            print("No such directory exists")
            return curDir
        else:
            return self.subDirs[iterator]

    #creates a list of files by name
    #takes the entire userinput, splits up the words, and removes the first word touch
    #the split list is then appended to list of filenames
    def touch(self, fileNames):
        newFiles = fileNames.split()
        newFiles.pop(0)
        self.files.extend(newFiles)

    #recursivvely lists a directory tree
    #returns the directory string
    def getTree(self):
        treeName = "/" + self.name

        if self.headDir == None:
            return self.name
        else:
            treeName = self.headDir.getTree() + treeName

        return treeName


def main():

    #Create home directory
    curDir = Directory("home")

    userInput = ""

    #loops until user ends program
    while userInput != "exit":
        userInput = input(curDir.getTree() + ">>")
        userList = userInput.split()
        # I wanted to use a switch here
        # but it would run through all the code anyway
        # making a switch entirely useless sadly

        if (len(userList) > 1 and userList[0] == "mkdir"):
            curDir.mkdir(userList[1])

        elif (len(userList) > 1 and userList[0] == "cd"):
            curDir = curDir.cd(userList[1], curDir)

        elif (len(userList) > 1 and userList[0] == "touch"):
            curDir.touch(userInput)

        elif (userInput == "ls"):
            curDir.ls()

        elif (userInput == "exit"):
            print("Goodbye!")

        elif (userInput == ""):
            print("")
        else:
            print("Could not find command " + userList[0] + " in context.")


if __name__ == "__main__":
        main()
