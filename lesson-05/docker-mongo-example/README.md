# Docker environment with Python 3 and MongoDB

1. Download ZIP of this repository.
2. Make sure Docker is running on your computer.
3. Open the terminal (inside the project root) and run `docker-compose up --build -d`. This will run your docker containers in the background.
4. Connect to the dockerized app shell: `docker-compose run app sh`. A shell will open inside your Terminal.
5. Now you can run `python main.py`. You can also do changes in the file.
6. When you want to finish, type `exit` in the shell.
7. Finally, type `docker-compose down` to shut down the containers.

You can also open a MongoDB Admin page on [http://localhost:8081](http://localhost:8081).
