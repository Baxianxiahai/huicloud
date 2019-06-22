#!/bin/bash -x

if [ -e /opt/pycv/bin/python3 ]
then
	export PATH=/opt/pycv/bin:$PATH
	export LD_LIBRARY_PATH=/opt/pycv/lib:$LD_LIBRARY_PATH
	export PYTHON_INCLUDE_DIRS=/opt/pycv/include/python3.6dm
	export PYTHON_LIBRARIES=/opt/pycv/lib/libpython3.6dm.a
	pyExec=/opt/pycv/bin/python3
elif [ -e /usr/local/bin/python3 ]
then
	export PATH=/usr/local/bin:$PATH
        export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
        export PYTHON_INCLUDE_DIRS=/usr/local/include/python3.6m
        export PYTHON_LIBRARIES=/usr/local/lib/libpython3.6m.a
	pyExec=/usr/local/bin/python3
else
	pyExec=/usr/bin/python3
fi

export PYTHONPATH=$PYTHONPATH:/var/www/html/huicloud/DjoSiteDba/
cmdExec="${pyExec} /var/www/html/huicloud/hst/hstMain.py"

if pgrep -f hstMain.py > /dev/null  ; then
	echo $(date +%Y-%m-%d_%H:%M:%S) "hst is running"
	exit 1
else
	echo $(date +%Y-%m-%d_%H:%M:%S) "hst not running, restarting now"
	cd /var/www/html/huicloud/hst/
	${pyExec} hstMain.py &
	cd /
fi

#Direct method, not used anymore, but keep for later on test purpose!
	#if pgrep -f hstMain.py > /dev/null; then
	#	echo $(date +%Y-%m-%d_%H:%M:%S) "hst is running"
	#	exit 1
	#else
	#	echo $(date +%Y-%m-%d_%H:%M:%S) "hst not running, restarting now"
	#	cd /var/www/html/huicloud/hst/
	#	python3 hstMain.py > /dev/null &
	#	cd /
	#fi

