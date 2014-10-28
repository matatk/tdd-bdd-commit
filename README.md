TDD Commit Message
===================

FIXME

Development Environment Set-up
-------------------------------

### First-time Setup

If you haven't got them, get **pip** and **virtualenv**
 * `sudo easy_install pip`
 * `pip install virtualenv`

Create and activate the virtual environment
 * `virtualenv venv`
 * `. venv/bin/activate`

Install/update packages
 * `pip install -r requirements.txt`
 * or `pip install --upgrade -r requirements.txt`

### Day-to-day Development

Activate the virtual environment and set the path for testing
 * `. venv/bin/activate`
 * `export PYTHONPATH=.`

**Note:** if you have [autoenv](https://github.com/kennethreitz/autoenv), the virtualenv script will be automatically sourced when you enter the directory.

The tests can be run continuously with `py.test --looponfail tests` or `py.test -f tests`
