#!/bin/bash
year=$(echo "$1" | cut -d "-" -f 1)
mkdir -p "$year"
if [ ! -f "The Economist $2.mobi" ];then

        sed  "s/edition_date = .*/edition_date = '$1'/" economist.recipe > "The Economist $2.recipe"

        ebook-convert "The Economist $2.recipe" .mobi --output-profile=kindle_pw3 --pubdate="$1" -vv --mobi-file-type=new --title="The Economist $2"

        rm "The Economist $2.recipe"
        cp "The Economist $2.mobi" "$year"
fi
