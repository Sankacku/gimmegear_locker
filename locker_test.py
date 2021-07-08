#  Blink an LED with the LGPIO library
#  Uses lgpio library, compatible with kernel 5.11
#  Author: William 'jawn-smith' Wilson

import time
import lgpio

LED = 24

# open the gpio chip and set the LED pin as output
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, LED)

try:
    # x = 0.1
    # while x<8:
    #     # Turn the GPIO pin on
    #     lgpio.gpio_write(h, LED, 1)
    #     time.sleep(x)

    #     # Turn the GPIO pin off
    #     lgpio.gpio_write(h, LED, 0)
    #     time.sleep(x)
    #     x = x + 1
    lgpio.gpio_write(h, LED, 0)
    time.sleep(20)
    lgpio.gpiochip_close(h)
except KeyboardInterrupt:
    lgpio.gpio_write(h, LED, 0)
    lgpio.gpiochip_close(h)