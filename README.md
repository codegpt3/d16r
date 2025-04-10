# Dolpinscheduler

## SEATUNNEL_VERSION

- 3.2.2
  
001 api + alert-server + zk + worker + master
002 api + zk + worker + master
003 api + zk + worker + master

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

```bash
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
```

## seatunnel

```bash
curl -LO https://mirrors.tuna.tsinghua.edu.cn/apache/seatunnel/2.3.9/apache-seatunnel-2.3.9-bin.tar.gz
docker cp apache-seatunnel-2.3.9-bin.tar.gz 001_dolphinscheduler-worker_1:/opt/soft/ && docker exec -it 001_dolphinscheduler-worker_1 bash -c "mkdir -p /opt/soft/seatunnel && tar -zxvf /opt/soft/apache-seatunnel-2.3.9-bin.tar.gz --strip-components 1 -C /opt/soft/seatunnel"
docker cp apache-seatunnel-2.3.9-bin.tar.gz 002_dolphinscheduler-worker_1:/opt/soft/ && docker exec -it 002_dolphinscheduler-worker_1 bash -c "mkdir -p /opt/soft/seatunnel && tar -zxvf /opt/soft/apache-seatunnel-2.3.9-bin.tar.gz --strip-components  1 -C /opt/soft/seatunnel"
docker cp apache-seatunnel-2.3.9-bin.tar.gz 003_dolphinscheduler-worker_1:/opt/soft/ && docker exec -it 003_dolphinscheduler-worker_1 bash -c "mkdir -p /opt/soft/seatunnel && tar -zxvf /opt/soft/apache-seatunnel-2.3.9-bin.tar.gz --strip-components 1 -C /opt/soft/seatunnel"
cat plugin-mapping.properties |awk -F '=' '{print $2}'|uniq|grep -v '^$'|xargs -i curl -LO https://maven.aliyun.com/repository/central/org/apache/seatunnel/{}/2.3.9/{}-2.3.9.jar

# https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.0.33/mysql-connector-j-8.0.33.jar
curl -LO https://maven.aliyun.com/repository/central/com/mysql/mysql-connector-j/8.0.33/mysql-connector-j-8.0.33.jar
环境变量-新建
export SEATUNNEL_HOME=/opt/soft/seatunnel
export JAVA_HOME=/opt/java/openjdk
export PATH=$JAVA_HOME/bin:$PATH
```

## 启动链接

<http://localhost:12345/dolphinscheduler/ui/>
admin dolphinscheduler123
