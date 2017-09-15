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

```bash
curl http://localhost:5000/users/

curl -X POST -H "Content-Type: application/json" -d '{
    "title": "JavaScript",
    "description": "JS developers."
}' http://localhost:5000/users/
```
