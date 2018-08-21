#!/usr/bin/env python
import requests

for x in range(0, 10000):
  r = requests.get('http://ip')
  print("SIMPLE\t" + r.text.rstrip("\r\n"))

sess = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=100,pool_maxsize=100)
sess.mount('http://',adapter)

for x in range(0, 10000):
  r = sess.get('http://ip')
  print("PERSISTENT\t" + r.text.rstrip("\r\n"))
