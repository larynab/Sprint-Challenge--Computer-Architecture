"""CPU functionality."""

import sys

#OP
HLT = 0b00000001
PRN = 0b01000111
LDI = 0b10000010
MUL = 0b10100010
PUSH = 0b01000101
POP = 0b01000110
CALL = 0b01010000
RET = 0b00010001
ADD = 0b10100000
CMP = 0b10100111
JMP = 0b01010100
JEQ = 0b01010101
JNE = 0b01010110  

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.register = [0] * 8
        self.pc = 0
        self.sp = 7

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value

    def load(self):
        """Load a program into memory."""
        
        print(sys.argv)
        
        address = 0

        if len(sys.argv) != 2:
            print(f"usage: {sys.argv[0]}")
            sys.exit(1)

        try:
            with open(sys.argv[1]) as my_file:
                for line in my_file:
                    num = line.split("#", 1)[0]
                    if num.strip() == '':
                        continue
                    self.ram[address] = int(num[0:8], 2)
                    address += 1
                    print(int(num[0:8]))


        except FileNotFoundError:
            print(f"{sys.argv[0]}: {sys.argv[1]} not found")
            sys.exit(2)

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.register[reg_a] += self.register[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            self.register[reg_a] *= self.register[reg_b]
        elif op == "CMP":
            while self.register[reg_a] == self.register[reg_b]:
                flag = True  
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        running = True
        flag = False
        
        while running:
            IR = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc+1)
            operand_b = self.ram_read(self.pc+2)            

            if IR == LDI:
                self.register[operand_a] = operand_b
                print(f"LDI {self.register[operand_a]}")
                self.pc += 3

            if IR == MUL:
                print("MULTIPLYING")
                self.alu("MUL", operand_a, operand_b)
                self.pc += 3

            if IR == ADD:
                print("ADDING")
                self.alu("ADD",operand_a, operand_b)
                self.pc += 3

            if IR == PUSH:
                self.register[self.sp] -= 1
                regnum = self.ram[self.pc + 1]
                value = self.register[regnum]
                self.ram[self.register[self.sp]] = value
                print(f"PUSH {self.register[operand_a]}")
                self.pc += 2

            if IR == POP:
                value = self.ram[self.register[self.sp]]
                regnum = self.ram[self.pc + 1]
                self.register[regnum] = value
                print(f"POP {self.register[regnum]}")
                self.register[self.sp] += 1
                self.pc += 2
            
            if IR == CALL:
                print('CALL')
                ret = self.pc + 2
                self.register[self.sp] -= 1
                self.ram[self.register[self.sp]] = ret
                sub = self.register[operand_a]
                self.pc = sub

            elif IR == RET:
                ret = self.ram[self.register[self.sp]]
                self.register[self.sp] += 1
                self.pc = ret

            elif IR == CMP:
                print("CMP")
                self.alu("CMP",operand_a, operand_b)
                print(f"Flag set to {flag}")
                self.pc += 3
            
            elif IR == JMP:
                print("JMP")
                # self.ram[self.register[self.pc]] == self.ram[self.register[operand_a]]
                jumper = self.register[operand_a]
                self.pc = jumper
                print(f"Jumped to {jumper}")

            elif IR == JEQ:
                print("JEQ")
                if flag == True:
                    # self.ram[self.register[self.pc]] == self.ram[self.register[operand_a]]
                    # print(f"Jumped to {operand_a}")
                    jumper = self.register[operand_a]
                    self.pc = jumper
                    print(f"Jumped to {jumper}")
                else:
                    self.pc += 2

            elif IR == JNE:
                print("JNE")
                if flag == False:
                    # self.ram[self.register[self.pc]] == self.ram[self.register[operand_a]]
                    # print(f"Jumped to {operand_a}")
                    jumper = self.register[operand_a]
                    self.pc = jumper
                    print(f"Jumped to {jumper}")
                else:
                    self.pc += 2            
        
            if IR == PRN:
                print(f"PRN {self.register[operand_a]}")
                self.pc += 2
                
            elif IR == HLT:
                running = False
                print("HLT")
                self.pc += 1

# Code to test the Sprint Challenge
#
# Expected output:
# 1
# 4
# 5

#OLD CODE----------------------------------------------------------------------------------------     
        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1           
            # self.pc += 1
            # else:
            #     running = False
            #     break
            #     print("no more commands, closing")  
            
    # def LDI(self):
    #     operand_a = self.ram_read(self.pc+1)
    #     operand_b = self.ram_read(self.pc+2)
    #     self.register[operand_a] = operand_b              

