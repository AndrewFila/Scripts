#!/bin/sh

URL='https://www.accuweather.com/en/us/houghton/49931/weather-forecast/333677'
TEXT=wget -q -O- "$URL" | awk -F\' '/acm_RecentLocationsCarousel\.push/{print $2": "$16", "$12"°" }'| head -1
echo ${TEXT}
