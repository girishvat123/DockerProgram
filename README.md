# Steps in Deploying your Python Application using Docker and Puppet

## Prerequisites
1. Github Account
2. Docker Hub /Amazon Container Registry
3. Web server that can deploy Python application with docker installed.
4. A Distelli account (Build,deploy to any server in any programming language)


### Steps

1. Create a dockerfile 
  Sample of it is given in the ```https://github.com/girishvat123/DockerProgram/blob/master/Dockerfile ```
2. Docker file specifies the dependencies, environment to run in and whatever are the commands to run.
3. Install Distalli Agent on your server
4. Build and upload the Docker image.
5. Set up port mappings 
6. Deploy your docker container.
7. Now you can access your ```http://<-You Server’s IP Address->:portAddress ```

