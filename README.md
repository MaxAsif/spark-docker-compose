# Spark cluster setup with docker compose

## Start the cluster
```bash
docker-compose up
```

## Submit an application

### Submit by connecting to master container
```bash
docker exec spark-master /opt/spark/bin/spark-submit --master spark://spark-master:7077 --deploy-mode client /opt/spark/apps/wordCount.py
```

### Spin a seperate driver container to submit an application
```bash

docker run --rm --name driver  -v $(pwd)/data:/opt/spark/data:z -v $(pwd)/spark_apps:/opt/spark/apps:z --network=spark  --entrypoint /bin/bash  -p 4042:4040 apache/spark /opt/spark/bin/spark-submit  --master spark://spark-master:7077 /opt/spark/apps/wordCount.py --deploy-mode client
```


## Stop the cluster
```bash
docker compose down
```
