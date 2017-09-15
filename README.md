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
