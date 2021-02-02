# Dockerize-datetime-Flask-API

## How to Run

    docker ps # displays containers
    docker kill container-name # deletes containers
    docker images # check images
    docker image ls # checks images list
    docker rmi -f $(docker images -q) # kill all images
    #go inside folder containing app.py, Dockerfile and requirements.txt through powershell and enter following commands

    docker build -t docker1:latest .       # Docker Build: build docker using this file
    docker images # Now we can see what we created.
    docker ps  # But, is it running? Nope
    docker run -p 5000:5000 docker1:latest # Docker Run
    docker ps # Okay, now we can see it is running!

    END RESULT:  curl http://127.0.0.1:5000/

## How to Scale-Up
> In order to scale up more instances can be launched using dockers with Kubernates, But if the application is hosted on AWS. AWS Elastic BeanStalk has load balancer and it scales automatically based on your scaling parameter.
