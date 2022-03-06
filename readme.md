# LaunchToRythm

A small python script that turns your Novation Launchpad into a 4K rythm game controller!

# Installation

```
git clone https://github.com/alexfeed1990/LaunchToRhythm.git
cd LaunchToRhythm
pip -r requirements.txt
python LaunchToRhythm.py
```

# Config

The configuration is pretty simple and self explanatory:

Name            | Description
----------------| -------------
effect1enabled  | If the first effect is enabled or not.
effect2enabled  | If the second effect is enabled or not.
effect1speed    | The speed of the first effect.
effect2speed    | The speed of the second effect.
effect1color    | The color of the first effect.
effect2colors   | Array of the colors used in the second effect
effect2colors 1 | First color used in the second effect (Background color).
effect2colors 2 | Second color used in the second effect (Foreground color).
keys            | Array of the 4 keys pressed.
keys 1          | First key.
keys 2          | Second key.
keys 3          | Third key.
keys 4          | Fourth key.
buttons         | Array of the 4 buttons x and y position on the Launchpad.
buttons 1       | The x and y of the first button.
buttons 2       | The x and y of the second button.
buttons 3       | The x and y of the third button.
buttons 4       | The x and y of the fourth button.
pressColor      | The color when you press one of the 4 keys on the Launchpad.

To modify any color values, check [this](http://www.launchpadfun.com/downloads/Velocity-Colors_MASTER_PICTURE_hires.png) map of the Launchpad color scheme.

To modify any position values, check out [this](https://github.com/FMMT666/launchpad.py/blob/master/examples/buttons_xy.py) script.
