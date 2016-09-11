#!/usr/bin/env python
"""Tools for Hack assembly translation"""

HACK_JUMP_TABLE = {
	"JGT": "001",
	"JEQ": "010",
	"JGE": "011",
	"JLT": "100",
	"JNE": "101",
	"JLE": "110",
	"JMP": "111"
}


def a_translate(instruction, symtable):
	"""Translates Hack A-instruction to machine code"""

	mcode = None

	if instruction.isdigit():
		mcode = format(int(instruction), 'b').zfill(16)
	else:
		address = symtable.get_address(instruction)
		if address is None:
			address = symtable.add_variable(instruction)

		mcode = format(address, 'b').zfill(16)

	return mcode


def get_dest_mcode(dest):
	"""Translates destination segment of C-instruction"""

	if dest is None:
		return "000"
	return "{0}{1}{2}".format(int("A" in dest), int("D" in dest), int("M" in dest))


def get_comp_mcode(comp):
	"""Translates computation segment of C-instruction"""

	mcode = None

	if comp == "0":
		mcode = "0101010"
	elif comp == "1":
		mcode = "0111111"
	elif comp == "-1":
		mcode = "0111010"
	else:
		if "M" in comp:
			mcode = "1{0}"
			comp = comp.replace("M", "A")
		else:
			mcode = "0{0}"

		if len(comp) == 1:
			mcode = mcode.format("{0}00".format("0011" if comp == "D" else "1100"))
		elif comp.startswith("!"):
			mcode = mcode.format("{0}01".format("0011" if comp == "D" else "1100"))
		elif comp.startswith("-"):
			mcode = mcode.format("{0}11".format("0011" if comp == "D" else "1100"))
		elif comp.endswith("+1"):
			mcode = mcode.format("{0}1{1}111")
			if comp.startswith("D"):
				mcode = mcode.format(0, 1)
			else:
				mcode = mcode.format(1, 0)
		elif comp.endswith("-1"):
			mcode = mcode.format("{0}10".format("0011" if comp[0] == "D" else "1100"))
		elif comp == "A-D":
			mcode = mcode.format("000111")
		elif comp == "D+A":
			mcode = mcode.format("000010")
		elif comp == "D-A":
			mcode = mcode.format("010011")
		elif comp == "D&A":
			mcode = mcode.format("000000")
		elif comp == "D|A":
			mcode = mcode.format("010101")

	return mcode


def get_jump_mcode(jump):
	"""Translates jump segment of C-instruction"""

	return HACK_JUMP_TABLE.get(jump, "000")

def c_translate(instruction):
	"""Translates Hack C-instruction to machine code"""

	mcode = "111{comp}{dest}{jump}"

	raw_dest, raw_comp, raw_jump = instruction

	comp = get_comp_mcode(raw_comp)
	dest = get_dest_mcode(raw_dest)
	jump = get_jump_mcode(raw_jump)

	return mcode.format(comp=comp, dest=dest, jump=jump)


def translate(itype, instruction, symtable):
	"""Translates Hack instruction to machine code"""

	mcode = None

	if itype == "A":
		mcode = a_translate(instruction, symtable)
	elif itype == "C":
		mcode = c_translate(instruction)

	return mcode
