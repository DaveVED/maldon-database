#!/usr/bin/env python3

import os
import argparse

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def ping_mongodb(user: str, password: str, cluster: str) -> None:
    url: str = f"mongodb+srv://{user}:{password}@{cluster}.waalpww.mongodb.net/?retryWrites=true&w=majority&appName={cluster}"

    client = MongoClient(url, server_api=ServerApi("1"))

    try:
        client.admin.command("ping")
        print(f"Ping connection to {cluster} successful")
    except Exception as e:
        print(f"Ping connection Failed: {e}")

def run():
    parser = argparse.ArgumentParser(description="Ping Maldonado's MongoDB Connection")
    
    parser.add_argument("--user", default="admin", help="MongoDb username")
    parser.add_argument("--cluster", required=True, help="MongoDb cluster")
    
    args = parser.parse_args()
    
    password = os.getenv("MONOGODB_MALDON_ADMIN_PASSWORD", None)
    assert password is not None, "The $MONGODB_MALDON_ADMIN_PASSWORD environment variable is not set"
    
    ping_mongodb(args.user, password, args.cluster)

if __name__ == "__main__":
    run()
