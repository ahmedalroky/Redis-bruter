#!/bin/bash
apt update
apt install wget zip gcc g++ make python python-dev libasound2-dev -y
wget https://github.com/pjsip/pjproject/archive/2.11.1.zip
unzip 2.11.1.zip
cd pjproject-2.11.1/
./configure --enable-shared --disable-static --enable-memalign-hack
make dep
make
make install
cd pjsip-apps/src/python
python setup.py build
python setup.py install
