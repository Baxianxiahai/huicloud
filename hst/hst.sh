#!/bin/sh
### BEGIN INIT INFO
# Provides:          hst
# Required-Start:    $local_fs $remote_fs $network $syslog $named
# Required-Stop:     $local_fs $remote_fs $network $syslog $named
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# X-Interactive:     true
# Short-Description: Start/stop hst
# 本文件hst执行程序放置位置: /var/www/html/huicloud/hst/hst.sh
# 
# python3.6执行必须采用结对路径
# 
#
### END INIT INFO

set -x

#
# Function that starts the daemon/service
#

#
#Define command
#在不同的服务器中，python3.6的安装地址可能不一样，将会导致这个绝对路径不一样，从而导致本脚本不一样，需要小心注意！
#
cmdExec = "/opt/pycv/bin/python3.6 /var/www/html/huicloud/hst/hstMain.py"

do_start()
{
	#判定hst是否运行
	if pgrep $cmdExec > /dev/null  ; then
		echo "hst is running"
		exit 1
	else
		echo "hst not running" 
		sudo cd /
		sudo -S /opt/pycv/bin/python3.6 /var/www/html/huicloud/hst/hstMain.py &
		sleep 1
	fi
}

#
# Function that starts the daemon/service
#
HST_PID = ""

do_stop()
{
	if pgrep $cmdExec > /dev/null  ; then
		echo "hst is running ..."
		HST_PID = $(pidof $cmdExec)
		kill -9 $(pidof $cmdExec) 
		echo "hst killed ..."
		exit 1
	else
		echo "hst not running, do nothing" 

	fi
}

case "$1" in
  start)
	do_start
	;;
  stop)
	do_stop
	;;
  restart)
	do_stop	
	do_start
	;;
  *)
	echo "Usage: hst {start|stop|restart|}" >&2
	exit 3
	;;
esac
