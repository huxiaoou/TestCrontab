#!/usr/bin/bash -l

cd /root/workspace/Projects/huxo/TestCrontab

current_time=$(date +"%Y%m%d %H:%M:%S")
echo "hello, world. it's $current_time" >> test.log
python main.py >> test.log
