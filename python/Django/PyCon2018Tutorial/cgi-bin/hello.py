#!/usr/bin/env python
from datetime import datetime
from sys import version_info
import os

print("Content-type: text/plain")
print()
print("Hello at", datetime.now())
print(version_info)
print(os.environ)
