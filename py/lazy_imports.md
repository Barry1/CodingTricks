---
title: import hints for python
date: 2026-09-11
author: Dr. Bastian Ebeling
---

The two articles <https://pythontest.com/python-lazy-imports-now> and <https://realpython.com/python315-lazy-imports> show interesting aspects on importing in python and timing consequences.

Hopefully beginning with Python 3.15 we will have lazy importing - but at least until then we need to take care.
The mimic is partially described [here](https://peps.python.org/pep-0810/#how-do-lazy-imports-interact-with-dir-getattr-and-module-introspection).

A solution idea for versions before 3.15 is described [here](https://medium.com/@RampantLions/dynamic-lazy-loading-module-proxies-in-python-getattr-dir-and-on-demand-import-09aa173e2321)

For measuring import times, try the following command on your script: 


```python 
python -X importtime YOUR_SCRIPT.py 2>&1 >/dev/null | grep -E '\| [^ ]' | sort -t'|' -k2 -rn | head -6
```

