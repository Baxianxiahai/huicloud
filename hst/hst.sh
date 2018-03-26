#!/bin/sh
### BEGIN INIT INFO
# Provides:          hst
# Required-Start:    $local_fs $remote_fs $network $syslog $named
# Required-Stop:     $local_fs $remote_fs $network $syslog $named
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# X-Interactive:     true
# Short-Description: Start/stop hst
# 本文件hcu执行程序放置位置: /var/www/html/huicloud/hst.sh
### END INIT INFO

set -x

#
# Function that starts the daemon/service
#
do_start()
{
	#判定hcu是否运行
	if pgrep "python3 /var/www/html/huicloud/hst/hstMain.py" > /dev/null  ; then
		echo "hst is running"
		exit 1
	else
		echo "hst not running" 
		sudo cd /
		sudo -S python3 /var/www/html/huicloud/hst/hstMain.py &
		sleep 1
		
}

#
# Function that starts the daemon/service
#
HST_PID = ""

do_stop()
{
	if pgrep "python3 /var/www/html/huicloud/hst/hstMain.py" > /dev/null  ; then
		echo "hst is running ..."
		HST_PID = $(pidof "python3 /var/www/html/huicloud/hst/hstMain.py")
		kill -9 $(pidof "python3 /var/www/html/huicloud/hst/hstMain.py") 
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
