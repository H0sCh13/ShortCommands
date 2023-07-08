import subprocess
import os
import shutil
from tabulate import tabulate


KeyWordTableINDEX = [["[cmd] start", "[start]", "[google]", "[clear]"],
                     ["[cmd] list", "[net]", "[youtube]", "[history]"],
                     ["[cmd] kill", "[krypt]", "[twitch]", "[exit]"],
                     ["[pwsh] start", "[copy]","", ""],
                     ["[pwsh] list", "[search]", "", ""],
                     ["[pwsh] kill", "", "", ""],
                     ["", "", "", ""]]


KeyWordCategoriesINDEX = ["Tasks/Programs", "Network", "Websites", "Miscellanous"]

#Empty List for KeyCommand

History = []

LoggingInput = []

#################################################################################################

#Docstrings: use with help command

def cmd():
    """ start = Starts given process with Cmdline by using the [start] command.

        list = Searches for running processes with Cmdline by using the [tasklist] command.

        kill = Kills chosen process with Cmdline by using the [taskkill] command. """


def pwsh():
    """ start = Starts chosen process with Powershell by using the [start-process] command.

        list = Searches for running processes with Powershell by using the [get-process] command.

        kill = Kills chosen process with Powershell by using the [stop-process] command. """


def start():
    """ start = Starts specific codelines with Cmdline which helps to identify the current User, IP-Adresses, MAC-Adresses of Networkadapters and current Connections."""

def net():
    """ net = Shows all connections to current system with Powershell by using the [get-netneighbor] command. """

    
def krypt():
    """ krypt = Starts the builtin Encryption/Decryption Program. """
    
def search():
    """ search = Starts File Searching Program for different Datatypes. """
    
def copy():
    """ copy = Starts File Copying Program for different Datatypes. """

def clear():
    """ clear = Clears the Terminal from all written Text by using the [cls] command to start all over again. """


def exit():
    """ exit = The Program will be shutdown. """


def twitch():
    """ twitch = Starts chosen Channel of Twitch.tv with the Firefox Browser. """

def youtube():
    """ youtube = Starts chosen Channel of Youtube.de with the Firefox Browser. """

def google():
    """ google = Lets you search for your input via google.de """
    

####################################################################################################

#Keyword examples and Introduction

print("**ShortCommands**\n")

print(tabulate(KeyWordTableINDEX, headers= KeyWordCategoriesINDEX, tablefmt= "github"))


print("\n\nUse the [Keywords] above to start a certain function (Example: cmd list)")

print ("\n[KEYWORD] + help -> Additional Information\n")

######################################################################################################

#Loop-Start

Entry = input("\nPress any Button to continue...\n")

while Entry != "exit":


    x = input("\nCommand: ")
    History.append(x)
    
###################################################################################################### CMD and Powershell

    if x == "cmd list":

        print("\n**Commandline**")
        os.system("cmd /c tasklist") #/k= executes and remains open, /c= executes and closes shell

    elif x == "cmd kill":

        kill = input("\nWhich process? ")

        print("\n**Commandline**\n")
        os.system("cmd /c taskkill /F /PID " + kill + ".exe")
        History.append(kill)

    elif x == "cmd start":

        start = input("\nWhich process? ")

        print("\n**Commandline**")
        os.system("cmd /c start " + start + ".exe")
        History.append(start)


    elif x == "pwsh list":

        print("\n**Powershell**")
        os.system("powershell -c get-process") #-c =executes in commandline, start= executes in another canvas


    elif x == "pwsh kill":

        kill = input("\nWhich process? ")

        print("\n**Powershell**")
        os.system("powershell -c stop-process -name: " + kill)
        History.append(kill)

    elif x == "pwsh start":


        start = input("\nWhich process? ")

        print("\n**Powershell**")
        os.system("powershell -c start " + start)
        History.append(start)

###################################################################################################### Network

    elif x == "start":

        print("\nSearching...\n")
        os.system("cmd /c whoami & getmac -v & arp -a & net user")
        os.system("cmd /c systeminfo | findstr Betriebssystem")


    elif x == "net":

        print("\n**Powershell**")
        os.system("powershell get-netneighbor")



