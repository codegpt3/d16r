FROM dolphinscheduler.docker.scarf.sh/apache/dolphinscheduler-worker:3.1.8

# 更换 MySQL 链接包
COPY mysql-connector-*.jar /opt/dolphinscheduler/libs

# worker 需要安装 python3 环境，用来支持 各种 类似于 datax 等等的脚本执行
#RUN apt-get update && \
#   apt-get install -y --no-install-recommends python3 python3-pip && \
#   # ds 该版本默认使用 python2.7 映射一下
#   ln -s /usr/bin/python3 /usr/bin/python2.7 && \
#   rm -rf /var/lib/apt/lists/*

RUN yum update && \
    yum install -y python3 python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python2.7 && \
    rm -rf /var/cache/yum/* \

# 安装 Python 依赖的包
COPY requirements.txt /opt/dolphinscheduler
RUN  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  -r requirements.txt

# 安装 DATAX
RUN wget https://datax-opensource.oss-cn-hangzhou.aliyuncs.com/202308/datax.tar.gz \
   && mkdir -p /opt/soft \
   && tar -zxvf datax.tar.gz -C /opt/soft/ \
   && rm -rf datax.tar.gz
