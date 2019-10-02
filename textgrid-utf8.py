#!/usr/bin/env python3
#-*- coding: utf-8 -*-
""" Usage:
      textgrid-utf8.py textgrid
	  
	  Will convert number inside the textgrid file into readable chinese
"""

from ast import literal_eval
import tgt
import sys

def convert_utf8(fn):
	tg = tgt.io.read_textgrid(fn)
	wtier = tg.get_tier_by_name("word")

	for ann in wtier._objects:
		if ann.text != 'sp':
			utf8str = literal_eval("b'{}'".format(ann.text)).decode('utf-8')
			ann.text = utf8str
	tgt.io.write_to_file(tg, fn+".utf8")
	
if __name__ == '__main__':
    try:
        textfile = sys.argv[1]
    except:
        print(__doc__)
        sys.exit(0)
		
convert_utf8(textfile)


