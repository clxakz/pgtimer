# PyTimer - A PyGame Timer Library
> A lightweight Python timer and tweening library insired by Love2D's [Hump](https://github.com/vrld/hump) library with built-in support for multiple easing functions from [pytweening](https://github.com/asweigart/pytweening), designed for easy time-based animations and delayed callbacks.

-----

# Instalation
```bash
git clone https://github.com/clxakz/pytimer
```
or
```bash
pip install pytimerlib
```

-----

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
As an example we can use tweens to pulse a rectangle on the screen
See [pulsing.py](https://github.com/clxakz/pytimer/blob/main/examples/pulse.py) for full example
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

And that looks like
