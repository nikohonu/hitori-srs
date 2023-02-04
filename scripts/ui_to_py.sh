#!/bin/bash
files=`ls hitori_srs/views/ui/*.ui`
for file in $files
do
   pdm run pyside6-uic "${file%%.*}".ui -g python -o "${file%%.*}".py
done
