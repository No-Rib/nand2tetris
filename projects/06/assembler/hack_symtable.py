#!/usr/bin/env python
"""Tools for Hack assembly language symbol table handling"""


DEFAULT_HACK_TABLE_VALUES = {
	"SCREEN": 16384,
	"KBD": 24576,
	"SP": 0,
	"LCL": 1,
	"ARG": 2,
	"THIS": 3,
	"THAT": 4
}

def get_default_table():
	"""Returns default symbol table"""
	table = dict(("R{0}".format(i), i) for i in range(16))
	table.update(DEFAULT_HACK_TABLE_VALUES)
	return table


class SymTable(object):
	"""Class implementing Hack sybmol table"""

	def __init__(self):
		self.table = get_default_table()
		self.next_free = 16

	def get_address(self, symbol):
		"""Gets address by symbol"""

		return self.table.get(symbol, None)

	def add_label(self, label, value):
		"""Adds label symbol to the table"""

		self.table[label] = value

	def add_variable(self, variable):
		"""Adds variable symbol to the table"""

		self.table[variable] = self.next_free
		self.next_free += 1
		return self.table[variable]
 