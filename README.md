# Install python poetry

For Debian-based Linux, use:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

# Check poetry version

```bash
(base) ┌──(klx㉿kali)-[~/learn-python-poetry]
└─$ poetry --version
Poetry (version 2.1.1)
(base) ┌──(klx㉿kali)-[~/learn-python-poetry]
```

# Init with poetry

```bash
(base) ┌──(klx㉿kali)-[~/learn-python-poetry]
└─$ poetry init

This command will guide you through creating your pyproject.toml config.

Package name [learn-python-poetry]:
Version [0.1.0]: 
Description []:  Learn how python poetry works
Author [klxcoder <klxcoder@gmail.com>, n to skip]:
License []:
Compatible Python versions [>=3.9]:

Would you like to define your main dependencies interactively? (yes/no) [yes]
        You can specify a package in the following forms:
          - A single name (requests): this will search for matches on PyPI
          - A name and a constraint (requests@^2.23.0)
          - A git url (git+https://github.com/python-poetry/poetry.git)
          - A git url with a revision         (git+https://github.com/python-poetry/poetry.git#develop)
          - A file path (../my-package/my-package.whl)
          - A directory (../my-package/)
          - A url (https://example.com/packages/my-package-0.1.0.tar.gz)

Package to add or search for (leave blank to skip): 

Would you like to define your development dependencies interactively? (yes/no) [yes] 
Package to add or search for (leave blank to skip): 

Generated file

[project]
name = "learn-python-poetry"
version = "0.1.0"
description = "Learn how python poetry works"
authors = [
    {name = "klxcoder",email = "klxcoder@gmail.com"}
]
readme = "README.md"
requires-python = ">=3.9"
dependencies = [
]


[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes]
(base) ┌──(klx㉿kali)-[~/learn-python-poetry] (main)
└─$ 

```

# Use poetry to install requests

```bash
(base) ┌──(klx㉿kali)-[~/learn-python-poetry] (main)
└─$ poetry add requests
Creating virtualenv learn-python-poetry-NMAWV853-py3.9 in /home/klx/.cache/pypoetry/virtualenvs
Using version ^2.32.3 for requests

Updating dependencies
Resolving dependencies... (1.7s)

Package operations: 5 installs, 0 updates, 0 removals

  - Installing certifi (2025.1.31)
  - Installing charset-normalizer (3.4.1)
  - Installing idna (3.10)
  - Installing urllib3 (2.3.0)
  - Installing requests (2.32.3)

Writing lock file

(base) ┌──(klx㉿kali)-[~/learn-python-poetry] (main)
└─$ 

```

# Use poetry to install dev dependency pytest

```bash
(base) ┌──(klx㉿kali)-[~/learn-python-poetry] (main)
└─$ poetry add --dev pytest
Using version ^8.3.5 for pytest

Updating dependencies
Resolving dependencies... (2.6s)

Package operations: 6 installs, 0 updates, 0 removals

  - Installing exceptiongroup (1.2.2)
  - Installing iniconfig (2.0.0)
  - Installing packaging (24.2)
  - Installing pluggy (1.5.0)
  - Installing tomli (2.2.1)
  - Installing pytest (8.3.5)

Writing lock file

(base) ┌──(klx㉿kali)-[~/learn-python-poetry] (main)
└─$ 

```

```bash
(base) ┌──(klx㉿kali)-[~/learn-python-poetry] (main)
└─$ poetry shell

Looks like you're trying to use a Poetry command that is not available.

Since Poetry (2.0.0), the shell command is not installed by default. You can use,

  - the new env activate command (recommended); or
  - the shell plugin to install the shell command

Documentation: https://python-poetry.org/docs/managing-environments/#activating-the-environment

Note that the env activate command is not a direct replacement for shell command.

(base) ┌──(klx㉿kali)-[~/learn-python-poetry] (main)
└─$
```

# Try "poetry run python -V"

```bash
(base) ┌──(klx㉿kali)-[~/learn-python-poetry] (main)
└─$ python -V                          
Python 3.9.18

(base) ┌──(klx㉿kali)-[~/learn-python-poetry] (main)
└─$ poetry run python -V
Python 3.9.18

(base) ┌──(klx㉿kali)-[~/learn-python-poetry] (main)
└─$ 

```

# example.py

```bash
(base) ┌──(klx㉿kali)-[~/learn-python-poetry] (main)
└─$ poetry run python example.py
Your IP address is: 42.1.87.169

(base) ┌──(klx㉿kali)-[~/learn-python-poetry] (main)
└─$ 
```

# Show info about `requests`

```bash
(base) ┌──(klx㉿kali)-[~/learn-python-poetry] (main)
└─$ poetry run python -m pip show requests
Name: requests
Version: 2.32.3
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache-2.0
Location: /home/klx/.cache/pypoetry/virtualenvs/learn-python-poetry-NMAWV853-py3.9/lib/python3.9/site-packages
Requires: certifi, charset-normalizer, idna, urllib3
Required-by:

(base) ┌──(klx㉿kali)-[~/learn-python-poetry] (main)
└─$ python -m pip show requests
Name: requests
Version: 2.31.0
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache 2.0
Location: /home/klx/miniconda3/lib/python3.9/site-packages
Requires: certifi, charset-normalizer, idna, urllib3
Required-by: conda, conda_package_streaming, huggingface-hub, jupyterlab_server, localstack-core, localstack-ext, pooch, spacy, tensorflow, transformers, ultralytics, weasel, yarg, youtube-transcript-api

(base) ┌──(klx㉿kali)-[~/learn-python-poetry] (main)
└─$ 

```

