#Node.js, Express & MySQL Tutorial.


1. npm install mysql
2. npm install express
3. npm install dotenv
4. npm install nodemon - everytime we make changes to the script it will automatically at it to the server.
5. npm install cors
5. to start server "nodemon app"

DOCKER 

1. docker ps give a list of all running containers on your system
2.docker build -t tedy97/demoapp:1.0 .
3. inorder to run the container for other people to pull for it enterintoterminal  - docker run ba03b164614450cb02f38cfdf71b8bbce1f55aaf3d5b0d96bb95402b68e3
4. Port Forwarding : docker run -p 5000:8081 + (sha256 encryption)
5. Volume - is a dedicated folder on the container. In this file you can share files that can be remounted on other containers. docker volume create my-vol , list volumes - docker volume ls , 
inspect a volume - docker volume inspect (name of container) , remove a volume- docker volume rm (name of container)

Start a docker container w/ a volume
1. docker run -d \
   --name devtest
   --mount source=myvol2,target=/app
   nginx:latest

Multipul Containers (MYSQL example) - 
in order to start a container with an instance of mysql running run: docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=1234qwerASDF" -p 8083:8083 --name sql1 -d mcr.microsoft.com/mssql/server:2019-latest
     the -p followed my 2 ports is an example of portforwarding routing the internal port to a external port.

 (POSTgresSQL config ) -
1. docker run ==== is the command used to create and run a new container based on an already downloaded image.
2.--name myPostgresDb ==== is the name we assign to the container that we are creating.
3. -p 5455:5432 === is the port mapping. Postgres natively exposes the port 5432, and we have to map that port (that lives within Docker) to a local port. In this case, the local 5455 port maps to Docker's 5432 port.
4.-e POSTGRES_USER=postgresUser, -e POSTGRES_PASSWORD=postgresPW, and -e POSTGRES_DB=postgresDB === set some environment variables. Of course, we're defining the username and password of the admin user, as well as the name of the database.
5.-d === indicates that the container run in a detached mode. This means that the container runs in a background process.
6. postgres === is the name of the image we are using to create the container.

                                                                              !!!!!!!!!!
 !!! If you forgot which environment variables you've defined for that container, you can retrieve them using Docker Desktop or by running docker exec myPostgresDb env!!!
 docker exec -it  myPostgresDB env - open up terminal inside container


 (XAMPP)

 Open the Products file location 
 start the Apache and MySQL services. If you run into any problems check teh config files and chage the ports.

takes click admin on MYSQL and it'll take you MYSQL ADMIN site add database 

  for the scope of this project :
  
  privileges: User account 'web_app'@'localhost' - Database web\_app 
  password : test123

  nodemon app