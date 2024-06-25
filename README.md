# Cliologging

![version](https://img.shields.io/badge/version-1.0.0-blue)

The cliologging library is an add-on to the official Python logging library.
Clio is one of the nine Muses, and is the muse of history and annals. This name suggests an ability to record and archive events so that you can keep a log of your projects.

![log-exemple.png](https://i.postimg.cc/nVG2vt3p/log-exemple.png)

**Table of Contents**

- [Installation](#installation)
- [Execution / Usage](#execution--usage)
- [Technologies](#technologies)
- [Features](#features)
- [Contributing](#contributing)
- [Contributors](#contributors)
- [Author](#author)
- [Change log](#change-log)

## Installation

On macOS and Linux:

```sh
$ python -m pip install cliologging
```

On Windows:

```sh
PS> python -m pip install cliologging
```

## Execution / Usage

Here are a few examples of using the cliologging library in your code:

```python
from cliologging import logger

log = logger.create('mylogger', "./log/debug.log")

log.info("This is a information log level message.")
...
```

## Technologies

cliologging uses the following technologies and tools:
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/requests)

## Features

cliologging currently has the following set of features:

- Create logger with a unique alias and a specific path.

## Contributing

To contribute to the development of < project's name >, follow the steps below:

1. Fork cliologging from <https://github.com/julienbltt/cliologging/fork>
2. Create your feature branch (`git checkout -b feature-new`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some new feature'`)
5. Push to the branch (`git push origin feature-new`)
6. Create a new pull request

## Contributors

Here's the list of people who have contributed to cliologging:

- Julien BALDERIOTTI – [@julienbalderiotti](https://www.linkedin.com/in/julien-balderiotti) – julien.blt@outlook.com

The cliologging development team really appreciates and thanks the time and effort that all these fellows have put into the project's growth and improvement.

## Author

Julien BALDERIOTTI – [@julienbalderiotti](https://www.linkedin.com/in/julien-balderiotti) – julien.blt@outlook.com

## Change log

- r1.0.0
    - First publish version