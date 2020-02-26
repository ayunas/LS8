import sys
from itertools import dropwhile
sys.path.append('./examples')

from opcodes import opc  #operation code

class LS8:
    def __init__(self):
        self.ram = [0]*256 #8 bit processor can handle 256 bytes in memory
        self.registers = [0]*8 #general purpose registers
        self.registers[-1] = 0xf4  #r7 initialized to 244 
        self.pc = 0 #program counter register (reserved)
        self.fl = 0  #flag register (reserved)

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

        address = self.ram.index(0) #sets address to first empty space in memory
        
        for byte_str in program:
            self.ram_write(address,int(byte_str,2))
            # self.ram[address] = int(byte_str,2)
            address += 1
        print('LS8 assembly program:\n',program,'\nloaded into RAM successfully.')
    
    def ram_read(self):
        self.pc += 1
        mdr = self.ram[self.pc]  #memory data register
        return mdr
    
    def ram_write(self,mar,mdr):
        self.ram[mar] = mdr  #write the memory data register value at the memory address register.
    
    def reg_write(self,reg,data):
        self.registers[reg] = data
        self.pc += 1

    def reg_read(self,reg):
        print(f'r[{reg}]: {self.registers[reg]}')
        self.pc += 1
    
    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        if op == "ADD":
            self.registers[reg_a] += self.registers[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            self.registers[reg_a] *= self.registers[reg_b]
        else:
            raise Exception("Unsupported ALU operation")
        self.pc += 1

    def run(self):
        self.load()
        halted = False

        while halted == False:
            ir = self.ram[self.pc]  #instruction register.  the current instruction to process from the ls8 assembly program loaded

            if ir == opc['LDI']:  #opc = operation code or the instruction
                reg = self.ram_read()
                data = self.ram_read()
                self.reg_write(reg,data)

            elif ir == opc['PRN']:
                reg = self.ram_read()
                self.reg_read(reg)
            
            elif ir == opc['MUL']:
                reg_1 = self.ram_read()
                reg_2 = self.ram_read()
                self.alu('MUL', reg_1,reg_2)

            elif ir == opc['HLT']:
                halted == True
                self.pc += 1
                sys.exit(1)

            else:
                opcode = [o for o in opc if opc[o] == ir]
                if not len(opcode):
                    print('opcode not found, exiting...')
                else:
                    print('invalid opcode', opcode[0], 'exiting...')
                sys.exit(1)

ls8 = LS8()
ls8.run()
print(ls8.registers)
