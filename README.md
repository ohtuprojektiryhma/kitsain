# [Kitsain](https://github.com/ohtuprojektiryhma/kitsain)

[![Pipeline](https://github.com/ohtuprojektiryhma/kitsain/actions/workflows/main.yml/badge.svg)](https://github.com/ohtuprojektiryhma/kitsain/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/ohtuprojektiryhma/kitsain/graph/badge.svg?token=DD0OPAD9B2)](https://codecov.io/gh/ohtuprojektiryhma/kitsain)

## About
This repository is for a backend software that has an API where food ingredients at hand are sent and the software calls OpenAI API to retrieve recipe suggestions for those ingredients. Documentation for API endpoints can be found [here](./documentation/restapidocs.md).

By University of Helsinki students for [the software engineering project course](https://studies.helsinki.fi/kurssit/toteutus/otm-4dab3f07-4ba7-4ae1-a269-ee1e0817c66c/TKT20007/Ohjelmistoprojekti). 


## [Definition of Done:](https://github.com/ohtuprojektiryhma/kitsain/blob/main/documentation/dod.md)
The requirement has been analyzed (acceptance criteria created), planned (divided into technical tasks), programmed, tested with tests that bring value (with minimum coverage of 80%), testing automated (CI-pipeline), documented (with Readme file) and merged into main production branch.

## [Backlog](https://github.com/orgs/ohtuprojektiryhma/projects/1)

The backlog is set to private according to our customers wishes.

## Documentation of our process

- [Working time sheet](https://github.com/ohtuprojektiryhma/kitsain/wiki/Työaikakirjanpito)

- [Customer meeting notes](https://github.com/ohtuprojektiryhma/kitsain/wiki/Asiakastapaamisten-muistiinpanot)

- [Retrospectives](https://github.com/ohtuprojektiryhma/kitsain/wiki/Retrospektiivit)


# Installation

1. Clone repository to computer
2. Go to root folder
3. Install Docker
4. Create a .env file that contains the variable OPENAI_API_KEY, set as your OpenAI API key


Then run these commands:

```cmd
docker build -t kitsain .
```

```cmd
docker run -it --rm -p 5000:5000 kitsain
```

Now the application is running on localhost, and you can [send requests](./documentation/restapidocs.md) to the API!

