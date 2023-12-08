#!/bin/bash

# Install the required libraries
sudo apt-get install -qq libproj-dev proj-data proj-bin libgeos-dev

# Install Cython
pip install Cython

# Install Cartopy
pip install cartopy

# Install a specific version of pyproj
pip install pyproj==1.9.6

# Install Skyfield
pip install skyfield

