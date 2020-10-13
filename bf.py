#! /usr/bin/python3

import sys

def bf(program, bits = 8):
	byte = 2**bits
	memory, mc = [0], 0
	pc, pair, stack = 0, {}, []

	# minification du programme
	program = ''.join([c for c in program if c in "+-><[].,"])

	# resolution des boucles
	for i in range(len(program)):
		if program[i] == '[': stack.append(i)
		elif program[i] == ']': pair[stack.pop()] = i

	# erreur de boucle
	if len(stack): return


	l = len(program)
	while pc < l:

		if program[pc] == '+': memory[mc] = (memory[mc] + 1) % byte
		elif program[pc] == '-': memory[mc] = (memory[mc] + (byte - 1)) % byte
		elif program[pc] == '>' and mc + 1 < len(memory): mc += 1
		elif program[pc] == '>': memory.append(0); mc += 1
		elif program[pc] == '<' and mc == 0: memory.insert(0, 0)
		elif program[pc] == '<': mc -= 1
		elif program[pc] == '[' and memory[mc]: stack.append(pc)
		elif program[pc] == '[': pc = pair[pc]
		elif program[pc] == ']': pc = stack.pop() - 1
		elif program[pc] == ',': memory[mc] = ord((input() + '\x00')[0])
		elif program[pc] == '.': print(chr(memory[mc]), end='')

		pc += 1


if __name__ == '__main__' and len(sys.argv) == 2:
	bf(sys.argv[1])
