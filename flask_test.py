from flask import Flask
import time
import lgpio
relay_pin_1 = 24
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h,relay_pin_1)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! <h1> Test </h1>'

@app.route('/test/')
def hello_world():
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
        lgpio.gpio_write(h,relay_pin_1, 1)
        time.sleep(20)
        lgpio.gpiochip_close(h)
        print("Still working")
    except KeyboardInterrupt:
        print("Not working here")
    return 'Hello World! <h1> Unlocking 1 </h1>'


if __name__ == "__main__":
    app.run()