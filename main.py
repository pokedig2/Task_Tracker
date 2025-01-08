# Goal of project is to create a fully functional task tracker - Destin
# Check for JSON file, if does not exist generate new JSON file
list = open("tasks.json", "w")
data = {

}

#create perpetual running to send commands to list application
run = True
while run:
    temp = input()
    if temp == "exit":
        print("Exiting...")
        run = False