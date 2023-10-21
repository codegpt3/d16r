# dolphinscheduler
- doc: https://dolphinscheduler.apache.org/zh-cn/docs/3.1.8/guide/start/quick-start
## version
- 3.1.8
## dolphinscheduler
- local
- dev
- main
  
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
- build各个镜像
如docker build -t dolphinscheduler-worker:latest .
  <img width="747" alt="image" src="https://github.com/cxjwbj/dolphinscheduler/assets/50309507/e89c6a69-81d0-4096-ab5a-0aed97be1666">
- docker-compose -f docker-compose-001.yml up -d  
- docker-compose -f docker-compose-001.yml down 


## 启动链接
http://localhost:12345/dolphinscheduler/ui/monitor/worker
