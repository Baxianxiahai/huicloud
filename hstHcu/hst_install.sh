#!/bin/bash

# Ubutu操作方法
# Step1: create /var/www/html
# Step2: copy huicloud.zip to /var/www/html/
# Step3: cp this file (hst_install.sh) to /var/www/html/
# Step4: exectue, sudo ./hst_install.sh
# Step5: 添加： sudo update-rc.d 服务名 defaults
#        删除：sudo update-rc.d -f 服务名 remove

# Centos操作方式
# Step1 - Step4: same as above
# Step5: copy hst.service to /usr/lib/systemd/system/
# Step6: chmod -R 754 /usr/lib/systemd/system/hst.service
# Step7: systemctl enable hst

# 最后使用systemctl status hst, start hst, stop hst，来分别看状态、停止和启动hst服务


# copy files
cp ./huicloud.zip /tmp/
cd /var/www/html
unzip /tmp/huicloud.zip
rm -v /tmp/huicloud.zip

#cp to target dir
cd ./huicloud/hst/
cp ./hst.sh /etc/init.d/hst.sh
chmod +x /etc/init.d/hst.sh

## add to each runlevel
for rl in 2 3 4 5
do
cd /etc/rc${rl}.d/
ln -sf ../init.d/hst.sh S02hst.sh
done

for rl in 0 1 6
do
cd /etc/rc${rl}.d/
ln -sf ../init.d/hcu.sh K01hst.sh
done


