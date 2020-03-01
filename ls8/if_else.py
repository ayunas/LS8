            # if instruction != 'JMP' or instruction != 'JNE':
            # if instruction not in no_increments:
            #     self.increment_pc(ir)

            # if ir == opc['LDI']:  #opc = operation code or the instruction
            #     self.ldi()
            #     reg = self.ram_read(1)
            #     data = self.ram_read(2)
            #     self.reg_write(reg,data)

            # elif ir == opc['PRN']:
            #     reg = self.ram_read(1)
            #     self.reg_read(reg)
            
            # if ir == opc['MUL']:
            #     reg_1 = self.ram_read(1)
            #     reg_2 = self.ram_read(2)
            #     self.alu('MUL', reg_1,reg_2)
            
            # elif ir == opc['ADD']:
            #     reg_1 = self.ram_read(1)
            #     reg_2 = self.ram_read(2)
            #     self.alu('ADD', reg_1,reg_2)
            
            # elif ir == opc['PUSH']:
            #     # reg = self.ram_read()
            #     # val = self.reg_read(reg)
            #     # self.push()
            #     reg = self.ram_read(1)
            #     self.push(self.registers[reg])
            
            # elif ir == opc['POP']:
            #     reg = self.ram_read(1)
            #     self.pop(reg)
            
            # elif ir == opc["JMP"]:
            #     #jump to address stored in the register operand
            #     # reg = self.ram[self.pc + 1]
            #     reg = self.ram_read(1)
            #     self.jump(reg)
            #     # self.pc = self.registers[reg]
            #     # print('JMP to ', self.pc)
            #     continue

            # elif ir == opc["PRA"]:
            #     reg = self.ram_read(1)
            #     self.reg_read(reg,True)  #True to print out the ASCII equivalent of the code in the register

            # elif ir == opc["CALL"]:
            #     # next_opc = self.ram_read(2)
            #     instruction_length = (ir >> 6) + 1 #inst_len = 2 for the CALL.  1 instruction + 1 operand only
            #     next_pc = self.pc + instruction_length
            #     self.push(next_pc) #push the ADDRESS of the next OPC not the opcode itself
            #     reg = self.ram_read(1)
            #     self.pc = self.registers[reg]
            #     continue
            
            # elif ir == opc["RET"]:
            #     address = self.pop()
            #     self.pc = address
            #     continue  #any instruction manually setting the pc, like returning from subroutine or jmp, don't process the typical increment of the while loop
            
            # elif ir == opc["ADDI"]:
                # reg_a = self.ram_read(1)
                # val = self.ram_read(2)
                # reg_b = self.registers.index(0) #find first empty register to store new value
                # self.reg_write(reg_b,val)
                # self.alu('ADD',reg_a,reg_b)

            # elif ir == opc["IRET"]:
            #     pass

            # elif ir == opc["CMP"]:
            #     reg_a = self.ram_read(1)
            #     reg_b = self.ram_read(2)
            #     self.alu('CMP',reg_a,reg_b)
            
            # elif ir == opc["JEQ"]:
            #     # equal_mask = 0b00000001
            #     # equal = self.fl & equal_mask
            #     equal = self.equal()
            #     if equal:
            #         reg = self.ram_read(1)
            #         self.jump(reg)
            #         continue
            
            # elif ir == opc["JNE"]:
            #     # equal_mask = 0b00000001
            #     # equal = self.fl & equal_mask
            #     equal = self.equal()
            #     if not equal:
            #         reg = self.ram_read(1)
            #         self.jump(reg)
            #         continue

            # elif ir == opc['ST']:
                # reg_a = self.ram_read(1)
                # reg_b = self.ram_read(2)
                # mar = self.registers[reg_a]
                # mdr = self.registers[reg_b]
                # self.ram_write(mar,mdr)
                # print(self.ram)
            
            # elif ir == opc["AND"]: 
            #     reg_a = self.ram_read(1)
            #     reg_b = self.ram_read(2)
            #     self.alu('AND', reg_a,reg_b)
            
            # elif ir == opc["OR"]:
            #     reg_a = self.ram_read(1)
            #     reg_b = self.ram_read(2)
            #     self.alu('OR', reg_a,reg_b)
            
            # elif ir == opc["XOR"]:
            #     reg_a = self.ram_read(1)
            #     reg_b = self.ram_read(2)
            #     self.alu('XOR', reg_a,reg_b)

            # elif ir == opc["SHL"]:
                # reg_a = self.ram_read(1)
                # reg_b = self.ram_read(2)
                # self.alu('SHL', reg_a,reg_b)

            # elif ir == opc["SHR"]:
            #     reg_a = self.ram_read(1)
            #     reg_b = self.ram_read(2)
            #     self.alu('SHR', reg_a,reg_b) 

            # elif ir == opc["MOD"]:
            #     reg_a = self.ram_read(1)
            #     reg_b = self.ram_read(2)
            #     self.alu('MOD', reg_a,reg_b)                   

            # elif ir == opc["NOT"]:
            #     reg_a = self.ram_read(1)
            #     self.alu("NOT", reg_a)

            # elif ir == opc['HLT']:
            #     halted == True
            #     # self.pc += 1
            #     sys.exit(1)
            # else:
            #     opcode = [o for o in opc if opc[o] == ir]
            #     if not len(opcode):
            #         print(f'opcode {ir} not found, exiting...')
            #     else:
            #         print('invalid opcode', opcode[0], 'exiting...')
            #     sys.exit(1)