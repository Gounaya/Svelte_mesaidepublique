with open("input.txt") as fp:
    line = fp.readline()
    commands = line.split(",")

for i in range(len(commands)):
    commands[i] = int(commands[i])
i = 0

while i < len(commands):
    if commands[i] == 1:
        commands[commands[i + 3]] = commands[commands[i + 1]] + commands[commands[i + 2]]
    elif commands[i] == 2: 
        commands[commands[i + 3]] = commands[commands[i + 1]] * commands[commands[i + 2]]
    elif commands[i] == 99:
        break;
    else:
        print("unkown opcode:" + str(commands[i]))
    i+=4
print(commands[0])
