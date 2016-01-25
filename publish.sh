ps -ef|grep  'python app.py'|awk '{print $2}' |xargs  kill -9 & git pull origin master && nohup python app.py &
