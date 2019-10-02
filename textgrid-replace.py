#!/usr/bin/env python3
""" Usage:
      textgrid-replace textgridfile tradition_pos_file

      textgridfile: The TextGrid file
      tradition_pos_file: The corresponding Chinese text
      The result will be stored as the original TextGrid file plus suffix .rep
"""

import sys
import tgt

def textgrid_replace(txtgrid, tradchin):
    data = [line.strip().split() for line in open(tradchin, 'r')]
    #print(data)
    flat_list = [item for sublist in data for item in sublist]
    #print(flat_list)
    
    tg = tgt.io.read_textgrid(txtgrid)
    
    namelist = tg.get_tier_names()
    
    wtname = [s for s in namelist if "word" in s.lower()]
    #print("Word tier name: ", wtname[0])
    if wtname != "":
        wtier = tg.get_tier_by_name(wtname[0])
        objlen = 0
        for ann in wtier._objects:
            if ann.text != 'sp' and ann.text != '':
                objlen = objlen + 1
        if objlen != len(flat_list):
            print("TextGrid:", objlen, "POS :", len(flat_list), "Length not equal")
            exit(-1)
        else:
            idx = 0
            for ann in wtier._objects:
                if ann.text != 'sp' and ann.text != '':
                    ann.text = flat_list[idx]
                    idx = idx + 1
        tgt.io.write_to_file(tg, txtgrid+".rep")
        
if __name__ == '__main__':
    try:
        # get the three mandatory arguments
        txtgrid = sys.argv[1]
        tradchin = sys.argv[2]
    except:
        print(__doc__)
        sys.exit(0)

textgrid_replace(txtgrid, tradchin)
