#!/bin/bash -x
if pgrep -f hstMain.py > /dev/null; then
	echo "hst is running"
	exit 1
else
	echo "hst not running" 
	cd /var/www/html/huicloud/hst/
	python3 hstMain.py > /dev/null &
	cd /
fi

