# Qillqaq Server

[![Documentation Status](https://readthedocs.org/projects/deepspeech/badge/?version=master)](http://deepspeech.readthedocs.io/?badge=master)
[![Task Status](https://github.taskcluster.net/v1/repository/mozilla/DeepSpeech/master/badge.svg)](https://github.taskcluster.net/v1/repository/mozilla/DeepSpeech/master/latest)

Project DeepSpeech is an open source Speech-To-Text engine, using a model trained by machine learning techniques, based on [Baidu's Deep Speech research paper](https://arxiv.org/abs/1412.5567). Project DeepSpeech uses Google's [TensorFlow](https://www.tensorflow.org/) project to make the implementation easier.


**Table of Contents**

- [Prerequisites](#prerequisites)
- [Installing requisites](#installing-requisites)
- [Using the Quechua model without server](#using-the-model)
  - [Using the language model](#using-the-language-model)
  - [Using no the language model](#using-no-the-language-model)
- [Code documentation](#code-documentation)
- [Contact/Getting Help](#contactgetting-help)

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

### Using the language model

```bash
deepspeech --model output_graph.pbmm --alphabet quz_alphabet.txt --lm 5-gram.binary --trie quz_trie --audio hatispa.wav
```

### Using no the language model

```bash
deepspeech --model output_graph.pb --alphabet quz_alphabet.txt --audio hatispa.wav
```


### Recommendations

If you have a capable (Nvidia, at least 8GB of VRAM) GPU, it is highly recommended to install TensorFlow with GPU support. Training will likely be significantly quicker than using the CPU. To enable GPU support, you can do:

```bash
pip uninstall tensorflow
pip install 'tensorflow-gpu==1.5.0'
```



## Code documentation

Documentation (incomplete) for the code can be found here: http://deepspeech.readthedocs.io/en/latest/

## Contact/Getting Help

There are several ways to contact us or to get help:

1. [**FAQ**](https://github.com/mozilla/DeepSpeech/wiki#frequently-asked-questions) - We have a list of common questions, and their answers, in our [FAQ](https://github.com/mozilla/DeepSpeech/wiki#frequently-asked-questions). When just getting started, it's best to first check the [FAQ](https://github.com/mozilla/DeepSpeech/wiki#frequently-asked-questions) to see if your question is addressed.

2. [**Discourse Forums**](https://discourse.mozilla.org/c/deep-speech) - If your question is not addressed in the [FAQ](https://github.com/mozilla/DeepSpeech/wiki#frequently-asked-questions), the [Discourse Forums](https://discourse.mozilla.org/c/deep-speech) is the next place to look. They contain conversations on [General Topics](https://discourse.mozilla.org/t/general-topics/21075), [Using Deep Speech](https://discourse.mozilla.org/t/using-deep-speech/21076/4), and [Deep Speech Development](https://discourse.mozilla.org/t/deep-speech-development/21077).

3. [**IRC**](https://wiki.mozilla.org/IRC) - If your question is not addressed by either the [FAQ](https://github.com/mozilla/DeepSpeech/wiki#frequently-asked-questions) or [Discourse Forums](https://discourse.mozilla.org/c/deep-speech), you can contact us on the `#machinelearning` channel on [Mozilla IRC](https://wiki.mozilla.org/IRC); people there can try to answer/help

4. [**Issues**](https://github.com/mozilla/deepspeech/issues) - Finally, if all else fails, you can open an issue in our repo.
