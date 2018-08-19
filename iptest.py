#!/usr/bin/env python
import requests

for x in range(0, 10000):
  r = requests.get('http://ip')
  print("SIMPLE\t" + r.text)

for x in range(0, 10000):
  r = requests.get('http://ip')
  print("PERSISTENT\t" + r.text.rstrip("\r\n"))
