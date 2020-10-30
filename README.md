<!-- PROJECT HEADER -->
# Project Deliver API

The Backend API portion of the Project Delivery App for [Out In Tech U Mentorship Fall 2020](https://outintech.com/).

<!-- PROJECT SHIELDS -->
<!--
[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
-->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Build Status][travisci-shield]][travisci-url]
[![codecov][codecov-shield]][codecov-url]

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Run the App!](#run-the-app!)
  * [Directory Tree](#directory-tree)
  * [Testing](#testing)
    * [Using just `pytest`](#using-just-pytest)
    * [Using `Coverage.py` with `pytest`](#using-coverage.py-with-pytest)
* [Usage](#usage)
* [License](#license)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project

Thanks to the global pandemic, restaurants and food services are struggling to keep their head above water without getting everyone else infected. Thanks to the significant social movement of #BlackLivesMatter, there's a huge focus to support racial justice and struggling BIPOC+-owned businesses.

The significant problem with trying to order food is dealing with the deluge of apps such as [Uber Eats](https://www.ubereats.com/), [GrubHub](https://www.grubhub.com/), [DoorDash](https://www.doordash.com/), etc. And that doesn't even start to include other proprietary apps or ordering through a phone call. And even then, it might not be clear if the app is ordered for pickup or delivery.

This map app utilizing [MapBox](https://www.mapbox.com/) help to aggregate and display all the restaurants that shows delivery and pickup along with their methods and outlets to order safely. This app also allow filtering the restaurants to "BIPOC+-Owned", "LGBTQ+-Owned", "LGBTQ+ Friendly", and "Wheelchair Accessibility" to ensure that everyone should order safely whether it's delivery or driving to pickup their takeout in a safe and contactless manner.

This is the backend portion of the app that integrate betweens the [frontend app](https://github.com/EndyPremier/project-deliver-app) and the database, ready to be deployed in a serverless environment in an API gateway.


### Built With

* **Runtime + Language:** [Python](https://www.python.org/) (Working with 3.8 but can work with 3.6+)
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Testing:** [pytest](https://docs.pytest.org/en/stable/)
* **Coverage:** [Coverage.py](https://coverage.readthedocs.io/)
* **CD/CI:** [Travis CI](https://travis-ci.com/github/EndyPremier/project-deliver-api/)
* **Hosting:** [TBD]


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.


### Prerequisites

Have a valid Python version that can work. This project is being working with version 3.8.6 but CI testing verifys that it works from 3.6+ onward. You can either install the [latest version](https://www.python.org/downloads/) or [this specific version](https://www.python.org/downloads/release/python-386/) at Python's official download page.

However, I recommend using [`pyenv`](https://github.com/pyenv/pyenv) to install your desired version from there.
```sh
$ pyenv install -v 3.8.6
#...
Installed Python-3.8.6 to $HOME/.pyenv/versions/3.8.6
$ pyenv global 3.8.6
$ python -V
Python 3.8.6
```

Aloing with that, I use a plugin called [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv) to manage virtual environments in conjunction with pyenv.


### Installation

1. Clone this repo.
   ```sh
   $ git clone https://github.com/EndyPremier/project-deliver-api.git
   $ cd project-deliver-api
   ```

2. Setup a virtual environment. You can use your virtual environment manager of choice such as [`virtualenv`](https://virtualenv.pypa.io/en/latest/) or [`pipenv`](https://pipenv.pypa.io/en/latest/). This is how you create a virtual environment for pyenv using pyenv-virtualenv.
   ```sh
   $ pyenv virtualenv 3.8.6 deliver-api
   ```

   To make it more convenient, create a file at the project root called `.python-version` so when you reach the directory, it activates the virtual environment that is pointing in `~/.pyenv/versions/` directory.
   ```sh
   # at project root
   $ echo 3.8.6/env/deliver-api > '.python-version'
   ```

3. Install pip packages
   ```sh
   # at project root
   $ pip install -r requirements.txt
   ```


### Run the App!

Just type this command and it will be run on `http://127.0.0.1:8000` to be able to fiddle around.
```sh
# at project root
$ uvicorn deliver.main:app --reload
```

### Directory Tree
```
.
├── deliver
│   ├── models
│   │   ├── __init__.py
│   │   ├── enums.py
│   │   ├── hours.py
│   │   ├── location.py
│   │   ├── services.py
│   │   └── utils.py
│   ├── __init__.py
│   └── main.py
├── tests
│   ├── models
│   │   ├── __init__.py
│   │   ├── test_location.py
│   │   ├── test_restaurant.py
│   │   ├── test_services.py
│   │   └── test_utils.py
│   ├── __init__.py
│   └── test_main.py
├── .gitignore
├── .pylintrc
├── .travis.yml
├── LICENSE
├── README.md
└── requirements.txt
```


### Testing

#### Using just `pytest`
```sh
# at project root
$ python -m pytest
# running test... and then show result
```

#### Using `Coverage.py` with `pytest`
```sh
# at project root
$ python -m coverage run --source=deliver -m pytest
# running test... and then show result
$ python -m coverage report -m
# get coverage report from ".coverage" file from test
```


<!-- USAGE EXAMPLES -->
## Usage

[TBA]


<!-- LICENSE -->
## License

Distributed under the GNU GPL v3 License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

**Mentee:** Endy Iskandar Imam - [LinkedIn][linkedin-url] - [@EndyPremier](https://twitter.com/EndyPremier) - imam.endy@gmail.com

**Mentor:** Rory Chinchilla - [LinkedIn](https://www.linkedin.com/in/r-chinchilla/)

**Project Link:** [https://github.com/EndyPremier/project-deliver-api](https://github.com/EndyPremier/project-deliver-api)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/EndyPremier/project-deliver-api.svg?style=flat-square
[contributors-url]: https://github.com/EndyPremier/project-deliver-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/EndyPremier/project-deliver-api.svg?style=flat-square
[forks-url]: https://github.com/EndyPremier/project-deliver-api/network/members
[stars-shield]: https://img.shields.io/github/stars/EndyPremier/project-deliver-api.svg?style=flat-square
[stars-url]: https://github.com/EndyPremier/project-deliver-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/EndyPremier/project-deliver-api.svg?style=flat-square
[issues-url]: https://github.com/EndyPremier/project-deliver-api/issues
[license-shield]: https://img.shields.io/github/license/EndyPremier/project-deliver-api.svg?style=flat-square
[license-url]: https://github.com/EndyPremier/project-deliver-api/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/endy-imam
[travisci-shield]: https://travis-ci.com/EndyPremier/project-deliver-api.svg
[travisci-url]: https://travis-ci.com/EndyPremier/project-deliver-api
[codecov-shield]: https://codecov.io/gh/EndyPremier/project-deliver-api/branch/main/graph/badge.svg?token=GUKQH21BIS
[codecov-url]: https://codecov.io/gh/EndyPremier/project-deliver-api
