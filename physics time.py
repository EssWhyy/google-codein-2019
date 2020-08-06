'''For our upcoming liquid galaxy project related to the space and also for the past project Airmashup we need some calculations.

Code an script that calculates the final position of an aircraft with a given values of initial position inputed as parameters over a given time i.e. :
For an aircraft flying at t=0 being at lat=34.8 and lon=20.1, with a height of 8000 m and horizontal velocity = 300 m/s and vertical velocity = 4m/s, where will this plane be in 30 seconds?

The script should be able to read:

latitude longitude height horizontal velocity vertical velocity time

And generate as output the final values of position OBSERVATIONS: Do not consider accelerations! PYTHON RECOMMENDED'''

import math, sys

class Plane:
    def __init__(self, name, latitude, longitude, height, horizontalvelocity, verticalvelocity, heading): #7 variables.

        self.name = name
        self.lat = float(latitude)
        self.lon = float(longitude)
        self.h = float(height)
        self.vel = float(horizontalvelocity) # 2 dimensions, x and y form the plane's main flight velocity.
        self.z_vel = float(verticalvelocity) # aka the plane's lift
        self.heading = float(heading) # bearing in which the plane is flying towards, 0 to 360.


    def forecastposition(self, timepassed): #shows the final coordinates of the plane after x seconds

        x_dist = self.vel * math.sin(self.heading) * timepassed
        y_dist = self.vel * math.cos(self.heading) * timepassed
        z_dist = self.z_vel * timepassed

        lat_final = self.lat + (y_dist / 111000.000000 * 1.000000) #on average, 111000m = 1 degree of latitude throughout
        lon_final = self.lon + (x_dist / (math.cos((self.lat+lat_final)/2) * 111321.000000) )  #derived from latitude. Not considering earth's rotational acceleration.
        h_final = self.h + z_dist #lat and lon have an accuracy of 6 decimal places.

        statement = 'flightnumber:' + str(self.name) + ',latitude:' + str(lat_final) + ', longitude:' + str(lon_final) + ', height:' + str(h_final)

        print(statement)



if __name__ == '__main__':
    #list out whatever coordinates /time you want here.
    while True:
        try:
            plane1 = Plane(input('Enter name'),input('Enter current latitude'),input('Enter current longitude'),input('Enter current height'),input('Enter Horizontal velocity'),input('Enter Vertical velocity'),input('Enter Heading'))
            plane1.forecastposition(float(input('Seconds elapsed?')))
        except:
            print('Error, you have entered an invalid parameter, name variable must be a string and all other variables must be numbers only.')

        loop = input("Press N to exit, else press any key to check another plane")
        if loop == 'n':
            sys.exit()
        else:
            continue
