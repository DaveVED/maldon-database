<div align="center">

# Maldon Database

[![GO](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](http://www.go.dev)

<img alt="Maldon Service" height="280" src="/assets/temp.png" />

</div>

## Getting Started

### Usage

#### Ping a MongoDB Cluster

```bash
# Set your password in the environment variable.
export MONOGODB_MALDON_ADMIN_:PASSWORD="<your_password>"

# If you you want to get fancy you can set it in you .venv so you don't have to set it every time..
# echo "export MONOGODB_MALDON_ADMIN_PASSWORD='<your_password>'" >> $VENV/bin/activate 

# Admin is optional and will be set to 'admin' by default
./scripts/ping_mongodb.py --cluster cluster0 --user admin
    
```
