#!/usr/bin/env python
"""Main body of Hack to machine code translator"""

import os
import sys

import hack_parser
import hack_symtable
import hack_translator


def translate():
	"""Main function"""

	asm_file_name = sys.argv[1]
	hack_file_name = os.path.splitext(asm_file_name)[0] + ".hack"

	asm_file = open(asm_file_name, "r")
	hack_file = open(hack_file_name, "w")

	raw_asm_code = asm_file.readlines()
	asm_code = []

	symtable = hack_symtable.SymTable()

	# label handling phase
	for line in raw_asm_code:
		(code, instruction) = hack_parser.parse_line(line)

		if code is not None:
			if code == "L":
				symtable.add_label(instruction, len(asm_code))
			else:
				asm_code.append((code, instruction))

	# code translation phase
	for code, instruction in asm_code:
		hack_file.write(hack_translator.translate(code, instruction, symtable) + "\n")

	asm_file.close()
	hack_file.close()

translate()
