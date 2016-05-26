# timeago

A python lib format datetime to `*** time ago` statement.

[![Build Status](https://travis-ci.org/hustcc/timeago.svg?branch=master)](https://travis-ci.org/hustcc/timeago) [![PyPi Status](https://img.shields.io/pypi/v/timeago.svg)](https://pypi.python.org/pypi/timeago) [![Python Versions](https://img.shields.io/pypi/pyversions/timeago.svg)](https://pypi.python.org/pypi/timeago) [![PyPi Downloads](https://img.shields.io/pypi/dm/timeago.svg)](https://pypi.python.org/pypi/timeago)

Such as: 

> just now
> 12 seconds ago
> 3 minutes ago
> 2 hours ago
> 24 days ago
> 6 months ago
> 2 years ago

or Chinese locale statement.

## Install

```sh
pip install timeago
```


## Usage & Example

```py
import timeago, datetime

now = datetime.datetime.now() + datetime.timedelta(seconds = 60 * 3.4)

print (timeago.format(date, now)) # will print 3 minutes ago
```


## Methor & Parameter

only one API **`format`**.

Three parameters of method `format`:

 - `date`: `datetime` will be done / format.
 - `now`: reference time, must be instance of `datetime`.
 - `locale`: the locale code, only zh_CN / en supported, default `en`.



## Localization

1. foke the project
2. add <locale>.py file in the locales folder.
3. pull a request.