# Qillqaq Server

[![Documentation Status](https://readthedocs.org/projects/deepspeech/badge/?version=master)](http://deepspeech.readthedocs.io/?badge=master)
[![Task Status](https://github.taskcluster.net/v1/repository/mozilla/DeepSpeech/master/badge.svg)](https://github.taskcluster.net/v1/repository/mozilla/DeepSpeech/master/latest)

**Table of Contents**

- [Prerequisites](#prerequisites)
- [Installing requisites](#installing-requisites)
- [Using the Quechua model without server](#using-the-quechua-model-without-server)
  - [Getting the trained model](#getting-the-trained-model)
  - [Using the language model](#using-the-language-model)
  - [Using no the language model](#using-no-the-language-model)
- [Run Qillqaq Server](#run-qillqaq-server)
- [Recommendations](#recommendations)
- [Code documentation](#code-documentation)
- [Contact](#contact)

## Prerequisites

* [Python 2.7](https://www.python.org/)
* [SOX](http://sox.sourceforge.net/)
* [DeepSpeech](https://github.com/mozilla/DeepSpeech/blob/2f9b551326f63db11b0f1533e8ce88ef5e3cf305/README.md#project-deepspeech)

## Installing requisites

You need to update the system:

```bash
sudo apt-get update
sudo apt-get grade
```

Now you need to install pip:

```bash
sudo apt-get install python-pip
```

Install the required dependencies using pip:

```bash
cd QillqaqServer
sudo pip install -r requirements.txt
```

Install python-mysql:

```bash
sudo apt-get install python-mysqldb
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

```bash
create database app_quechua;
use app_quechua;
source ../QillqaqServer/app_quechua.sql;
```


## Using the Quechua model without server

There are two ways to use DeepSpeech inference:

```bash
cd QillqaqServer
```

### Getting the trained model

You have to download the trained Quechua model for performing speech-to-text, also you can download it (along with other important inference material) from the QillqaqServer releases page. Alternatively, you can run the following command to download and unzip the files in your current directory:

```bash
sudo wget -O - https://github.com/rjzevallos/QillqaqServer/releases/download/v0.01/5-gram.binary
sudo wget -O - https://github.com/rjzevallos/QillqaqServer/releases/download/v0.01/output_graph.pb
sudo wget -O - https://github.com/rjzevallos/QillqaqServer/releases/download/v0.01/quz_trie
```

### Using the language model

```bash
deepspeech --model output_graph.pbmm --alphabet quz_alphabet.txt --lm 5-gram.binary --trie quz_trie --audio hatispa.wav
```

### Using no the language model

```bash
deepspeech --model output_graph.pb --alphabet quz_alphabet.txt --audio hatispa.wav
```


## Run Qillqaq Server

```bash
cd Qillqaq
python server.py
```

## Recommendations

You server has to be ubuntu 16.04 LTS, 16GB RAM, 125GB SSD.

In server.py can change the root where audio files are saving.


## Code documentation

Documentation (incomplete) for the code can be found here: https://docs.google.com/document/d/1nOP5HCoASVtoykoC3LNMzKZEPyz-cU86YubEAo4COxw/edit

## Contact

We are always happy to hear from you:

rjzevallos.salazar@gmail.com 
camacho.l@pucp.pe
