## Run system Command

### using  subprocess
```
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, 
    capture_output=False, shell=False, cwd=None, timeout=None, check=False,
    encoding=None, errors=None, text=None, env=None,    universal_newlines=None)
    
subprocess.run(["ls", "-l"]) 
```
## Multi Processing

### using treading
```
from threading import Thread

def work(id, start, end, result):
	total = 0
	for i in range(start, end):
		total += i
	result.append(total)
	return

if __name__ == "__main__":
	START, END = 0, 100000000
	result = list()
	th1 = Thread(target=work, args=(1, START, END, result))

	th1.start()
	th1.join()

	print(f"Result: {sum(result)}")
```


### using processing

```
from multiprocessing import Process, Queue

def work(id, start, end, result):
	total = 0
	for i in range(start, end):
	total += i
	result.put(total)
	return

if __name__ == "__main__":
	START, END = 0, 100000000
	result = Queue()
	th1 = Process(target=work, args=(1, START, END//2, result))
	th2 = Process(target=work, args=(2, END//2, END, result))

	th1.start()
	th2.start()
	th1.join()
	th2.join()

	result.put('STOP')
	total = 0
	while True:
		tmp = result.get()
		if tmp == 'STOP':
			break
		else:
			total += tmp

	print(f"Result: {total}")

```

# Useful Python Package

## pytest  (testing framework)

```

$ pip install -U pytest

	# content of test_sample.py
	def func(x):
    		return x + 1

	def test_answer():
    		assert func(3) == 5
	#-------------------
	
$ pytest

```

## Hypothesis
https://hypothesis.readthedocs.io/en/latest/
https://hypothesis.works/

pip install hypothesis

```

from hypothesis import given
import hypothesis.strategies as st


@given(st.integers(), st.integers())
def test_ints_are_commutative(x, y):
    assert x + y == y + x
    
```


## Black  (Python code formatter)
https://github.com/psf/black

### yapf (formatter)
https://github.com/google/yapf



##  faster  python

###  PyPy
```
$   sudo apt-get install pypy

$  ./pypy3.5 pystone.py
```

###  Nuitka

```
$   sudo apt-get install Nuitka
$   sudo apt-get install clang

$   nuitka pystone.py
$  ./pystone.exe 500000 
```

