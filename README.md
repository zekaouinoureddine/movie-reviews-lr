[![PyPI - License](https://img.shields.io/badge/license-MIT-green.svg)](/LICENSE)
[![CI/CD](https://github.com/DamZiobro/serverless-fastapi/workflows/CI/CD/badge.svg)](https://github.com/zekaouinoureddine/movie-reviews-lr/actions/workflows/cicd.yml)

# Automate CI/CD pipelines with GitHub Actions
Deploy a Machine Learning model using FastAPI and automate test pipelines with GitHub Actions.

## Tech Stack
- [x] Scikit-Learn
- [x] FastAPI
- [x] pytest
- [x] Docker

## Installation
* ***Clone it***

Clone the repository, move to the project directory, then:
  1. Creat a virtual env
  2. Install the needed packages and dependencies
  3. Run the server

```
$ git clone https://github.com/zekaouinoureddine/movie-reviews-lr.git
$ cd movie-reviews-lr
$ conda create --name mrenv python==3.10.9
$ pip install -r requirements.txt
$ uvicorn src.main:app --reload
```

* ***Dockerize it***

Build the image and fire up the container:
```
docker build --tag mrlr .
docker run -d --name mrlr -p 8000:8000 mrlr
```

* ***Run it***

To ensure if the app is running, open you favorite browser then go to [127.0.0.1:8000](http://127.0.0.1:8000/). You should see the following message in the browser:

```
{"message": "The API is working ..."}
```

* ***Test it***

Once you make sure your API is running on the local server or in the Docker container go to [127.0.0.1:8000/docs](http://127.0.0.1:8000/docs). Here, you can test your API using some examples.


* ***Stop it***

Before moving on, dont forget to bring down the container:

```
$ docker stop mrlr
```

## cURL
cURL is a command-line tool for sending HTTP requests. It supports various protocols such as HTTP, HTTPS, FTP, and many more. It can be used to send and receive data from a server, and is often used for testing APIs and debugging network issues. cURL is available for most operating systems, including Windows, Mac, and Linux. Ensure that it is installed on your machine, then type:

```c
curl -X "GET" "http://127.0.0.1:8000/predict/?review=I%20like%20this%20amazing%20movie" -H "accept: application/json"
```

Output

```JSON
{
  "success": true,
  "result": {
    "sentiment": "Positive",
    "positive prediction": 0.6022566919053794,
    "negative prediction": 0.39774330809462055,
    "time": 0.020993947982788086
  }
}
```

Amazing job!

## Author Infos

If you like it, give it a ⭐, then follow me on:
- LinkedIn: [Nour Eddine ZEKAOUI](https://www.linkedin.com/in/nour-eddine-zekaoui-ba43b1177/)
- Twitter: [@NZekaoui](https://twitter.com/NZekaoui)

---
[![](https://img.shields.io/badge/BACK%20TO-THE%20TOP-blue)](#automate-cicd-pipelines-with-github-actions)