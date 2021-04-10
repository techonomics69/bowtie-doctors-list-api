# necktie-doctors-list-api
Doctors List API for Necktie

# Requirement
Docker

# Getting Started
Simply open the project in VSCode using the devcontainer and navigate to http://localhost:8080/doctor!

# Alternatively
- build the project for with `docker build --target prod -t ronaldslc/necktie-doctors-list-api -f docker/doctors-api/Dockerfile src` in the project root. 
- run with `docker run -it -p 8000:8000 ronaldslc/necktie-doctors-list-api`
- navigate to `http://localhost:8000/doctor/?district=SSP&price_range=1,1000`
- test with `docker run -it ronaldslc/necktie-doctors-list-api -c "python manage.py test"`