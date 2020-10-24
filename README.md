# Operativa API

[![Documentation Status](https://readthedocs.org/projects/deepspeech/badge/?version=master)](http://deepspeech.readthedocs.io/?badge=master)
[![Task Status](https://github.taskcluster.net/v1/repository/mozilla/DeepSpeech/master/badge.svg)](https://github.taskcluster.net/v1/repository/mozilla/DeepSpeech/master/latest)


SiminchikServer is a server that processes a Speech-To-Text engine (Qillqaq), using a model trained by machine learning techniques, it also store and processes audio files collected (Huqariq). The server can be used to connect to apps, websites or others applications.

**Table of Contents**

- [Prerequisites](#prerequisites)
- [Installing requisites](#installing-requisites)
- [Getting the trained model](#getting-the-trained-model)
- [Using the Quechua model](#using-the-quechua-model)
  - [Using the language model](#using-the-language-model)
  - [Using no the language model](#using-no-the-language-model)
- [Run Qillqaq Server](#run-qillqaq-server)
  - [Local o Dev Server](#local_o_dev_server)
  - [Production Server](#production_server)
- [Recommendations](#recommendations)
- [Code documentation](#code-documentation)
- [Contact](#contact)

## Prerequisites

* [Python 2.7](https://www.python.org/)
* [SOX](http://sox.sourceforge.net/)

## Installing requisites

You need to update the system:

```bash
sudo apt-get update
sudo apt-get upgrade
```

Now you need to install pip:

```bash
sudo apt-get install python-pip
```

Install the required dependencies using pip:

```
sudo git clone https://github.com/rjzevallos/SiminchikServer
cd SiminchikServer
sudo pip install -r requirements.txt
```

Install python-mysql:

```bash
sudo apt-get install python-mysqldb
```

Install ffmpeg:

```bash
sudo apt-get install ffmpeg
```

Now, You have to install mysql, create a database and run .sql script.

Install mysql-server, password "root2":

```bash
sudo apt-get install mysql-server
```

Create a database:

```bash
sudo mysql -p
```

Commands sql:

```
create database app_quechua;
use app_quechua;
source ../QillqaqServer/app_quechua.sql;
```

## Getting the trained model

You have to download the trained Quechua model for performing speech-to-text, also you can download it (along with other important inference material) from the QillqaqServer releases page. Alternatively, you can run the following command to download the files in your current directory:

```bash
sudo wget https://github.com/rjzevallos/QillqaqServer/releases/download/v0.01/5-gram.binary
sudo wget https://github.com/rjzevallos/QillqaqServer/releases/download/v0.01/output_graph.pb
sudo wget https://github.com/rjzevallos/QillqaqServer/releases/download/v0.01/quz_trie
```

## Using the Quechua model without server

There are two ways to use DeepSpeech inference:

```
cd QillqaqServer
```



### Using the language model

```bash
deepspeech --model output_graph.pb --alphabet quz_alphabet.txt --lm 5-gram.binary --trie quz_trie --audio hatispa.wav
```

### Using no the language model

```bash
deepspeech --model output_graph.pb --alphabet quz_alphabet.txt --audio hatispa.wav
```


## Run Qillqaq Server

### Local o Dev Server

```
cd Qillqaq
python service.py
```

### Production Server

We must install:

* Gunicorn : deploy flask app.
* Nginx : proxy inverso.
* Supervisor : monitor and control gunicorn process.

#### Install Gunicorn:

```bash
sudo pip install gunicorn
```

In order to run several processes simultaneously it is necessary to specify the workers, each of the workers is a Unix process that loads the Python application. There is no shared memory between the workers. The suggested number of workers is (2*CPU)+1. For a dual-core machine (2 CPU), 5 is the suggested value workers. In this case 8 workers are being placed.

```bash
gunicorn -w 8  service:app -b 0.0.0:5000
```

#### Install Nginx:

```bash
sudo apt-get update
sudo apt-get install nginx
```

After installing Nginx go to the path /etc/nginx/sites-enabled/ , add a document having the following

```bash
sudo vim /etc/nginx/sites-enabled/virtual.conf
```

```
server {
    listen 80;
    server_name  your_public_dnsname_here;
    
    # write access and error logs to /var/log
    access_log /var/log/proyect_access.log;
    error_log /var/log/proyect_error.log;
    
    location / {
        # forward application requests to the gunicorn server
        proxy_pass http://0.0.0.0:5000/;
    }
}
```

OPTIONAL: In this part make sure to place the route of the FULLCHAIN.PEM and PRIVKEY.PEM only if a certificate has been generated, in this case before the configuration a certificate was generated thanks to LET´S ENCRYPT, for more information go to the following link https://letsencrypt.org/

```
server {
    # listen on port 443 (https)
    listen  443 ssl;
    server_name _;

    # location of the self-signed SSL certificate
    ssl_certificate /etc/letsencrypt/live/www.pucp.tk/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/www.pucp.tk/privkey.pem;

    include snippets/ssl.conf;
    include snippets/letsencrypt.conf;

    # write access and error logs to /var/log
    access_log /var/log/proyect_access.log;
    error_log /var/log/proyect_error.log;

    location / {
        # forward application requests to the gunicorn server
        proxy_pass http://0.0.0.0:5000/;
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

}
```

Finally, save the file and restart Nginx

```bash
sudo systemctl restart nginx
```

#### Install Supervisor:

To configure Supervisor go to the path /etc/supervisor/ and create a conf.d folder, then create a file with extension .conf, finally add what is detailed below.

```
[program:proyect]
directory=/home/ubuntu/proyect
command=gunicorn -w 8 service:app -b 0.0.0:5000
autostart=true
autorestart=true
stderr_logfile=/var/log/proyect/proyect.err.log
stdout_logfile=/var/log/proyect/proyect.out.log
```

Enable configuration, run the following commands:

```bash
sudo supervisorctl reread
sudo service supervisor restart
```

## Recommendations

You server has to be ubuntu 16.04 LTS, 16GB RAM, 125GB SSD.

## Code documentation


## Contact

We are always happy to hear from you:

* Rodolfo Zevallos rjzevallos.salazar@gmail.com 
