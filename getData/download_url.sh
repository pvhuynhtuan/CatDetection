#!/bin/bash
in_file=$1

while IFS= read -r line
do
	echo "$line"
	wget $line
done < $in_file
