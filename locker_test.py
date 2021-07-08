#  Blink anrelay_pin_1 with the LGPIO library
#  Uses lgpio library, compatible with kernel 5.11
#  Author: William 'jawn-smith' Wilson

import time
import lgpio
relay_pin_1 = 24

# open the gpio chip and set therelay_pin_1 pin as output
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h,relay_pin_1)

try:
    print("Working here")
    # x = 0.1
    # while x<8:
    #     # Turn the GPIO pin on
    #     lgpio.gpio_write(h,relay_pin_1, 1)
    #     time.sleep(x)

    #     # Turn the GPIO pin off
    #     lgpio.gpio_write(h,relay_pin_1, 0)
    #     time.sleep(x)
    #     x = x + 1
    lgpio.gpio_write(h,relay_pin_1, 0)
    time.sleep(20)
    lgpio.gpio_write(h,relay_pin_1, 1)
    lgpio.gpiochip_close(h)
    print("Still working")
except KeyboardInterrupt:
    print("Not working here")