import subprocess
import os

print("**ShortCommands**\n")

print ("list cmd = searches for processes with cmdline")
print ("kill cmd = kills chosen process with cmdline\n")
print ("list pwsh = searches for processes with powershell")
print ("kill pwsh = kills chosen process with powershell\n")
print ("net = searches for IP´s connected to network\n")
print ("clear = clears the terminal\n")

Entry = input("Press any Button to continue...\n")

while Entry != "exit":

    x = input("\nType:")
    
    if x == "list cmd":
    
        print("\n**Commandline**")
        os.system("cmd /c tasklist") #/k= executes and remains open, /c= executes and closes shell
        
    elif x == "kill cmd":
    
        kill = input("\nWhich process?")
    
        print("\n**Commandline**")
        os.system("cmd /c taskkill /F /PID " + kill + ".exe")
        
        
    elif x == "list pwsh":
    
        print("\n**Powershell**")
        os.system("powershell -c get-process") #-c =executes in commandline, start= executes in own shell
    
    elif x == "kill pwsh":
    
        kill = input("\nWhich process?")

        print("\n**Powershell**")
        os.system("powershell -c stop-process -name: " + kill)
        
    elif x == "net":
    
        print("\n**Powershell**")
        os.system("powershell get-netneighbor")
        
    elif x == "clear":
    
        os.system("cls")
        
        print("**Shortcut Commands**\n")

        print ("list cmd = searches for processes with cmdline")
        print ("kill cmd = kills chosen process with cmdline\n")
        print ("list pwsh = searches for processes with powershell")
        print ("kill pwsh = kills chosen process with powershell\n")
        print ("net = searches for IP´s connected to network\n")
        print ("clear = clears the terminal\n")
        
        
    elif x == "exit":
    
        break
        
    else:
    
        print("\nError")
    
                  
print("\nGoodbye!")

input()

