from flask import Flask
import time
import lgpio


relay_pin_1 = 2
relay_pin_2 = 3
relay_pin_3 = 4
relay_pin_4 = 14
relay_pin_5 = 15
relay_pin_6 = 18


pin_nr1 = lgpio.gpiochip_open(1)
pin_nr2 = lgpio.gpiochip_open(1)
pin_nr3 = lgpio.gpiochip_open(1)
pin_nr4 = lgpio.gpiochip_open(1)
pin_nr5 = lgpio.gpiochip_open(1)
pin_nr6 = lgpio.gpiochip_open(1)
lgpio.gpio_claim_output(pin_nr1,relay_pin_1)
lgpio.gpio_claim_output(pin_nr2,relay_pin_2)
lgpio.gpio_claim_output(pin_nr3,relay_pin_3)
lgpio.gpio_claim_output(pin_nr4,relay_pin_4)
lgpio.gpio_claim_output(pin_nr5,relay_pin_5)
lgpio.gpio_claim_output(pin_nr6,relay_pin_6)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/<number>')
def hello_world2(number):
#     # lgpio.gpio_write(h,relay_pin_1, 1)
#     # time.sleep(20)
#     # lgpio.gpiochip_close(h)
#     # print("Still working")
    print("Going to activate Number: " + number + " for 3 Seconds now")
    if int(number) == 1:
        lgpio.gpio_write(pin_nr1,relay_pin_1, 0)
        time.sleep(3)
        lgpio.gpio_write(pin_nr1,relay_pin_1, 1)
    elif int(number) == 2:
        lgpio.gpio_write(pin_nr2,relay_pin_2, 0)
        time.sleep(3)
        lgpio.gpio_write(pin_nr2,relay_pin_2, 1)
    elif int(number) == 3:
        lgpio.gpio_write(pin_nr3,relay_pin_3, 0)
        time.sleep(3)
        lgpio.gpio_write(pin_nr3,relay_pin_3, 1)
    elif int(number) == 4:
        lgpio.gpio_write(pin_nr4,relay_pin_4, 0)
        time.sleep(3)
        lgpio.gpio_write(pin_nr4,relay_pin_4, 1)
    elif int(number) == 5:
        lgpio.gpio_write(pin_nr5,relay_pin_5, 0)
        time.sleep(3)
        lgpio.gpio_write(pin_nr5,relay_pin_5, 1)
    elif int(number) == 6:
        lgpio.gpio_write(pin_nr6,relay_pin_6, 0)
        time.sleep(3)
        lgpio.gpio_write(pin_nr6,relay_pin_6, 1)
    else:
        print("noob")
    return f'<h1> Hello !! </h1> <h1> Unlocking {number} </h1>'
     

if __name__ == "__main__":
    app.run(host="0.0.0.0")
