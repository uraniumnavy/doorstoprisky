#!/bin/bash

wget http://ftp.gnu.org/gnu/gcc/gcc-4.8.2/gcc-4.8.2.tar.bz2 &&
    mkdir --parents build/init/1 &&
    mock --init --resultdir build/init/1 &&
    mkdir --parents build/buildsrpm/1 &&
    mock --buildsrpm --spec doorstoprisky.spec --sources gcc-4.8.2.tar.bz2 --resultdir build/buildsrpm/1 &&
    mkdir --parents build/init/2 &&
    mock --init --resultdir build/init/2 &&
    true
