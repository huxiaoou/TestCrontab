# crontab 配置指南

## 上传

```powershell
scp cron_3.0pl1-136ubuntu1_amd64.deb YOUR_HOST:/root/workspace/因子研究/TestCrontab
```

## 安装

```bash
cd /root/workspace/因子研究/TestCrontab
dpkg -i cron_3.0pl1-136ubuntu1_amd64.deb
```

## 查看服务

```bash
service cron status
```

## 启用服务

```bash
service cron start
```

## 设置开机运行

```bash
systemctl enable cron
```

## 定时任务案例

```bash
crontab -e
```

在文件末尾加入用户需要的定时任务. 以下为两个案例,

### 案例1:每分钟执行一次本项目下的脚本`main.sh`
```vim
* * * * *  /root/workspace/因子研究/TestCrontab/main.sh
```

### 案例2:每周1-5的18:30,执行自定义脚本task02.sh
```vim
30 18 * * 1-5 /path/to/task02.sh
```

## 查看crontab

```bash
crontab -l
```
