#!/bin/bash
echo "Compile edilir."
sleep 1
clear
echo "Compile edilir.."
sleep 1
clear
echo "Compile edilir..."
sleep 1
clear
cmake .
make -j $(nproc)
echo "Lazimsiz fayllar silinir..."
sleep 1
rm CMakeFiles CMakeCache.txt Makefile cmake_install.cmake -rf



