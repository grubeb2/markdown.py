"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

for line in fileinput.input():
  line = line.rstrip() 
  if line[0] == '>':
    line = '<blockquote>' + line[1:].lstrip() + "</blockquote>"
  elif len(line) > 3 and line[:3] == '###':
    line = '<h3>' + line[3:].lstrip() + '</h3>'
  elif len(line) > 2 and line[:2] == '##':
    line = '<h2>' + line[2:].lstrip() + '</h2>'
  elif len(line) > 1  and line[:1] == '#':
    line = '<h1>' + line[1:].lstrip() + '</h1>'
  line = convertStrong(line)
  line = convertEm(line)
  print '<p>' + line + '</p>',

