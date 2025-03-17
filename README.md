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

