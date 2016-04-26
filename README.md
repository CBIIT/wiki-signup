# wiki-signup

To use this application you must install python, setuptools and pip

	Open a Terminal

	1.	Install python either through clean install or virtualenv. Please use python 2.7+:
		1.1	To install python via virtualenv do the following:
			1.1.1 Install setuptools
				1.1.1.1 For example curl -O https://pypi.python.org/packages/d3/16/21cf5dc6974280197e42d57bf7d372380562ec69aef9bb796b5e2dbbed6e/setuptools-20.10.1.tar.gz
				1.1.1.2 tar xvfz setuptools-20.10.1.tar.gz
				1.1.1.3 cd setuptools-20.10.1
				1.1.1.4 sudo python setup.py install

			1.1.2 Install pip
				1.1.2.1 sudo easy_install pip

			1.1.3 pip install virtualenv

			1.1.4 cd into home directory 
				1.1.4.1 cd ~/ 
				1.1.4.2 git clone https://github.com/CBIIT/wiki-signup

			1.1.5 cd wiki-signup

			1.1.6 virtualenv python

	1.2 While still in wiki-signup directory
		1.2.1 ./python/bin/python setup.py install
		1.2.1 ./python/bin/python runserver.py

	1.3 Open browser and go to localhost:5000
