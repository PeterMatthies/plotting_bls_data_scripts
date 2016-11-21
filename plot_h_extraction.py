import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

__author__ = 'Peter Matthies'


file_name = '26-10-16-M4_horizontal_line_extract.txt'
m_data_file = '25-10-16-M6_hline_idc_0-20ma_6ghz_15dbm_30mt_ver2.txt'
data = np.loadtxt(file_name, skiprows=1)

m_data = np.loadtxt(m_data_file, skiprows=1)

colors = cm.rainbow(np.linspace(0, 1, 20))

m_data_x, m_data_y = [], []
dc_values = np.arange(0, 20, 1)
for i in range(0, 40, 2):
    m_data_x.append(m_data[:,i])
    m_data_y.append(m_data[:,i+1])
    # ax.plot(m_data[:,i], m_data[:,i+1], label='current ' + str(dc_value[i])+'mA', color=colors[i])


# all data plot

fig = plt.figure()
fig.suptitle('Phase resolved line scan: 6GHz at 15dBm, 30 mT\n25.10.2016', fontsize=12, fontweight='bold')
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

for m_x, m_y, col, dc_v in zip(m_data_x[:5], m_data_y[:5], colors[:5], dc_values[:5]):
    ax1.plot(m_x, m_y, label=str(dc_v)+'mA', color=col)
for m_x, m_y, col, dc_v in zip(m_data_x[5:10], m_data_y[5:10], colors[5:10], dc_values[5:10]):
    ax2.plot(m_x, m_y, label=str(dc_v)+'mA', color=col)
for m_x, m_y, col, dc_v in zip(m_data_x[10:15], m_data_y[10:15], colors[10:15], dc_values[10:15]):
    ax3.plot(m_x, m_y, label=str(dc_v)+'mA', color=col)
for m_x, m_y, col, dc_v in zip(m_data_x[15:20], m_data_y[15:20], colors[15:20], dc_values[15:20]):
    ax4.plot(m_x, m_y, label=str(dc_v)+'mA', color=col)


step_size = 0.223
actual_labels = np.linspace(0, 22.3, 10)
actual_labels = ["{0:.2f}".format(a_l) for a_l in actual_labels]
ax1.set_xticklabels(actual_labels)
ax2.set_xticklabels(actual_labels)
ax3.set_xticklabels(actual_labels)
ax4.set_xticklabels(actual_labels)


# custom_xticks = np.arange(0, 101, 5)
# plt.xticks(custom_xticks)


ax1.legend(prop={'size': 11})
ax1.grid()
ax1.set_ylabel('Intensity (a.u.)')

ax2.legend(prop={'size': 11})
ax2.grid()

ax3.legend(prop={'size': 11})
ax3.grid()
ax3.set_xlabel('Position starting from rf antenna \n along the Py stripe'+r' ($\mu m$)')
ax3.set_ylabel('Intensity (a.u.)')

ax4.set_xlabel('Position starting from rf antenna \n along the Py stripe'+r' ($\mu m$)')
ax4.legend(prop={'size': 11})
ax4.grid()




fig.tight_layout()
fig.subplots_adjust(top=0.89, right=0.96, left=0.11, bottom=0.12)
plt.savefig('25102016_phase_resolved_line_scans_all.png', format='png', dpi=1000)
plt.show()


# selected currents (0, 5, 10, 19 mA)

# fig2 = plt.figure()
# fig2.suptitle('Phase resolved line scan: 6GHz at 15dBm, 30 mT\n25.10.2016', fontsize=12, fontweight='bold')
# ax = fig2.add_subplot(111)
# ax.plot(m_data_x[0], m_data_y[0], label=str(dc_values[0])+' mA', color='black')
# ax.plot(m_data_x[5], m_data_y[5], label=str(dc_values[5])+' mA', color='blue')
# ax.plot(m_data_x[10], m_data_y[10], label=str(dc_values[10])+' mA', color='green')
# ax.plot(m_data_x[15], m_data_y[15], label=str(dc_values[15])+' mA', color='orange')
# ax.plot(m_data_x[19], m_data_y[19], label=str(dc_values[19])+' mA', color='red')
#
# y_line = np.arange(0, 18000, 5)
# # y_line = np.arange(0, 3500, 5)
# x_line = np.array([30 for i in range(len(y_line))])
# ax.plot(x_line, y_line, linestyle='--', color='red', label='DC line step')
#
# fig2.subplots_adjust(top=0.89, right=0.96, left=0.12, bottom=0.17)
#
#
# step_size = 0.223
# actual_labels = np.linspace(0, 22.3, 21)
# actual_labels = ["{0:.2f}".format(a_l) for a_l in actual_labels]
# ax.set_xticklabels(actual_labels)

#
# custom_xticks = np.arange(0, 101, 5)
# plt.xticks(custom_xticks)
#
# print(actual_labels)
# print(custom_xticks)
# plt.legend()
# plt.xticks(rotation=70)
# plt.grid()
# plt.ylabel('Intensity (a.u.)')
# plt.xlabel('Position starting from rf anttena \n along the Py stripe'+r' ($\mu m$)')
# plt.savefig('25102016_phase_resolved_line_scans_all.png', format='png', dpi=1000)
# plt.show()
