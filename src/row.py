import copy

class Row:
	def __init__(self, record):
		self.cells = record
		self.cooked = self.copyf(record)
		self.isEvaled = False

	def copyf(self, record):
		if not isinstance(record, list):
			return record
		u = copy.deepcopy(record)
		return u

