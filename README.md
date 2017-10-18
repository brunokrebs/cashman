## Running Cashman

```bash
docker run --name cashman-psql \
    -e POSTGRES_PASSWORD=dbpassword \
    -e POSTGRES_USER=dbuser \
    -e POSTGRES_DB=cashman \
    -p 5432:5432 \
    -d postgres
```

## Interacting with Expenses Endpoint

```bash
curl http://localhost:5000/expenses

curl -X POST -H "Content-Type: application/json" -d '{
    "amount": 10.0,
    "description": "soda"
}' http://localhost:5000/expenses
```

## Interacting with Incomes Endpoint

```bash
curl http://localhost:5000/incomes

curl -X POST -H "Content-Type: application/json" -d '{
    "amount": 300.0,
    "description": "loan payment"
}' http://localhost:5000/incomes

curl -X POST -H "Content-Type: application/json" -d '{
    "amount": 300.0,
    "description": "loan payment",
    "tags": [
        "loan",
        "profit"
    ]
}' http://localhost:5000/incomes

curl -X POST -H "Content-Type: application/json" -d '{
    "amount": 510.0,
    "description": "lottery ticket",
    "tags": [
        "luck",
        "profit"
    ]
}' http://localhost:5000/incomes
```

## Cashman and Docker Container

```bash
# build image
docker build -t cashman .

# run cashman on docker
docker run --name cashman \
    -d -p 5000:5000 \
    cashman

# connect to cashman container
docker exec -it cashman bash

# stop and remove cashman
docker stop cashman
docker rm cashman
```
