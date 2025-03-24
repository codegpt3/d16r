## version
- 3.2.2
  
001 api + alert-server + zk + worker + master

## 端口
worker

1234
1235

master

5678
5679

alert

50052
50053

api

12345
25333
25334

## 搭建流程
docker tag apache/dolphinscheduler-tools:3.2.2 ocr.private.io:7233/apache/dolphinscheduler-tools:3.2.2
docker tag apache/dolphinscheduler-master:3.2.2 ocr.private.io:7233/apache/dolphinscheduler-master:3.2.2
docker tag apache/dolphinscheduler-worker:3.2.2 ocr.private.io:7233/apache/dolphinscheduler-worker:3.2.2
docker tag apache/dolphinscheduler-api:3.2.2 ocr.private.io:7233/apache/dolphinscheduler-api:3.2.2
docker tag apache/dolphinscheduler-alert-server:3.2.2 ocr.private.io:7233/apache/dolphinscheduler-alert-server:3.2.2
docker tag bitnami/zookeeper:3.7.1 ocr.private.io:7233/bitnami/zookeeper:3.7.1
docker tag bitnami/postgresql:15.2.0 ocr.private.io:7233/bitnami/postgresql:15.2.0
docker push ocr.private.io:7233/apache/dolphinscheduler-tools:3.2.2
docker push ocr.private.io:7233/apache/dolphinscheduler-master:3.2.2
docker push ocr.private.io:7233/apache/dolphinscheduler-worker:3.2.2
docker push ocr.private.io:7233/apache/dolphinscheduler-api:3.2.2
docker push ocr.private.io:7233/apache/dolphinscheduler-alert-server:3.2.2
docker push ocr.private.io:7233/bitnami/zookeeper:3.7.1
docker push ocr.private.io:7233/bitnami/postgresql:15.2.0


## 启动链接
http://localhost:12345/dolphinscheduler/ui/monitor/worker
