#MIT License
#
#Copyright (c) 2025 clxakz
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import pytweening
from typing import Callable, Optional

_easing_functions = {
    "linear": lambda t: t,
    "easeInQuad": pytweening.easeInQuad,
    "easeOutQuad": pytweening.easeOutQuad,
    "easeInOutQuad": pytweening.easeInOutQuad,
    "easeInCubic": pytweening.easeInCubic,
    "easeOutCubic": pytweening.easeOutCubic,
    "easeInOutCubic": pytweening.easeInOutCubic,
    "easeInQuart": pytweening.easeInQuart,
    "easeOutQuart": pytweening.easeOutQuart,
    "easeInOutQuart": pytweening.easeInOutQuart,
    "easeInQuint": pytweening.easeInQuint,
    "easeOutQuint": pytweening.easeOutQuint,
    "easeInOutQuint": pytweening.easeInOutQuint,
    "easeInSine": pytweening.easeInSine,
    "easeOutSine": pytweening.easeOutSine,
    "easeInOutSine": pytweening.easeInOutSine,
    "easeInExpo": pytweening.easeInExpo,
    "easeOutExpo": pytweening.easeOutExpo,
    "easeInOutExpo": pytweening.easeInOutExpo,
    "easeInCirc": pytweening.easeInCirc,
    "easeOutCirc": pytweening.easeOutCirc,
    "easeInOutCirc": pytweening.easeInOutCirc,
    "easeInElastic": pytweening.easeInElastic,
    "easeOutElastic": pytweening.easeOutElastic,
    "easeInOutElastic": pytweening.easeInOutElastic,
    "easeInBack": pytweening.easeInBack,
    "easeOutBack": pytweening.easeOutBack,
    "easeInOutBack": pytweening.easeInOutBack,
    "easeInBounce": pytweening.easeInBounce,
    "easeOutBounce": pytweening.easeOutBounce,
    "easeInOutBounce": pytweening.easeInOutBounce,
}

def _get_easing_function(easing_name: str):
    if not easing_name in _easing_functions: print(f"Easing type '{easing_name}' is invalid. Use 'Timer.get_easing_types()' to list all easing types.")
    return _easing_functions.get(easing_name, lambda t: t)


class __Timer():
    def __init__(self):
        self.timers = []
        self.tweens = []


    def get_easing_types(self):
        return list(_easing_functions.keys())

    
    def after(self, delay: int, callback: Optional[Callable[[], None]] = None):
        data = {
            "timer": 0,
            "delay": delay,
            "callback": callback
        }

        self.timers.append(data)


    def tween(self, duration: int, start_value: float, end_value: float, on_update: Callable[[float], float], easing: str = "linear", callback: Optional[Callable[[], None]] = None):
        easing_func = _get_easing_function(easing)
        data = {
            "timer": 0,
            "duration": duration,
            "start": start_value,
            "end": end_value,
            "on_update": on_update,
            "easing": easing_func,
            "callback": callback
        }
        self.tweens.append(data)


    def update(self, dt):
        # Timers
        timers_to_remove = []
        for timer in self.timers:
            timer["timer"] += dt

            if timer["timer"] >= timer["delay"]:
                if timer["callback"]:
                    timer["callback"]()
                timers_to_remove.append(timer)


        # Tweens
        tweens_to_remove = []
        for tween in self.tweens:
            tween["timer"] += dt
            
            raw_progress = min(tween["timer"] / tween["duration"], 1.0)
            eased_progress = tween["easing"](raw_progress)
            value = tween["start"] + (tween["end"] - tween["start"]) * eased_progress
            tween["on_update"](value)

            if raw_progress >= 1.0:
                if tween["callback"]:
                    tween["callback"]()
                tweens_to_remove.append(tween)

        # Clear timers and tweens
        for timer in timers_to_remove: self.timers.remove(timer)
        for tween in tweens_to_remove: self.tweens.remove(tween)


Timer = __Timer()