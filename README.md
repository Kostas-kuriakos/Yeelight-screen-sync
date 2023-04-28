# Yeelight Screen Color Sync

This Python script uses a Yeelight RGB bulb to display the average color of your screen in real time. The bulb's color and brightness will change based on the dominant color of your screen, creating a synchronized lighting effect. The script is useful for enhancing your viewing experience while watching movies, playing games, or even just browsing the web.

## Prerequisites

-   A Yeelight RGB bulb
-   Python 3.x installed on your computer
-   The Pillow, yeelight, and numpy libraries installed in Python. You can install them by running `pip install Pillow yeelight numpy` in your terminal or command prompt.

## Usage

1.  Connect your Yeelight bulb to your local network.
2.  Find the IP address of your Yeelight bulb. You can find it by using the Yeelight app or your router's admin page.
3.  Open `screen_color_sync.py` in your favorite text editor.
4.  Edit the `BULB_IP` variable to match the IP address of your Yeelight bulb.
5.  Run the script by typing `python screen_color_sync.py` in your terminal or command prompt.
6.  The Yeelight bulb will now display the average color of your screen in real time.

## Configuration

You can adjust the brightness, color temperature, and smoothness of the Yeelight bulb by changing the values in the `main()` function. You can also adjust the delay time between updates by changing the `DELAY` variable.

## Troubleshooting

-   If the script throws an error, make sure you have installed all the required libraries.
-   If the Yeelight bulb does not respond, check that it is connected to the same network as your computer and that it is powered on.
-   If the Yeelight bulb continues to throw errors, it may be due to too many requests. Wait for a few seconds before running the script again.

## License

This script is released under the BSD 3-Clause License.

Copyright (c) 2023, kostas kuriakos

Redistribution and use in source and binary forms, with or without
modification, are permitted.
