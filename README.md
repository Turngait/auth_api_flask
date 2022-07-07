# Auth API
## powered by Flask
### v. 0.1b0

Template AuthAPI on Flask for my own pet-projects.

## Requirements
```
git
docker
docker-compose
```

## Local setup
```
git clone https://github.com/Turngait/auth_api_flask.git auth_api
cd auth_api
make init
```
or you can do it manually
```
cp .env.example .env
docker-compose build
```
Then fill all fields in .env .

```
docker-compose up
```

<br/>

## **Releases**
### July 05 - 0.1b0
Betta version release ready.
### June 30 - 0.3a0
Add logger.

### June 03 - 0.2a1
Change Dokerfile image.
### June 01 - 0.2a0
Complete "check api key" flow.

### May 31 - 0.1a4
Add create api key function.
