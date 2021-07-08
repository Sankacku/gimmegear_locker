from flask import Flask
# import time
# import lgpio
# relay_pin_1 = 24
# h = lgpio.gpiochip_open(0)
# lgpio.gpio_claim_output(h,relay_pin_1)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/<name>')
def hello_world2(name):
#     # lgpio.gpio_write(h,relay_pin_1, 1)
#     # time.sleep(20)
#     # lgpio.gpiochip_close(h)
#     # print("Still working")
    print(name)
    return f'Hello {name}! <h1> Unlocking 1 </h1>'
     


# if __name__ == "__main__":
#     app.run()
