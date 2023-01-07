class person:
    def __init__(self, name):
        self.name=name
        
    def talk(name):
        print(f"Hello It's {name} !")
        print('''How I can help you?
        press 1 to get the list of cmds
        press 2 to skip'''
              )
        step2 = input(">")
        if(step2=="1"):
            print('''! Enter the cmds to get their manual !
                  1) ls
                  2)chmod
                  3)pwd
                  4)mkdir
                  5) mv
                  6)touch
                  7)cd''')
            step3 = input(">")
        else:
            step3 = input(">") 
        
        commands = {
            "ls": "The most frequently used command in Linux to list directories",
            
            "chmod": '''chmod is the command and system call used to change the access 
                        permissions and the special mode flags of file system objects.''',
                        
            "cd":"Linux command to navigate through directories.",
            
            "pwd": "Print working directory command in Linux",
            
            "mv" :"Move or rename files in Linux",
            
            "mkdir":"Command used to create directories in Linux.",
            
            "touch": "touch is a command used to update the access date and/or modification date of a computer file or directory."
            }

        if(step3=="ls"):
            print(commands.get("ls"))
        if(step3=="chmod"):
            print(commands.get("chomd"))
        if(step3=="cd"):
            print(commands.get("cd"))
        if(step3=="pwd"):
            print(commands.get("pwd"))
        if(step3=="mv"):
            print(commands.get("mv"))
        if(step3=="mkdir"):
            print(commands.get("mkdir"))
        if(step3=="touch"):
            print(commands.get("touch"))


person1 = person.talk("Harshita")
