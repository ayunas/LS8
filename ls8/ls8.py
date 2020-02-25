import sys
from itertools import dropwhile
sys.path.append('./examples')

from instructions import inst

class LS8:
    def __init__(self):
        self.ram = [0]*256 #8 bit processor can handle 256 bytes in memory
        self.registers = [0]*8
        self.pc = 0
        self.mar = None #Memory Address Register, holds the memory address to read/write

    def load(self):
        filename = input("enter the LS8 program you wish to run: ")
        try:
            data = open(f"./examples/{filename}",'r')
            # print([*data])
           
        except:
            print(f"Could not open/read file {filename}. exiting...")
            sys.exit(1)
        
        clear_header = [*dropwhile(lambda l : l.startswith('#') or l == '\n',data)]
        clear_comments = [byte.split('#')[0].strip() for byte in clear_header]
        program = [b for b in clear_comments if b != '']
        print(program, '\n')

        address = self.ram.index(0) #sets address to first empty space in memory
        
        for byte_str in program:
            self.ram[address] = int(byte_str,2)
            address += 1
        
        print(self.ram)
        print('program loaded into RAM successfully')
    
    def ram_read(self):
        print('ram_read')
        self.pc += 1
        return self.ram[self.pc]
    
    def reg_write(self,reg,data):
        print('reg_write')
        self.registers[reg] = data
        print(self.registers)
        self.pc += 1
    
    def run(self):
        self.load()
        halted = False

        while halted == False:
            instruction = self.ram[self.pc]
            print(instruction == inst['LDI'])
            if instruction == inst['LDI']:
                reg = self.ram_read()
                data = self.ram_read()
                print(reg,data)
                self.reg_write(reg,data)

            print(self.registers)
            break














    


ls8 = LS8()
ls8.run()
