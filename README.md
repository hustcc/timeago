# timeago

A very simple python lib, used to format datetime with `*** time ago` statement. Javascript version here. [timeago.js](https://github.com/hustcc/timeago.js).

[![Build Status](https://travis-ci.org/hustcc/timeago.svg?branch=master)](https://travis-ci.org/hustcc/timeago) [![PyPi Status](https://img.shields.io/pypi/v/timeago.svg)](https://pypi.python.org/pypi/timeago) [![Python Versions](https://img.shields.io/pypi/pyversions/timeago.svg)](https://pypi.python.org/pypi/timeago) [![PyPi Downloads](https://img.shields.io/pypi/dm/timeago.svg)](https://pypi.python.org/pypi/timeago)

Such as: 

```
just now
12 seconds ago
3 minutes ago
2 hours ago
24 days ago
6 months ago
2 years ago

in 12 seconds
in 3 minutes
in 2 hours
in 24 days
in 6 months
in 2 years
```

or Chinese locale statement.

## Install

```sh
pip install timeago
```


## Usage & Example

```py
import timeago, datetime

now = datetime.datetime.now() + datetime.timedelta(seconds = 60 * 3.4)

# locale
print (timeago.format(date, now, locale='zh_CN')) # will print 3分钟后

# input datetime
print (timeago.format(date, now)) # will print 3 minutes ago

# input timedelta
print (timeago.format(datetime.timedelta(seconds = 60 * 3.4))) # will print 3 minutes ago

# input date, auto add time(0, 0, 0)
print (timeago.format(datetime.date(2016, 5, 27), now))

# input date
print (timeago.format(datetime.date(2016, 5, 27), now))

# input datetime formated string
print (timeago.format('2016-05-27 12:12:12', '2016-05-27 12:12:03')) # will print just now
```


## Methor & Parameter

only one API **`format`**.

Three parameters of method `format`:

 - **`date`**: the parameter which will be formated, must be instance of `datetime` / `timedelta` or datetime formated string.
 - **`now`**: reference time, must be instance of `datetime` or datetime formated string.
 - **`locale`**: the locale code, only **zh_CN** / **en** supported, default `en`. Other locale, you can pull request.



## Localization

1. foke the project
2. add `locale.py` file in the locales folder.
3. pull a request.
