FROM apache/dolphinscheduler-worker:3.1.8
#FROM dolphinscheduler.docker.scarf.sh/apache/dolphinscheduler-api:3.1.8
#FROM dolphinscheduler.docker.scarf.sh/apache/dolphinscheduler-alert-server:3.1.8
#FROM dolphinscheduler.docker.scarf.sh/apache/dolphinscheduler-master:3.1.8
# 例如
# FROM dolphinscheduler.docker.scarf.sh/apache/dolphinscheduler-tools:<version>

# 注意，如果构建的是dolphinscheduler-tools镜像
# 需要将下面一行修改为COPY mysql-connector-java-8.0.16.jar /opt/dolphinscheduler/tools/libs
# 其他服务保持不变即可
#COPY mysql-connector-java-8.0.16.jar /opt/dolphinscheduler/tools/libs
COPY extend/mysql-connector-java-8.0.16.jar /opt/dolphinscheduler/libs

COPY extend/datax /opt/soft/datax

# worker 需要安装 python3 环境，用来支持 各种 类似于 datax 等等的脚本执行
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 && \
    # ds 该版本默认使用 python2.7 映射一下
    ln -s /usr/bin/python3 /usr/bin/python2.7 && \
    rm -rf /var/lib/apt/lists/*
