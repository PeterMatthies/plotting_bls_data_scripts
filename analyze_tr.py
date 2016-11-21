import matplotlib.pyplot as plt
import numpy as np

measurment_data = np.loadtxt('21112016_TR_data.txt', skiprows=1)

fig = plt.figure()
fig.suptitle("TR BLS: CW RF excitation at 8.7 GHz(-5 dBm) in 100 mT external field \n 50 ns 1V DC pulses | 21.11.2016 ",
             fontweight='bold')


ax = fig.add_subplot(111)
ax.plot(measurment_data[:,0], measurment_data[:,1])
plt.xlabel('Time (ns)')
plt.ylabel('Intensity (a.u.)')
plt.tight_layout()
plt.subplots_adjust(top= 0.90)
plt.grid()
plt.savefig('21112016-TR-M1.png', format='png', dpi=1000)
# plt.legend()
plt.show()