# The Big Webservice

### Running
```bash
gunicorn tbws.service:app
```

### API

POST & PUT /things/put/{key}
GET /things/get/{key}
GET /things/get_largest
