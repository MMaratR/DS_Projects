#!/bin/sh

OUTPUT_FILE="hh_positions.csv"

echo '"id","created_at","name","has_test","alternate_url"' > $OUTPUT_FILE


cat *.csv | sed '/^"id","created_at","name","has_test","alternate_url"/d' >> $OUTPUT_FILE
