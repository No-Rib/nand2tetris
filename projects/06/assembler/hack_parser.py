#!/usr/bin/env python
"""Tools for Hack assembly language parsing"""

import re

def is_code(line):
	"""Return True if given line is line of Hack code, False if comment or whitespace"""

	return False if line.isspace() or line.startswith("//") else True


def is_label(line):
	"""Returns True if given line is Hack label"""

	label_pattern = re.compile(r"\(.*\)")
	return bool(label_pattern.match(line))


def is_ainst(line):
	"""Returns True if given line is Hack A-instruction"""

	ainst_pattern = re.compile("@.*")
	return ainst_pattern.match(line)


def get_cinst(line):
	"""Returns parsed Hack C-instruction"""

	dest = None
	comp = None
	jump = None

	if "=" in line:
		dest, rest = [x.strip() for x in line.split("=")]
	else:
		rest = line

	if ";" in rest:
		comp, jump = [x.strip() for x in rest.split(";")]
	else:
		comp = rest

	return (dest, comp, jump)


def parse_line(rawline):
	"""Returns parsed Hack line and result code"""

	line = rawline.split()
	if line:
		line = line[0]
	else:
		return (None, None)

	result_value = None

	if is_code(line):
		if is_label(line):
			result_code = "L"
			result_value = line[1:-1]
		elif is_ainst(line):
			result_code = "A"
			result_value = line[1:]
		else:
			result_code = "C"
			result_value = get_cinst(line)
	else:
		result_code = None

	return (result_code, result_value)
