<img src="assets/logo.png" alt="Alt text" width="1000" />


[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# PgTimer - A Simple PyGame Timer Library
> A lightweight Python timer and tweening library inspired by Love2D's [Hump](https://github.com/vrld/hump) library with built-in support for multiple easing functions from [pytweening](https://github.com/asweigart/pytweening), designed for easy time-based animations and delayed callbacks.
-----

<br/>

# Contents
- [Instalation](#instalation)
- [Quick start](#quick-start)
    - [Updating the timer](#update-the-timer)
    - [Creating a pulsing rectangle](#create-a-pulsing-rectangle)
- [Examples](#examples)
- [Documentation](#documentation)
    - [After](#afterdelay-callback)
    - [Tween](#tweenduration-start_value-end_value-on_update-easing-callback)
    - [Custom Easing type](#add_easing_typename-function)
    - [Easing types](#get_easing_types)


-----

<br/>

# Instalation
```bash
git clone https://github.com/clxakz/pgtimer
```
or
```bash
pip install pgtimer
```

-----

<br/>

# Quick start
place the `pgtimer` folder inside your project and import it
```python
from pgtimer import Timer
```

# Update the Timer
In your main loop update the `Timer` with delta time
> [!NOTE]
> There's no need to instantiate the timer using `timer = Timer()` since an instance is already created and exposed as Timer at the module level
```python
while running:
    dt = clock.tick(60) / 1000
    Timer.update(dt)
```

# Create a pulsing rectangle
As an example we can use tweens to pulse a rectangle on the screen <br/>
See [pulse.py](https://github.com/clxakz/pgtimer/blob/main/examples/pulse.py) for full example
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

# Examples
Animation example #1
```python
class Cube():
    def __init__(self, x, y):
        self.surface = pygame.Surface((100,100))
        self.surface.fill((255,255,255))

        self.rect = self.surface.get_frect(center=(x, y))

    def draw(self, screen: pygame.Surface):
        screen.blit(self.surface, self.rect)

cube = Cube(100, 100)


def animate():
    Timer.tween(1, cube.rect.centerx, 400, lambda v: setattr(cube.rect, "centerx", v), "easeInOutQuad", lambda:             # Tween x position from 100 > 400
        Timer.tween(1, cube.rect.centery, 400, lambda v: setattr(cube.rect, "centery", v), "easeInOutQuad", lambda:         # Tween y position from 100 > 400
            Timer.tween(1, cube.rect.centerx, 100, lambda v: setattr(cube.rect, "centerx", v), "easeInOutQuad", lambda:     # Tween x position from 400 > 100
                Timer.tween(1, cube.rect.centery, 100, lambda v: setattr(cube.rect, "centery", v), "easeInOutQuad", animate # Tween y position from 400 > 100 and repeat
                )
            )
        )
    )
```
And that looks like <br/>
<img src="assets/demo2.gif" alt="Alt text" width="500" />

-----

<br/>


# Documentation
### `.after(delay, callback)`
The `after()` function will run a callback function after a set time
```python
Timer.after(1, print("Done!")) # <- Prints 'Done!' after 1 second
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

Timer.tween(1, 0, 255, set_value, "easeOutQuad", print("Done!")) # <- Smoothly animates alpha from 0 to 255 using the easeOutQuad easing type. Prints 'Done!' when finished.
```

Arguments
- `duration` `int` - Duration in seconds
- `start_value` `int` - The start value
- `end_value` `int` - The end value
- `on_update` `callable` - Returns the updated value as float
- `easing` `str` - Sets the easing type
- `callback` `callable` - An optional callback function, none by default

-----

> [!TIP]
> You can nest `after` and `tween` functions to build a sequence of animations

<br/>

-----

### `.add_easing_type(name, function)`
The `add_easing_type()` function can be used to add your own custom easing type
```python
def easeInCustom(t):
    return math.pow(t, 3)

Timer.add_easing_type("custom", easeInCustom)
```

Arguments
- `name` `str` - The name of you custom easing type
- `function` `callable` - The function for your custom easing type

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
