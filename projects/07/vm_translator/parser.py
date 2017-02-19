"""Provides Parser class that handles vm-code file parsing."""

import re

_COMMENT_RE = re.compile("//.*$")

class Parses(object):
	"""Class thaht handles vm-code file parsing."""

	def __init__(self, inputfile):

		self.file = open(inputfile, "r")
		self.current_cmd = None

	def advance(self):
		"""Reads next command and makes it current one."""

		self.current_cmd = _tokenize(lines.pop(0))

		pass

	def command_type(self):
		"""Returns type of current command."""
		pass

	def arg1(self):
		"""Returns first agrument of current command."""
		pass

	def arg2(self):
		"""Returns second agrument of current command."""
		pass

	@classmethod
	def _tokenize(cls, cmd):
		"""Returns tokenized command."""
		return cmd

	def _get_next_cmd(self):
		"""Sets next command."""

		prepped_cmd = self._prep_cmd()


	def _prep_cmd(self):
		"""Returns next non-null command."""

		while True:
			raw_cmd = lines.pop(0)
			prep_cmd = self._rm_comment(raw_cmd)
			if prep_cmd:
				return prep_cmd

	@classmethod
	def _rm_comment(cls, raw_cmd):
		"""Removes comment from line."""

		return _COMMENT_RE.sub("", raw_cmd)
