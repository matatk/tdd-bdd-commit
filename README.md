TDD/BDD Commit
==============

Your commit log should tell the story of your code!

This tool helps you keep to the 'red-green-refactor' (and more) pattern of commits when using [test-driven development](http://en.wikipedia.org/wiki/Test-driven_development) or [behaviour-driven development](http://en.wikipedia.org/wiki/Behavior-driven_development) and supports you in explaining the rationale for changes (as well as just listing them). The goal is to document the journey your code takes, and make the commit log informative and even fun to read.

Instead of using `git commit ...`, you'd issue `commit red`, `commit green`, and so on. You can provide a commit message if one's needed, and `git` will be called to make the commit. Best practices involving messages and line lengths are handled, and a 'notepad' is provided so you can keep notes on a commit as you work on it (but remember that taking small steps often is part of the Zen of TDD :-)).

![Graph of commit states (described below)](graph/commit-states.png)

(The central 'red-green-refactor' cycle is depicted \[in black\], with the additional commit types around the outside \[in slate blue\].)

Background
----------

In [test-driven development](http://en.wikipedia.org/wiki/Test-driven_development) and [behaviour-driven development](http://en.wikipedia.org/wiki/Behavior-driven_development) there are three main types of commits:

-   'red' after a failing test/part-test;
-   'green' when that test/part passes, and
-   'refactor' when changes are made to improve the code's quality along the lines of [DRY](http://en.wikipedia.org/wiki/Don't_repeat_yourself), the [single responsibility principle](http://en.wikipedia.org/wiki/Single_responsibility_principle) and other such guidelines.

Commits should alternate between 'red' and 'green', with optional (though highly-recommended) refactorings after a 'green' commit. It helps, particularly when performing a test-/behaviour-driven development kata, for the commit messages to tell a story (and for their summary lines to be clear and concise, so they can be quickly read). This tool makes it easy to format commit messages. (Note that 'green' commits do not need messages, as their purpose should be clear from the preceding 'red' commit.)

There are three additional types of commit (one is only used once per project):

-   'initial' is the first commit (and needs no message);
-   'merge' commits are used when bringing in commits from other branches or repositories, and
-   'beige' commits affect parts of the project that are outside the remit of TDD, such as (some) documentation and static assets -- do think carefully whether a green-red pattern would be more suitable, though!

Commit Messages
---------------

**Note:** this is not actually implemented yet ;-).

Commit messages have two parts:

-   A summary line that identifies the kind of commit (e.g. red or green) and, briefly, its nature.
-   An optional body, which provides more details.

Specify a summary on the command line:

    commit red 'sprocket should fit into widget'

This will translate into the following summary line for the commit under `git log`:

    RED Sprocket should fit into widget

Any command flags are passed through to `git`.

    commit -a green

You will be warned if the summary line exceeds 50 characters; if it exceeds 75 characters it will not be allowed.

You can write the body of the commit message in a 'CHANGES' file in the root of the repository. A good format for this file would be an explanation of the rationale behind the commit, or perhaps an asterisk-bulleted list of changes (though if the commit changes a lot in one go, it might be better to split it up).

The 'CHANGES' file is emptied after a successful commit, so you can start again.

### Example CHANGES files

It can be good for the body of the commit message to read in a narrative manner. For example, for the first test in a 'Noughts and Crosses' TDD kata, entitled ['RED Test that a legal move is legal '](https://github.com/matatk/NoughtsAndCrosses/commit/9fd202591dd97031627da318a2706152aa4cf7c2), the following commit message body was used.

    We are aiming to write Noughts and Crosses using Keith Braithwaite's
    'Test-driven development as if you meant it' ethos.

    We are starting from the is_legal (to be) method, that checks the
    validity of a proposed move.  Our first test is somewhat contrived due
    to the restrictions of the process.

    It seems more natural to approach TDDAIYMI in a bottom-up, as opposed to
    to-down, manner.

Here's a fairly traditional CHANGES file:

    * Fix recurring issue with the chameleon circuit
    * Add extra stabilisation routine to flux capacitor

**Note:** the lines in the CHANGES file are not auto-wrapped; `git`'s suggested line length is 72 characters.

### Editor Auto-wrapping

If you are using Vim, you can set it up to provide line-wrapping at 72 characters for any file called 'CHANGES' by including the following in your vimrc.

```vim
autocmd BufNewFile,BufRead CHANGES set textwidth=72
```

It is also useful to ensure that spell-checking is enabled.

### Reference Information

-   There was some interesting information in this [StackOverflow question and answers on git commit message formatting](http://stackoverflow.com/questions/2290016/git-commit-messages-50-72-formatting).

Development Environment Set-up
------------------------------

### First-time Setup

If you haven't got them, get **pip** and **virtualenv**

-   `sudo easy_install pip`
-   `pip install virtualenv`

Create and activate the virtual environment

-   `virtualenv .venv`
-   `. .venv/bin/activate`

Install/update packages

-   `pip install -r requirements.txt`
-   or `pip install --upgrade -r requirements.txt`

### Day-to-day Development

Activate the virtual environment and set the path for testing

-   `. .venv/bin/activate`
-   `export PYTHONPATH=.`

**Note:** if you have [autoenv](https://github.com/kennethreitz/autoenv), the virtualenv script will be automatically sourced when you enter the directory.

The tests can be run continuously with `py.test --looponfail tests` or `py.test -f tests`.
