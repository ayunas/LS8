import sys
from itertools import dropwhile
sys.path.append('./examples')

class LS8:
    def __init__(self):
        self.ram = [0]*256 #8 bit processor can handle 256 bytes in memory
        self.register = [0]*8
        self.pc = self.register[-1]
    
    def load(self):
        filename = input("enter the LS8 program you wish to run: ")
        try:
            data = open(f"./examples/{filename}",'r')
            # print([*data])
           
        except:
            print(f"Could not open/read file {filename}. exiting...")
            sys.exit(1)
        
        prog_comments = [*dropwhile(lambda l : l.startswith('#') or l == '\n',data)]
        program = [byte.split('#')[0].strip() for byte in prog_comments]
        program = [b for b in program if b != '']
        print(program)





ls8 = LS8()

ls8.load()
