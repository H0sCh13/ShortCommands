import subprocess
import os

#Docstrings used with help command

def cmd():
    """ start cmd = Starts given process with Cmdline by using the [start] command.
        list cmd = searches for running processes with Cmdline by using the [tasklist] command.
        kill cmd = kills chosen process with Cmdline by using the [taskkill] command. """
        
    
def pwsh():
    """ start pwsh = starts chosen process with Powershell by using the [start-process] command.
        list pwsh = searches for running processes with Powershell by using the [get-process] command.
        kill pwsh = kills chosen process with Powershell by using the [stop-process] command. """
        
        
def net():   
    """ net = Shows all connections to current system with Powershell by using the [get-netneighbor] command. """   
    
def clear():

    """ clear = Clears the Terminal from all written Text by using the [cls] command to start all over again. """

    
#Keyword examples and Introduction

print("**ShortCommands**\n")

print ("start [cmd] = starts chosen process with cmdline")
print ("list [cmd] = searches for processes with cmdline")
print ("kill [cmd] = kills chosen process with cmdline\n")

print ("start [pwsh] = starts chosen process with powershell")
print ("list [pwsh] = searches for processes with powershell")
print ("kill [pwsh] = kills chosen process with powershell\n")

print ("[net] = searches for IP´s connected to network")
print ("[clear] = clears the terminal\n")

print ("help [KEYWORD] = Gives additional information about chosen command\n")


#Loop-Start

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
        
    elif x == "start cmd":
        
        start = input("\nWhich process?")
        
        print("\n**Commandline**")
        os.system("cmd /c start " + start + ".exe")
        
        
    elif x == "list pwsh":
    
        print("\n**Powershell**")
        os.system("powershell -c get-process") #-c =executes in commandline, start= executes in another canvas
    
    elif x == "kill pwsh":
    
        kill = input("\nWhich process?")

        print("\n**Powershell**")
        os.system("powershell -c stop-process -name: " + kill)
        
    elif x == "start pwsh":


        start = input("\nWhich process?")
        
        print("\n**Powershell**")
        os.system("powershell -c start " + start)

        
    elif x == "net":
    
        print("\n**Powershell**")
        os.system("powershell get-netneighbor")
      
        
    elif x == "help net":
    
        help(net)
       
    elif x == "help cmd":
    
        help(cmd)
        
    elif x == "help pwsh":
        
        help(pwsh)
        
    elif x == "help clear":  
    
        help(clear)
        
        
    elif x == "clear":
    
        os.system("cls")
        
        print("**Shortcut Commands**\n")

        print ("start cmd = starts chosen process with cmdline")
        print ("list cmd = searches for processes with cmdline")
        print ("kill cmd = kills chosen process with cmdline\n")

        print("start pwsh = starts chosen process with powershell")
        print ("list pwsh = searches for processes with powershell")
        print ("kill pwsh = kills chosen process with powershell\n")

        print ("net = searches for IP´s connected to network\n")
        print ("clear = clears the terminal\n")


# Loop-End
        
    elif x == "exit":
    
        break
        
    else:
    
        print("\nError")
    
                  
print("\nGoodbye!")

input()

