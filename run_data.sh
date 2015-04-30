#!/usr/bin/env sh
echo "====================================="
echo "Iris Dataset:"
echo "====================================="
./LLS.py iris.csv
echo "\n"

echo "====================================="
echo "Wine Dataset:"
echo "====================================="
./LLS.py wine.csv --head
echo "\n"


echo "====================================="
echo "Parkisons Dataset:"
echo "====================================="
./LLS.py parkisons.csv
