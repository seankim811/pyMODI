import numpy as np
import modi as md 
import time

# Acceleration X, Y, Z
ax = []
ay = []
az = []

# Gyro X, Y Z
gx = []
gy = []
gz = []

# Roll, Pitch, Yaw
roll = []
pitch = []
yaw = []

# Time tick
tick = []

bundle = md.MODI()

time.sleep(5)

gyro = bundle.gyros[0]

print( "start log\n")

# Read the 6-DOF Gryo-Accel-RPY value at every 50mS
filename = ""
filename = "log" + str(time.time()) + ".csv"

for i in range(1, 20):
    tick.append( time.time() ) 
    ax.append(gyro.acceleration_x())
    ay.append(gyro.acceleration_y())
    az.append(gyro.acceleration_z())
    gx.append(gyro.angular_vel_x())
    gy.append(gyro.angular_vel_y())
    gz.append(gyro.angular_vel_z())
    roll.append( gyro.roll())
    pitch.append( gyro.pitch() )
    yaw.append( gyro.yaw() )
    #delay in 50mS
    time.sleep(0.05)

filename = ""
filename = "log" + str(time.time()) + ".csv"
np.savetxt(filename, (tick, ax, ay, ay, gx, gy, gz, roll, pitch, yaw), delimiter=",")
print( "end log\n")