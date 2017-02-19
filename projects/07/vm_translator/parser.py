"""Provides Parser class that handles vm-code file parsing."""

import re

_COMMENT_RE = re.compile("//.*$")

_OK_CODE = 0
_EOF_CODE = 1

class Parser(object):
	"""Class thaht handles vm-code file parsing."""

	def __init__(self, inputfile):

		self.file = open(inputfile, "r")
		self.current_cmd = None
		self.cmd_code = _OK_CODE

	def advance(self):
		"""Reads next command and makes it current one."""

		self.cmd_code, self.current_cmd = self._get_next_cmd()
		return self.cmd_code

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

		code, prepped_cmd = self._prep_cmd()
		if code == _EOF_CODE:
			return (code, None)

		return (code, self._tokenize(prepped_cmd))

	def _prep_cmd(self):
		"""Returns next non-null command."""

		while True:
			try:
				raw_cmd = self.file.next()
			except StopIteration:
				return (_EOF_CODE, None)
			prep_cmd = self._rm_comment(raw_cmd).strip()
			if prep_cmd:
				return (_OK_CODE, prep_cmd)

	@classmethod
	def _rm_comment(cls, raw_cmd):
		"""Removes comment from line."""

		return _COMMENT_RE.sub("", raw_cmd)
