#!/usr/bin/env python
from livereload.task import Task
import json
import subprocess

def f():
    subprocess.call(("nikola", "build"))

fdata = json.loads('''["conf.py", "themes", "templates", "galleries", "posts", "stories", ""]''')

for watch in fdata:
    Task.add(watch, f)