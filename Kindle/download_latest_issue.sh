#!/bin/bash

nearest_saturday(){
	# Get the current day of the week (1..7); 1 is Monday
	day=$(date +%u)
	
	# If today is Friday, print the date of the next Saturday
	if [ "$day" -eq 5 ]; then
	    date -d "next Saturday" '+%Y-%m-%d'
	# If today is not Friday and not Saturday, print the date of the previous Saturday
	elif [ "$day" -ne 6 ]; then
	    date -d "last Saturday" '+%Y-%m-%d'
	# If today is Saturday, print today's date
	else
	    date '+%Y-%m-%d'
	fi
}

issue_date=$(nearest_saturday)
cat Readme.md | grep "$issue_date" | bash
