#!/bin/sh

OUTPUT_FILE="./hh.json"
VACANCY_NAME=$(echo "$1" | jq -R @uri)

curl -G "https://api.hh.ru/vacancies?text=$VACANCY_NAME&page=0&per_page=20" | jq > $OUTPUT_FILE