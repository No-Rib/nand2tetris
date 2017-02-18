"""Provides CodeWriter class that converts parsed vm-code command to assembly command."""

class CodeWriter(object):
	"""Class that converts parsed vm-code command to assembly command."""

	def __init__(self, outputfile):
		pass

	@classmethod
	def _translate_arithmetic(self, command):
		"""Returns translated arithmetic command."""

		pass

	def _translate_stack(self, command):
		"""Returns translated stack manipulation command."""

		pass

	def write_command(self, command):
		"""Writes command to otuput file."""

		pass