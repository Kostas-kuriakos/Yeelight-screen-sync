try:
    # Import the required packages
    from yeelight.main import Bulb
    from yeelight.main import BulbException
    from time import sleep
    from PIL import ImageGrab
    import json

except ModuleNotFoundError as module:
    # Handle the exception when a required module is not found
    print(f'Error while importing packages! {module}, Try installing all required packages')
    exit()

except Exception as e:
    # Handle any other exceptions
    print(e)
    exit()


with open('config.json') as json_file:
    data = json.load(json_file)
    BULB_IP = data["Bulb_IP"]
    DELAY = data["Transmit_Delay"]
 


bulb = Bulb(BULB_IP, effect="smooth", duration=700)

try:
    # Set the initial brightness and turn on the bulb
    bulb.set_brightness(100)
    bulb.turn_on()

except BulbException as e:
    # Handle the exception when the bulb cannot be turned on
    print(e)
    exit()


def getAverageRGB(image):
    npixels = image.size[0]*image.size[1]
    cols = image.getcolors(npixels)
    sumRGB = [(x[0]*x[1][0], x[0]*x[1][1], x[0]*x[1][2]) for x in cols]
    avg = tuple([sum(x)/npixels for x in zip(*sumRGB)])
    return avg

def getavg():
    printscreen_pil =  ImageGrab.grab()
    return getAverageRGB(printscreen_pil)

# Amplify the RGB values of an image
def amplify_rgb():
    r,g,b = getavg()
    if r * 2 > 255:
        r = 255
    else:
        r *= 2
    if g * 2 > 255:
        g = 255
    else:
        g *= 2
    if b * 2 > 255:
        b = 255
    else:
        b *= 2
    return int(r), int(g), int(b)


def main(DELAY:float):
    r, g, b = amplify_rgb()

    if r == 255 and g == 255 and b == 255:
        # If the RGB values are all 255, set the bulb to white and turn it on
        bulb.turn_on()
        bulb.set_rgb(r, g, b)
        bulb.set_color_temp(3700)

    elif r <= 80 and g <= 80 and b <= 82:
        # If the RGB values are all below a certain threshold, turn off the bulb
        bulb.turn_off()
        sleep(1)

    else:
        # Set the RGB values of the bulb to the amplified RGB values of the screen
        bulb.turn_on()
        bulb.set_rgb(r, g, b, )
    sleep(DELAY)

RESTARTS = 0

while True:    
    try:
        main(DELAY)
    
    except KeyboardInterrupt:
        # If the user interrupts the program, turn the bulb back on and set its color temperature to 3700K before breaking out of the loop
        bulb.turn_on()
        bulb.set_color_temp(3700)
        break

    except BulbException as e:
        # If the bulb throws an error, it may be due to too many requests,
        # so re-initialize the bulb and have a cooldown period before trying again
        RESTARTS += 1
        print(RESTARTS)
        sleep(1.5)
        bulb = Bulb(BULB_IP, effect="smooth", duration=700) 

    except Exception as e:
        # If there is any other unexpected error, print the error message and break out of the loop
        print(e)
        break
