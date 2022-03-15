# BackendTest

Small API that lists android applications

### Usage

```
git clone https://github.com/hmesnard/BackendTest && cd BackendTest
docker-compose up
```
Access the API through : http://127.0.0.1:8000

Endpoint : /api/applications/

GET request lists all applications that are stored and some metadata from them.

POST allows to upload a .apk file and stores it in the database along with the metadata extracted from it.
