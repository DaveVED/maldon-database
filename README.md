<div align="center">

# Maldon Database

[![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](https://https://www.python.org)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](http://www.go.dev)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://https://www.docker.com/)

<img alt="Maldon Service" height="280" src="/assets/temp.png" />

Welcome, here you will find a collection of scripts and tools to help manage and
maintain a MongoDB cluster for the Maldon application. It was originally 
designed to be used with a MongoDB Atlas cluster, but can be used with any
MongoDB cluster. I try provide a set of generic tools to help _you_ run and mange
Maldon. It is not meant to be a one-size-fits-all solution, that can
run out of the box, but also allows for customization and modification to fit
for your specific use case.

</div>

## ⇁ TOC
* [Getting Started](#-Getting-Started)
* [Contribution](#-Contribution)

## ⇁ Getting Started

### Prerequisites

Before getting started, you'll need to have the following tools installed:
- MongoDb Atlas Account or a MongoDB Cluster running.
- Python 3.8 or later insatlled
- Requuiremnts installed _(`pip3 install -r requirements.txt`)_

### Scripts Usage

#### Ping a MongoDB Cluster

```bash
# Set your password in the environment variable.
export MONOGODB_MALDON_ADMIN_PASSWORD="<your_password>"

# If you you want to get fancy you can set it in you .venv so you don't have to set it every time..
# echo "export MONOGODB_MALDON_ADMIN_PASSWORD='<your_password>'" >> $VENV/bin/activate 

# Admin is optional and will be set to 'admin' by default
chmod +x scripts/ping_mongodb.py
./scripts/ping_mongodb.py --cluster cluster0 --user admin
```

## ⇁ Contribution

This project is officially open source, not just public source.  If you wish to
contribute start with an issue and I am totally willing for PRs, but I will be
very conservative on what I take.  I don't want Maldon Database scripts _solving_ specific
issues. I want them to be generic and useful for everyone.  If you have a specific
use cases you can take a fork and make it your own.


