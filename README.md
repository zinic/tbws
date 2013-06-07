# The Big Webservice

### A Fun Coding Exercise

Hello fellow developer! I have completed this webservice according to a number of requirements
handed to me by my business people. I'd like you to take a look at it and send me a pull request
of everything you would change to make it production ready!

I'd do the work myself, normally, however there are ants in my house that require my full
and undivided attention to defeat.

Good luck!

### Running TBWS
```bash
pip install -r tools/pip-requires
pip install -r tools/test-requires
gunicorn tbws.service:app
```

### TBWS API

POST & PUT /things/put/{key}

GET /things/get/{key}

GET /things/get_largest
