import re

# # Common or utility functions go here
# def push(t, k):
# 	keyss = sorted(t.keys())
# 	t[len(keyss)] = k
# 	return k

def coerce(s):
    def isNumber(string):
        try:
            float(string)
            return True
        except ValueError:
            return False 

    def fun1(s1):
        if s1 == "true":
            return True
        elif s1 == "false":
            return False
        return s1
    
    if isNumber(s):
        return int(s)  
    else:
        return fun1(s) or None

def csv():
	"""Call fun on each row. Row cells are divided in the.seperator"""
	pass


def push(t, x):
    t.append(x)
    return x


# Strings
def o(t):
	if type(t) != dict:
		return str(t)

	def show(k, v):
		match_str = re.compile("^_")
		if not re.findall(match_str, str(k)):
			v = o(v)
			return len(t) == 0 and "{}".format(k, v) or str(v)

	u = dict()
	for k, v in t.items():
		u[len(u)] = show(k, v)
	if len(t) == 0:
		sorted(u)
	return u


def oo(t):
	print(o(t))
	return t
