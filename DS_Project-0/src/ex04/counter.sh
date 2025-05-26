#!/bin/sh

OUTPUT_FILE="hh_uniq_positions.csv"
INPUT_FILE="../ex03/hh_positions.csv"

echo '"name","count"' > $OUTPUT_FILE
tail -n +2 $INPUT_FILE | awk -F"," '{print $3}' | sort | uniq -c | awk '{print $2 "," $1}' >> $OUTPUT_FILE