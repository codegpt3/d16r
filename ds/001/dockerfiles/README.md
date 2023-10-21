
# 准备 alert-server 镜像

# 准备 api 镜像

# 准备 master 镜像

# 准备 worker 镜像
- python -m venv .venv
- source .venv/bin/active
- pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip 
- pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sqlalchemy
- pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pymysql
- pip freeze > requirements.txt