from flask import Flask
import time
import lgpio

#lgpio.gpiochip_close(0)

def activate_for_3_sec(pin_nr):
    pin_open = lgpio.gpiochip_open(0)
    #lgpio.gpio_claim_output(pin_open,pin_nr)
    lgpio.gpio_write(pin_open,pin_nr, 0)
    time.sleep(3)
    lgpio.gpio_write(pin_open,pin_nr, 1)
    lgpio.gpio_free(pin_nr)
    lgpio.gpiochip_close(0)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/<number>')
def hello_world2(number):
    print("Going to activate Number: " + number + " for 3 Seconds now")
    if int(number) == 1:
        activate_for_3_sec(2)
    elif int(number) == 2:
        activate_for_3_sec(3)
    elif int(number) == 3:
        activate_for_3_sec(4)
    elif int(number) == 4:
        activate_for_3_sec(14)
    elif int(number) == 5:
        activate_for_3_sec(15)
    elif int(number) == 6:
       activate_for_3_sec(18)
    else:
        print("noob")
    return f'<h1> Hello !! </h1> <h1> Unlocking {number} </h1>'
     


if __name__ == "__main__":
    app.run(host="0.0.0.0")
