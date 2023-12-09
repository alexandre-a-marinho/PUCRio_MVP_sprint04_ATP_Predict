# # PUCRio_MVP_sprint04_ATP_Predict - Frontend
MVP of the fourth Sprint of the graduate program in Software Engineering at PUC-Rio (**MVP Sprint 04**)

Author: Alexandre Alves Marinho

---
## How to run (development mode):

Just download the project and open the index.html file in your browser.

---
## How to run (Docker mode):

Be sure to have [Docker](https://docs.docker.com/engine/install/) installed and in execution in your machine.

Navigate to the directory containing the Dockerfile in the terminal.
Run **as administrator** the following command to build the Docker image:

```
$ docker build -t front-match-prediction .
```

Once the image is created, to run the container simply execute, **as administrator**, the following command:

```
$ docker run --rm -p 8080:80 front-match-prediction
```

Once running, to access the Frontend, simply open [http://localhost:8080/#/](http://localhost:8080/#/) in the browser.
