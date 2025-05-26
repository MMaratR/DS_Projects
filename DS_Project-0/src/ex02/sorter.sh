#!/bin/sh

OUTPUT_FILE="hh_sorted.csv"
INPUT_FILE="../ex01/hh.csv"

head -n 1 $INPUT_FILE > $OUTPUT_FILE
tail -n +2 $INPUT_FILE | sort -t, -k2 -k1 >> $OUTPUT_FILE
