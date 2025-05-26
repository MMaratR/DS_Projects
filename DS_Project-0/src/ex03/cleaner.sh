#!/bin/sh

OUTPUT_FILE="hh_positions.csv"
INPUT_FILE="../ex02/hh_sorted.csv"

head -n 1 "$INPUT_FILE" > "$OUTPUT_FILE"
tail -n +2 "$INPUT_FILE" | awk -F"," '{
    result = "";
    if (tolower($3) ~ /junior/) {
        result = "Junior";
    } else if (tolower($3) ~ /middle/) {
        result = "Middle";
    } else if (tolower($3) ~ /senior/) {
        result = "Senior";
    }

    # Если ничего не найдено, ставим "-"
    if (result == "") {
        $3 = "\"-\"";
    } else {
        $3 = "\""result"\"";
    }

    print;
}' OFS="," >> "$OUTPUT_FILE"
