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

## Interacting with Expenses Endpoint

```bash
curl http://localhost:5000/expenses/

curl -X POST -H "Content-Type: application/json" -d '{
    "amount": 10.0,
    "description": "soda"
}' http://localhost:5000/expenses/
```

## Interacting with Incomes Endpoint

```bash
curl http://localhost:5000/incomes/

curl -X POST -H "Content-Type: application/json" -d '{
    "amount": 10.0,
    "description": "soda"
}' http://localhost:5000/incomes/
```
