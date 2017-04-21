'''
curl -X POST -d "username=jafrancov&password=Alex8422" http://localhost:8000/api/auth/token/

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImphZnJhbmNvdiIsInVzZXJfaWQiOjEsImVtYWlsIjoiamFmcmFuY292QGdtYWlsLmNvbSIsImV4cCI6MTQ5Mjc4OTk5N30.0i3bm1WeliJEJGdI9A33BFogXniXJP5xhb5pVOj0cjM

curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImphZnJhbmNvdiIsInVzZXJfaWQiOjEsImVtYWlsIjoiamFmcmFuY292QGdtYWlsLmNvbSIsImV4cCI6MTQ5Mjc4OTk5N30.0i3bm1WeliJEJGdI9A33BFogXniXJP5xhb5pVOj0cjM" http://localhost:8000/api/posts/

curl http://localhost:8000/api/posts/

'''