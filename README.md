# python



## todo

  + Data Science


## doing

  + practice_python


## done

  + LA
    - ~~html : find out a way of showing popup txt~~

```
                [new Date(2010,8,1,12,0,0), , '<div title="Actual: popup_report"> my_Report </div><br>' +
                        '<img src="img/attachment-icon.png" style="width:32px; height:32px;">']
```

##  Environment

```
$  sudo pip install virtualenv

$  virtualenv venv

$  source venv/bin/activate

    or  $  .  venv/bin/activate
```

##  Env for testing
```
$ pip install pytest
$ pip install codecov
$ pip install pytest-cov
```
##  testing
```
$  pytest
$  pytest {test*.py}
$  pytest  -s
$  pytest {test*.py} -s

$  pytest  --cov=my_prj/   my_prj/
$  pytest  --cov=my_prj/   my_prj/test_refsm.py

$  pytest  --cov=./                       {test_refsm.py}
$  pytest  --cov=./  --cov-report html    {test_refsm.py}
$  pytest  --cov=./  --cov-report xml
```
##  Python Tools

```
> Code Formatter
>>python 3.6 아래  version   (  Python 3.6.0+  일땐  black) 

  $ pip install yapf
  $ yapf proc_main_log.py -i



```


## idea

  + Log Analayzer (LA)

  
    + LA 
      - task : get hash-value (sha1sum),  unzip file, list files, execut proper proc_** program
      
