#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Diff two pandoc-compatible documents (e.g. .docx-files) as markdown with Kaleidoscope's ksdiff tool."""

# Make sure pandoc and ksdiff are in PATH!

import sys, os, subprocess, tempfile

def panconv(inputfile):
	"""Convert inputfile to a markdown string with pandoc"""

	o = subprocess.check_output(['pandoc', '-t', 'markdown', inputfile])

	return o

def panpan(m):
	"""Convert a file and extract label"""
	r = panconv(m)
	nr = os.path.basename(m)

	return r, nr

def runksdiff(a,b):
	"""Run Kaleidoscope's ksdiff to compare the files and block until closed"""

	# Convert files
	a,na = panpan(a)
	b,nb = panpan(b)

	# Store markdown temorarily
	with tempfile.NamedTemporaryFile(prefix=na + '_') as ta, tempfile.NamedTemporaryFile(prefix=nb + '_') as tb:
		# Write content
		ta.write(a)
		tb.write(b)

		# Run ksdiff
		print('A: ' + ta.name)
		print('B: ' + tb.name)
		subprocess.check_output(['ksdiff', '--wait', ta.name, tb.name])

def main(args):
	if len(args) < 2:
		print('''Usage: %(script)s fileA fileB\nDiff the files using Kaleidoscope's ksdiff tool after converting to markdown.''' % {'script': os.path.basename(__file__)})
		sys.exit(1)
	runksdiff(args[0], args[1])

	#diff = diffdocs(args[0], args[1])
	#print('\n'.join(diff))

#def diffstrings(a,b,na,nb):
#	"""Diff two strings"""
#	a, b = a.splitlines(), b.splitlines()
#
#	import difflib
#
#	diff = difflib.context_diff(a, b, na, nb, n=10)
#	return diff
#
#def diffdocs(x,y):
#	"""Diff the documents"""
#	a,na = panpan(x)
#	b,nb = panpan(y)
#
#	diff = diffstrings(a, b, na, nb)
#	return diff
	
if __name__ == '__main__':
	main(sys.argv[1:])
