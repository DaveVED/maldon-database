<div align="center">

# Maldon Database

[![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](https://https://www.python.org)
[![GO](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](http://www.go.dev)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://https://www.docker.com/)

<img alt="Maldon Service" height="280" src="/assets/temp.png" />

</div>

## ⇁ TOC
* [Getting Started](#-Getting-Started)
* [Deployments](#-Deployments)
* [Packages](#-Packages)
    * [Users](#-Users)

## ⇁ Getting Started

## Deployments

### Local
```bash
docker-compose up -d

# If you're facing issues you can hard start. 
docker-compose up -d --force-recreate --pull always
```

## Packages

We provide a few opitons for you to interact with the with the MongoDB database, if you'd like, of courese,
you can always write your own client.

### Users

The Users package provides a way to interact with the users collection in the database. Here is the 
interface for the Users package:

```go
type UserInterface interface {
    CreateUser(ctx context.Context, user DiscordUser) (*mongo.InsertOneResult, error)
    GetUser(ctx context.Context, discordUsername, discordDiscrim string) (DiscordUser, error) // Corrected method name
    SearchUsers(ctx context.Context) ([]DiscordUser, error)
}
```
