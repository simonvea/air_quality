#!/bin/bash

FILE=collect_air_quality.py

PID=$(ps ax | grep $FILE | sed 1q | grep -Eo '^[0-9]{,5}')

kill $PID
