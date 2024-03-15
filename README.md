<div align="center">

# Maldon Database

[![GO](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](http://www.go.dev)

<img alt="Maldon Service" height="280" src="/assets/temp.png" />

</div>

## ⇁ TOC
* [Getting Started](#-Getting-Started)
* [Contribution](#-Contribution)

## ⇁ Getting Started

### Prerequisites

Before getting started, you'll need to have the following tools installed:
- MongoDV Atlas Account or a MongoDB Cluster running.
- Python 3.8 or later (`python3 -m venv .venv && pip3 install -r requirements.txt`)

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