######################################################################################################### Kryptograph_2.0

    elif x == "krypt":
    
        os.system("cls")
        
        print("\nKryptograph 4.0\n")

        print("to encrypt your text, type [encrypt]")
        print("to decrypt your text, type [decrypt]")
        print("to clear window, type [clear]")

        print("to end program, type [exit]\n")


        intab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        outtab = "Z1T2R3E4W5Q6U7I8O9P0ASDFGuztrüwqiopasdCVBNmHJKLMNbvc"

        encryptTranslate = str.maketrans(intab, outtab)
        decryptTranslate = str.maketrans(outtab, intab)

        Entry = input("Press any Button to continue...")

        while Entry != "exit":

            x = input("\nEntry:")
    
            if x == "encrypt":
        
        
                x = input("\nYour Text(encrypted):\n")
                encrypt = x.translate(encryptTranslate)
                print(encrypt)
        
    
            elif x == "decrypt":
    
                x = input("\nYour Text(decrypted):\n")
                decrypt = x.translate(decryptTranslate)
                print(decrypt)
    
    
            elif x == "clear":
    
                os.system("cls")
        
                print("Kryptograph 4.0\n")

                print("to encrypt your text, type [encrypt]")
                print("to decrypt your text, type [decrypt]")
                print("to clear window, type [clear]")

                print("to end program, type [exit]\n")
    
    
            elif x == "exit":
                
                os.system("cls")
                
                print("\n-Kryptograph deactivated-\n")
    
                print("\n**ShortCommands**\n")

                print(tabulate(KeyWordTableINDEX, headers= KeyWordCategoriesINDEX, tablefmt= "github"))


                print("\n\nUse the [Keywords] above to start a certain function (Example: cmd list)")

                print ("\n[KEYWORD] + help -> Additional Information\n")
    
                break
                
                
    
            else:
    
                print("\nSorry?\n")

############################################################################################################ FileSearchPro_2.0
        
    elif x == "search":
    
        os.system("cls")
    
        totalFiles = 0  #Anzahl der Files
        totalDir = 0    #Anzahl der Directories
        
        searchList = []

        print("**FileSearch Pro 2.0**\n")




        KeyWordTableSEARCH = [["[txt]", "[clear]"],
                             ["[jpg]", "[save]"],
                             ["[gif]", ""],
                             ["[png]", ""]]


        KeyWordCategoriesSEARCH = ["Datatypes", "Miscellanous"]


        print(tabulate (KeyWordTableSEARCH, headers= KeyWordCategoriesSEARCH, tablefmt = "github"))


########################################################################################

#Loop-Start
        print("")

        Entry = input("\nPress any Button to continue...\n")

        while Entry != "ABORT":
            
            x = input ("\nWhich Datatype? ")
    
            if x == "txt":
    
                x = input("\nWhich Path? (Example: C:\\) ")
        
                print("\n - Search in Path [" + x + "] -\n")
        
                input()
        
        
                for root, dirs, files in os.walk(x):
                    for file in files:
                        if file.endswith(".txt"):
            
         
                            totalFiles +=1
           
           
                            print(os.path.join(root, file)) 
                            searchList.append(os.path.join(root, file))
                            
                            print("Found: ", totalFiles) 
                            print("")
                   

            elif x == "jpg":
    
                x = input("\nWhich Path? (Example: C:\\) \n")
        
                print("\n - Search in Path [" + x + "] -\n")
        
                input()
        
        
                for root, dirs, files in os.walk(x):
                    for file in files:
                        if file.endswith(".JPG"):
            
           
                            totalFiles +=1
           

                            print(os.path.join(root, file)) 
                            searchList.append(os.path.join(root, file))
                            
                            print("Found: ", totalFiles) 
                            print("")
                    
     
            elif x =="png":
    
                x = input("\nWhich Path? (Example: C:\\) \n")
        
                print("\n - Search in Path [" + x + "] -\n")
        
                input()
        
        
                for root, dirs, files in os.walk(x):
                    for file in files:
                        if file.endswith(".png"):
            
           
                            totalFiles +=1
           
                         
                            print(os.path.join(root, file))  
                            searchList.append(os.path.join(root, file))                            
                            
                            print("\nFound:", totalFiles) 
                            print("")
                    
                    
            elif x == "gif":
    
                x = input("\nWhich Path? (Example: C:\\) \n")
        
                print("\n - Search in Path [" + x + "] -\n")
    
                input()
    
    
                for root, dirs, files in os.walk(x):
                    for file in files:
                        if file.endswith(".gif"):
                
                            totalFiles +=1
           
            
                            print(os.path.join(root, file)) 
                            searchList.append(os.path.join(root, file))
                            
                            print("\nFound:", totalFiles) 
                            print("")
                            
                            
            elif x == "save":
            
                with open ("FileSearch.txt", "w") as savefile:
                    for item in searchList:
                        savefile.write(item + ", \n")
    
    
    
            elif x == "clear":
            
                os.system("cls")
            
                print("**FileSearch Pro 2.0**\n")


                print(tabulate (KeyWordTableSEARCH, headers= KeyWordCategoriesSEARCH, tablefmt = "github"))


############################################################################

#Loop-End                  
                    
            elif x == "exit":    
            
                os.system("cls")
        
                print("\n**ShortCommands**\n")

                print(tabulate(KeyWordTableINDEX, headers= KeyWordCategoriesINDEX, tablefmt= "github"))

                print("\n\nUse the [Keywords] above to start a certain function (Example: cmd list)")

                print ("\n[KEYWORD] + help -> Additional Information\n")
        
                break
     
    
            else:
    
                print("\nError...")
        
        
        
