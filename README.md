# PyTimer - A Simple PyGame Timer Library
> A lightweight Python timer and tweening library insired by Love2D's [Hump](https://github.com/vrld/hump) library with built-in support for multiple easing functions from [pytweening](https://github.com/asweigart/pytweening), designed for easy time-based animations and delayed callbacks.

-----

<br/>

# Contents
- [Instalation](#instalation)
- [Quick start](#quickstart)
    - [Updating the timer](#updatethetimer)
    - [Creating a pulsing rectangle](#createapulsingrectangle)
- [Documentation](#documentation)
    - [After](#afterdelay-callback)
    - [Tween](#tweenduration-start_value-end_value-on_update-easing-callback)
    - [Easing types](#geteasingtypes)


-----

<br/>

# Instalation
```bash
git clone https://github.com/clxakz/pytimer
```
or
```bash
pip install pytimerlib
```

<br/>

> [!NOTE]
> Using pip, the PyTimer library is renamed to pytimerlib, since pytimer is allready taken.

-----

<br/>

# Quick start
place the `pytimer` folder inside your project and import it
```python
from pytimerlib import Timer
```

# Update the Timer
In your main loop update the `Timer` with delta time
```python
while running:
    dt = clock.tick(60) / 1000
    Timer.update(dt)
```

# Create a pulsing rectangle
As an example we can use tweens to pulse a rectangle on the screen <br/>
See [pulse.py](https://github.com/clxakz/pytimer/blob/main/examples/pulse.py) for full example
```python
surface = pygame.Surface((250, 250))
surface.fill((255,255,255))
alpha = 0

def set_alpha(value):
    global alpha
    alpha = value


def pulse():
    Timer.tween(1, 0, 255, set_alpha, "linear", lambda:         # Tween from 0 to 255
        Timer.after(1, lambda:                                  # Wait 1 second
            Timer.tween(1, 255, 0, set_alpha, "linear", pulse)  # Tween from 255 to 0 and repeat pulse
        )
    )

pulse()

# In your mainloop
surface.set_alpha(alpha)
screen.blit(surface, (125, 125))
```

And that looks like <br/>
<img src="assets/demo.gif" alt="Alt text" width="500" />


-----

<br/>


# Documentation
### `.after(delay, callback)`
The `after()` function will run a callback function after a set time
```python
Timer.after(1, lambda: print("Done!")) # <- Prints 'Done!' after 1 second
```

Arguments
- `delay` `(int)` - Time in seconds
- `callback` `(callable)` - An optional callback function, none by default

-----

<br/>

### `.tween(duration, start_value, end_value, on_update, easing, callback)`
The `tween()` function animates a value smoothly from `start_value` to `end_value` over `duration` seconds, calling `on_update(value)` each frame with the eased value. Supports custom easing types and an optional `callback` when complete
```python
alpha = 0

def set_value(value):
    global alpha
    alpha = value

Timer.tween(1, 0, 255, set_value, "easeOutQuad", lambda: print("Done!")) # <- Smoothly animates alpha from 0 to 255 using the easeOutQuad easing type. Prints 'Done!' when finished.
```

Arguments
- `duration` `int` - Duration in seconds
- `start_value` `int` - The start value
- `end_value` `int` - The end value
- `on_update` `callable` - Returns the updated value as float
- `easing` `str` - Sets the easing type
- `callback` `callable` - An optional callback function, none by default

-----

<br/>

### `.get_easing_types()`
The `get_easing_types()` function will print a full list of all available easing types
```python
Timer.get_easing_types()
```

You can use any of the following easing types in `.tween()`, thanks to [pytweening](https://github.com/asweigart/pytweening) for providing these:
- linear
- easeInQuad
- easeOutQuad
- easeInOutQuad
- easeInCubic
- easeOutCubic
- easeInOutCubic
- easeInQuart
- easeOutQuart
- easeInOutQuart
- easeInQuint
- easeOutQuint
- easeInOutQuint
- easeInSine
- easeOutSine
- easeInOutSine
- easeInExpo
- easeOutExpo
- easeInOutExpo
- easeInCirc
- easeOutCirc
- easeInOutCirc
- easeInElastic
- easeOutElastic
- easeInOutElastic
- easeInBack
- easeOutBack
- easeInOutBack
- easeInBounce
- easeOutBounce
- easeInOutBounce