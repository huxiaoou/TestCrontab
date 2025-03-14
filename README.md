# crontab 配置指南

## 上传项目到服务器

```powershell
scp -r /path/to/Project/TestCrontab YOUR_HOST:/root/workspace/Projects/huxo
```

## 安装

首先进入项目目录

```bash
cd /root/workspace/Projects/huxo/TestCrontab/
```

然后使用以下命令安装

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

使用以下命令进入`crontab` 编辑模式.

```bash
crontab -e
```

编辑器默认是Vim，需要熟悉常见操作

| 按键     | 操作     |
|--------|--------|
| insert | 进入编辑模式 |
| esc    | 退出编辑模式 |
| :wq    | 保存并退出  |

在文件末尾加入用户需要的定时任务. 以下为两个案例,

### 案例1:每分钟执行一次本项目下的脚本`main.sh`

```vim
* * * * *  /root/workspace/Projects/huxo/TestCrontab/main.sh
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
