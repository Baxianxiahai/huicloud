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

if pgrep -f fawsMain.py > /dev/null  ; then
	echo "faws is running"
	exit 1
else
	echo "faws not running"
	cd /var/www/html/faws/
	${pyExec} fawsMain.py &
	cd /
fi

