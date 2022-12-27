# Mouse Jiggler

## Description

A mouse jiggler is a small program or script that simulates movement of the mouse pointer on a computer screen. This can be useful in a variety of situations, such as keeping a computer from going to sleep or preventing screensavers from activating.

## Features

- Simulates mouse movement at regular intervals
- Allows for customization of movement frequency and intensity
- Can be started and stopped on demand

## Requirements

- Python 3.x
- pyautogui library (can be installed using `pip install pyautogui`)

## Usage

1. Run the script using `python mouse_jiggler.py`
2. The jiggler will start automatically, moving the mouse slightly at the default interval of every 10 seconds.
3. To adjust the interval, use the `--interval` flag followed by the desired interval in seconds (e.g. `python mouse_jiggler.py --interval 30` for a 30 second interval)
4. To adjust the intensity of the mouse movement, use the `--distance` flag followed by the desired distance in pixels (e.g. `python mouse_jiggler.py --distance 5` for a distance of 5 pixels)
5. To stop the jiggler, use the `--stop` flag (e.g. `python mouse_jiggler.py --stop`)

## Example

To start the jiggler with a 20 second interval and a movement distance of 10 pixels:


## Notes

- The jiggler will run in the background and can be stopped at any time using the `--stop` flag.
- If the jiggler is not responding as expected, try increasing the interval or distance to ensure that the mouse movement is noticeable.
