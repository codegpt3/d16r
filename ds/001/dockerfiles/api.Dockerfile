FROM dolphinscheduler.docker.scarf.sh/apache/dolphinscheduler-api:3.1.8
COPY mysql-connector-*.jar /opt/dolphinscheduler/libs
