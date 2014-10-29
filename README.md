TDD Commit
===========

Helps you stick to the "red", "green"\[, "refactor"\] (and more) pattern of commits when using [Test-driven Development](http://en.wikipedia.org/wiki/Test-driven_development).

Instead of using `git commit ...`, you'd issue `commit red`, `commit green`, and so on.  You'll be asked for a commit message if one's needed, and `git` will be called to make the commit.  Message length limits and quotes inside the messages are handled.

(If this takes off I'd like to support other revision control systems!)

Background
-----------

In [Test-driven Development](http://en.wikipedia.org/wiki/Test-driven_development) there are three main types of commits:

 * "red" after a failing test/part-test;
 * "green" when that test/part passes and
 * "refactor" when changes are made to improve the code's quality along the lines of [DRY](http://en.wikipedia.org/wiki/Don't_repeat_yourself), the [single responsibility principle](http://en.wikipedia.org/wiki/Single_responsibility_principle) and other such guidelines.

Commits should alternate between "red" and "green", with optional refactorings after a "green" commit.  It helps, particularly when performing a Test-driven Development kata, for the commit messages to tell a story (and, for katas, to be only one line, so they can be quickly read). This tool makes it easy to format them into sentences.

**Note:** "green" commits do not need messages, as their purpose should be clear from the preceeding "red" commit.

There are two additional types of commit:

 * "initial" is the first commit and
 * "merge" commits are used when bringing in commits from other branches or repositories.

You will always have an initial commit, and may well use merge commits.  Initial commits do not need messages.  Merges can be carried out after green or refactor commits.

There was some interesting information in this [StackOverflow question and answers on git commit message formatting](http://stackoverflow.com/questions/2290016/git-commit-messages-50-72-formatting).

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
