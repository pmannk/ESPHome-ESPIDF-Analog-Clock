# ESPHome-Analog-Clock
This is an ESPHome component forked from the excellent source found here: https://github.com/markusressel/ESPHome-Analog-Clock

⚠️ This is a work in progress - the idf_clock.h files and esphome_rmt_led_clock_effect.yaml light changes are complete, so you can use them as a custom_component, but this repository is not yet ready for use as an external_component

# Significant changes
* [ ] TODO: Update to work with external_components (custom_components are deprecated and will be removed in 2026.6.0)
* [x] Updated to work with ESP-IDF (from 2026.1.0 the ESPHome default for ESP32 / ESPC3|S2|S3)
* [x] Works with esp32_rmt_led_strip


<B>Original image and video:</b> <br>
 [![Demo VIdeo](https://img.youtube.com/vi/RIAHLAqe6oY/0.jpg)](https://www.youtube.com/watch?v=RIAHLAqe6oY)

# Features

* [x] "Loading" animation while initializing
* [x] Works with (almost) any LED strip length
* [x] Fading animations for all hands when switching
* [x] Slowly fading tail behind the second hand
* [x] Overlapping (additive) hand colors
* [x] Settings
    * [x] Disable second hand
    * [x] Show hour indicators

## How to use

* Create a new ESPHome configuration YAML file
* Establish a basic device configuration (Board, WiFi, etc.) to your liking
* Add the contents of [esphome_rmt_led_clock_effect.yaml](./esphome_rmt_led_clock_effect.yaml) to the file
* Customize the fields in the `substitutions` part at the top
* Deploy and enjoy!

## Watchface

The provided [Watchface.svg](Watchface.svg) perfectly fits on the 60 LED NeoPixel ring.
You can print this, cut it out and simply glue/tape it to the ring to create the look visible in the video above. 

# Contributing

GitHub is for social coding: if you want to write code, I encourage contributions through pull requests from forks
of this repository. Create GitHub tickets for bugs and new features and comment on the ones that you are interested in.

# License

CC0 see [LICENSE](./LICENSE)