############################################################################################################ CopyPaster_3.0
       
    elif x == "copy":
    
        KeyWordTableCOPY = [["txt"],
                            ["jpg"],
                            ["png"]]
                    
        KeyWordCategories = ["Datatypes"]


        Destination = "C:\\Users\\User\Desktop\CopyPaster_3.0\Target"

        TotalFiles = 0



        ########################################################################################

        #Loop-Start
        
        os.system("cls")

        print("CopyPaster 3.0\n")

        print(tabulate(KeyWordTableCOPY, headers= KeyWordCategories, tablefmt= "github"))


        start = input("\nPress any Button to continue...\n" )

        while start != "exit":

            x = input("\nWhich Datatypes? ")
    
            if x == "txt":
    
                path = input("\nWhich Path? ")
                Destination = input("\nWhich Destination? ")
    

                for root, dirs, files in os.walk(path):
                    for file in files:
                        if file.endswith(".txt"):
                
                            TotalFiles += 1
           
                            print(os.path.join(root, file))
                
                            try:
            
                                shutil.copy(os.path.join(root, file), (os.path.join(Destination, file)))                         
                                print("\nfile copied...", TotalFiles, "\n")
                
                
                            except:
            
                                print("copy failed...\n")
			
            	
                print("\nTarget Directory:\n")
        
                print(os.listdir(Destination))
        
        
        
            elif x == "jpg":
    
                path = input("\nWhich Path? ")
                Destination = input ("\nWhich Destination? ")
        
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if file.endswith(".JPG"):
                
                            TotalFiles += 1
                
                            print(os.path.join(root, file))
                    
                            try:
                    
                                shutil.copy(os.path.join(root, file), (os.path.join(Destination, file)))
                                print("\nfile copied...", TotalFiles, "\n")
                        
                            except:
                    
                                print("copy failed...\n")
                        
                        
                print("\nTarget Directory:\n")
        
                print(os.listdir(Destination))
        
        
        
            elif x == "png":
    
                path = input("\nWhich Path? ")
                Destination = input("\nWhich Destination? ")
        
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if file.endswith(".png"):
                
                            TotalFiles += 1
                
                            print(os.path.join(root, file))
                    
                            try:
                    
                                shutil.copy(os.path.join(root, file), (os.path.join(Destination, file)))
                                print("file copied...", TotalFiles, "\n")
                        
                            except:
                    
                                print("copy failed...\n")
                        
                print("\nTarget Directory:\n")
        
                print(os.listdir(Destination))
        
        
            elif x == "clear":
    
                os.system("cls")
        
                print("CopyPaster 3.0\n")

                print(tabulate(KeyWordTableCOPY, headers= KeyWordCategories, tablefmt= "github"))

                print("\nTarget Directory:\n")
       
                print(os.listdir(Destination))
    


        ########################################################################################

        #Loop-End
        
            elif x == "exit":
            
                os.system("cls")
                
                print("**ShortCommands**\n")

                print(tabulate(KeyWordTableINDEX, headers= KeyWordCategoriesINDEX, tablefmt= "github"))


                print("\n\nUse the [Keywords] above to start a certain function (Example: cmd list)")

                print ("\n[KEYWORD] + help -> Additional Information\n")
    
                break
                
                
            else:
    
                print("\nError...")
                
                
############################################################################################################ Websites       
    
    elif x == "twitch":
        
        channel = input("\nWhich Channel? ")
        
        while channel != "stop":

            print("\n**Firefox**")
            print("------------\n")
            print("*Twitch* = " + channel)

            os.system("cmd /c start firefox.exe twitch.tv/" + channel)
            History.append(channel)
            
            break


    elif x == "youtube":

        channel = input("\nWhich Channel? ")

        print("\n**Firefox**")
        print("-----------\n")
        print("*Youtube* = " + channel)

        os.system("cmd /c start firefox.exe youtube.de/results?search_query=" + channel)
        History.append(channel)


    elif x == "google":

        search = input("\nSearch for what? ")

        print("\n**Firefox**")
        print("------------\n")
        print("*Googles* = " + search)

        os.system("cmd /c start firefox.exe google.de/search?q=" + search)
        History.append(channel)
        

    elif x == "clear":

       os.system("cls")

       print ("**ShortCommands**\n")

       print(tabulate(KeyWordTableINDEX, KeyWordCategoriesINDEX, tablefmt ="github"))

       print("\n\nUse the [Keywords] above to start a certain function (Example: cmd list)")
       print ("\n[KEYWORD] + help -> Additional Information\n")


    elif x == "history":

        print(History)


###############################################################################################

#help-Commands


    elif x == "cmd help":

        help(cmd)


    elif x == "pwsh help":

       help(pwsh)

        
        
    elif x == "krypt help":
    
        help(krypt)


    elif x == "start help":

        help(start)


    elif x == "net help":

        help(net)

        
    elif x == "search help":
    
        help(search)
        
        
    elif x == "copy help":
    
        help(copy)


    elif x == "twitch help":

        help(twitch)


    elif x == "youtube help":

        help(youtube)

    elif x == "google help":

        help(google)


    elif x == "clear help":

        help(clear)


    elif x == "exit help":

        help(exit)


############################################################################################

# Loop End

    elif x == "exit":

        break

    else:

        print("\nError...")


print("\nGoodbye!")

input()

