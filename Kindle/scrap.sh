#!/bin/bash

sed -i "s/edition_date = None/edition_date = '$1'/" economist.recipe

ebook-convert economist.recipe .mobi --output-profile=kindle_pw3 --pubdate="$1" -vv --mobi-file-type=new --title="The Economist $2" --mobi-keep-original-images

sed -i "s/edition_date = '$1'/edition_date = None/" economist.recipe
mv economist.mobi "The Economist $2.mobi"
