from flask import Flask
# import time
# import lgpio
# relay_pin_1 = 24
# h = lgpio.gpiochip_open(0)
# lgpio.gpio_claim_output(h,relay_pin_1)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! <h1> Test </h1>'

# @app.route('/test')
# def hello_world2():
#     # print("Working here")
#     # lgpio.gpio_write(h,relay_pin_1, 1)
#     # time.sleep(20)
#     # lgpio.gpiochip_close(h)
#     # print("Still working")
#     return 'Hello World! <h1> Unlocking 1 </h1>'


# if __name__ == "__main__":
#     app.run()
