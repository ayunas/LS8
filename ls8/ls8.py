import sys
from itertools import dropwhile
sys.path.append('./examples')

from opcodes import opc  #operation code

class LS8:
    def __init__(self):
        self.ram = [0]*256 #8 bit processor can handle 256 bytes in memory
        self.registers = [0]*8 #general purpose registers
        self.pc = 0 #program counter register (reserved)
        self.sp = 0xf4 #initialized to index 244, used for moving through the RAM.
        self.registers[7] = self.sp  #r7 is the stack pointer, initialized to 244
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
        data.close()
    
    def ram_read(self,n):
        # self.pc += 1
        mdr = self.ram[self.pc + n]  #memory data register
        return mdr
    
    def ram_write(self,mar,mdr):
        self.ram[mar] = mdr  #write the memory data register value at the memory address register.
    
    def reg_write(self,reg,data):
        self.registers[reg] = data
        # self.pc += 1

    def reg_read(self,reg):
        print(f'r[{reg}]: {self.registers[reg]}')
        # self.pc += 1
    
    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        if op == "ADD":
            self.registers[reg_a] += self.registers[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            self.registers[reg_a] *= self.registers[reg_b]
        else:
            raise Exception("Unsupported ALU operation")
        # self.pc += 1
    
    def push(self,reg):
        self.sp -= 1
        if self.ram[self.sp] != 0:
            raise IndexError('stack overflow...')
            sys.exit(1)
        else:
            self.ram[self.sp] = self.registers[reg]
            # self.pc += 1

    def pop(self,reg):
        self.registers[reg] = self.ram[self.sp]
        self.ram[self.sp] = 0
        if self.sp > len(self.ram):
            raise IndexError('stack underflow...')
            sys.exit(1)
        self.sp += 1
        # self.pc += 1

    def run(self):
        self.load()
        halted = False

        while halted == False:
            ir = self.ram[self.pc]  #instruction register.  the current instruction to process from the ls8 assembly program loaded
            print([o for o in opc if opc[o] == ir][0])
            if ir == opc['LDI']:  #opc = operation code or the instruction
                reg = self.ram_read(1)
                data = self.ram_read(2)
                self.reg_write(reg,data)

            elif ir == opc['PRN']:
                reg = self.ram_read(1)
                self.reg_read(reg)
            
            elif ir == opc['MUL']:
                reg_1 = self.ram_read(1)
                reg_2 = self.ram_read(2)
                self.alu('MUL', reg_1,reg_2)
            
            elif ir == opc['ADD']:
                reg_1 = self.ram_read(1)
                reg_2 = self.ram_read(2)
                self.alu('ADD', reg_1,reg_2)

            elif ir == opc['HLT']:
                halted == True
                # self.pc += 1
                break
            
            elif ir == opc['PUSH']:
                # reg = self.ram_read()
                # val = self.reg_read(reg)
                # self.push()
                reg = self.ram_read(1)
                self.push(reg)
            
            elif ir == opc['POP']:
                reg = self.ram_read(1)
                self.pop(reg)
            
            elif ir == opc["JMP"]:
                #jump to address stored in the register operand
                reg = self.ram[self.pc + 1]
                self.pc = self.registers[reg]
                print('JMP to ', self.pc)
                print('ram', self.ram)
                continue

            else:
                opcode = [o for o in opc if opc[o] == ir]
                if not len(opcode):
                    print(f'opcode {ir} not found, exiting...')
                else:
                    print('invalid opcode', opcode[0], 'exiting...')
                sys.exit(1)
            
            ir_operands = ir >> 6
            instruction_length = ir_operands + 1
            # print('instruction length', instruction_length)
            self.pc += instruction_length
            # print(self.ram) 
            # print(self.registers)

ls8 = LS8()
ls8.run()
print(ls8.ram)
print(ls8.registers)