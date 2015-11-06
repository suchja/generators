#!/bin/bash

# Clone all necessary gits
gits=( "ac-current-bricklet" "accelerometer-bricklet" "ambient-light-bricklet" "ambient-light-v2-bricklet" "analog-in-bricklet" "analog-in-v2-bricklet" "analog-out-bricklet" "analog-out-v2-bricklet" "barometer-bricklet" "blinkenlights" "breakout-brick" "breakout-bricklet" "color-bricklet" "co2-bricklet" "current12-bricklet" "current25-bricklet" "dc-brick" "debug-brick" "distance-ir-bricklet" "distance-us-bricklet" "doc" "dual-button-bricklet" "dual-button-bricklet" "dual-relay-bricklet" "dust-detector-bricklet" "gas-detector-bricklet" "generators" "gps-bricklet" "hall-effect-bricklet" "heart-rate-bricklet" "humidity-bricklet" "imu-brick" "imu-v2-brick" "industrial-analog-out-bricklet" "industrial-digital-in-4-bricklet" "industrial-digital-out-4-bricklet" "industrial-dual-0-20ma-bricklet" "industrial-dual-analog-in-bricklet" "industrial-quad-relay-bricklet" "io16-bricklet" "io4-bricklet" "joystick-bricklet" "laser-range-finder-bricklet" "lcd-16x2-bricklet" "lcd-20x4-bricklet" "led-strip-bricklet" "line-bricklet" "linear-poti-bricklet" "load-cell-bricklet" "master-brick" "moisture-bricklet" "motion-detector-bricklet" "multi-touch-bricklet" "nfc-rfid-bricklet" "oled-128x64-bricklet" "oled-64x48-bricklet" "ozone-bricklet" "piezo-buzzer-bricklet" "piezo-speaker-bricklet" "ptc-bricklet" "remote-switch-bricklet" "rotary-encoder-bricklet" "rotary-poti-bricklet" "rs232-bricklet" "segment-display-4x7-bricklet" "servo-brick" "solid-state-relay-bricklet" "sound-intensity-bricklet" "stepper-brick" "temperature-bricklet" "temperature-ir-bricklet" "thermocouple-bricklet" "tilt-bricklet" "uv-light-bricklet" "voltage-bricklet" "voltage-current-bricklet" )

mkdir -p $TF_HOME
cd $TF_HOME

for g in "${gits[@]}"
do
	git clone https://github.com/$GIT_USER/$g.git
done
