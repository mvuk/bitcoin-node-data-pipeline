# Bitcoin Data Pipeline

## Introduction

This is a python flask application that queries the nodes for data, and downloads appropriately formatted CSVs. It can be used to produce financial statements auditing specific wallet addresses, and querying datasets from the Bitcoin L1 and L2. It makes use of the pandas library to set up the dataframes which get downloaded into CSV files. Users can browse a UI web interface. 

## Services

1. **bitcoind**: Bitcoin full node. (puned to ~25gb)
2. **c-lightning**: Lightning Network node.
3. **python-app**: Python application interacting with both nodes.

## Setup

### Build and Run

1. Build and start all services:
   ```bash
   docker-compose build
   docker-compose up

2. To stop the services
    ```bash
    docker-compose down 