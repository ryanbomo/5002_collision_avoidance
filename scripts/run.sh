#!/bin/bash
cd ../
cd ./src/
SCRIPT=$(readlink -f "$0")
./main -m$1 -i$2 -d$3
