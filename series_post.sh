#!/bin/bash

if [ $# -lt 2 ]
then
	echo "[USAGE] $0 [url] [csv file]"
	exit 1
fi
URL=$1
CSV_NAME=$2

C_TYPE='Content-Type: application/json'

cat $CSV_NAME | tail -n +2 | while read line
do
#	echo $line
	user_id=`echo $line | cut -d ',' -f 1`
	rain_pct=`echo $line | cut -d ',' -f 6`
	w_temp=`echo $line | cut -d ',' -f 7`
	pred=`echo $line | cut -d ',' -f 10`
	json_str="{\"user_id\":${user_id},\"rain_pct\":${rain_pct},\"w_temp\":${w_temp},\"m_predict\":${pred}}"
#	echo $C_TYPE $json_str $URL
	curl -X POST -H "${C_TYPE}" -d "$json_str" "$URL"
done
