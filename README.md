# crontab 配置指南

## 上传

```powershell
scp -r /path/to/Project/TestCrontab YOUR_HOST:/root/workspace/因子研究/
```

## 安装

```bash
cd /root/workspace/因子研究/TestCrontab
```

```bash
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

## 定时任务案例

```bash
crontab -e
```

在文件末尾加入用户需要的定时任务. 以下为两个案例,

### 案例1:每分钟执行一次本项目下的脚本`main.sh`
```vim
* * * * *  /root/workspace/因子研究/TestCrontab/main.sh
```

建议以此案例来测试`crontab`. 测试时使用

```bash
chmod +x main.sh
```

来赋予脚本执行权限. 然后使用

```bash
tail -f test.log
```

来查看任务执行情况.

### 案例2:每周1-5的18:30,执行自定义脚本task02.sh
```vim
30 18 * * 1-5 /path/to/task02.sh
```

## 查看crontab

```bash
crontab -l
```
