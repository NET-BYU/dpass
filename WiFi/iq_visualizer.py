import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import matplotlib.patches as patches




cmap = plt.get_cmap('viridis') # this may fail on older versions of matplotlib
cmap.set_under(color='k', alpha=None)


fig, axes = plt.subplots(1,3,sharey="all",figsize=(12,4))
dat = np.fromfile("/home/apal6981/work/IEEE_MASS_experiment_data/lora_1.iq",dtype=np.float32)
# print(dat)
dat = dat.astype(np.float32).view(np.complex64)
vmin = -120  # hide anything below -40 dB

NFFT = 1024  # FFT size
noverlap = NFFT // 2  # Overlap between segments
spec, freqs, times, im = axes[0].specgram(dat, Fs=.500e6, NFFT=NFFT, noverlap=noverlap, mode='magnitude', cmap=cmap, sides='twosided')

# Swap X and Y axes of the spectrogram
spec = spec.T
spec = np.flip(spec,axis=0)

# Set the extent of the plot to match the data
extent = [ -250000,250000,times[0], times[-1]]

vmin = -95  # Minimum value in dB
vmax = -90  # Maximum value in dB
vmin_lin = 10**(vmin/20)  # Minimum value in linear scale
vmax_lin = 10**(vmax/20)  # Maximum value in linear scale
# Apply the scaling to the spectrogram data
spec = np.clip(spec, vmin_lin, vmax_lin)  # Clip values to the range [vmin_lin, vmax_lin]
spec = 20*np.log10(spec)  # Convert back to dB scale

# Display the spectrogram
axes[2].imshow(spec, aspect='auto', cmap=cmap, extent=extent,vmin=vmin, vmax=vmax)

# Set axis labels
# axes[2].set_ylabel('Time (s)')
axes[2].set_xlabel('Frequency (MHz)')
axes[2].set_xticks([-100000,0,100000],["914","915","916"])
axes[2].set_xlim((-100000,100000))
# plt.yticks(np.arange(0,24,2),[str(i) for i in range(24,-1,-2)])
axes[2].invert_yaxis() 
# create a rectangle patch around the point of interest
rect = patches.Rectangle((-98000, 0.1), 196000, 8.5, linewidth=2, edgecolor='r', facecolor='none',label="Normal Traffic")
rect1 = patches.Rectangle((-98000, 8.85), 196000, (11.9-9), linewidth=2, edgecolor='yellow', facecolor='none',label="DPASS Packet")
rect2 = patches.Rectangle((-98000, 12), 196000, 24.3-12, linewidth=2, edgecolor='lime', facecolor='none',label="Non-DPASS Compliant traffic")


# add the rectangle patch to the plot
axes[2].add_patch(rect)
axes[2].add_patch(rect1)
axes[2].add_patch(rect2)





dat = np.fromfile("/home/apal6981/work/IEEE_MASS_experiment_data/wifi_4.iq",dtype=np.float32)
# # print(dat)
dat = dat.astype(np.float32).view(np.complex64)[21000000:266000000]
NFFT = 1024  # FFT size
noverlap = NFFT // 2  # Overlap between segments
spec, freqs, times, im = axes[1].specgram(dat, Fs=10e6, NFFT=NFFT, noverlap=noverlap, mode='magnitude', cmap=cmap, sides='twosided')

# Swap X and Y axes of the spectrogram
spec = spec.T
spec = np.flip(spec,axis=0)

# Set the extent of the plot to match the data
extent = [ -5000000,5000000,times[0], times[-1]]

vmin = -100  # Minimum value in dB
vmax = 0  # Maximum value in dB
vmin_lin = 10**(vmin/20)  # Minimum value in linear scale
vmax_lin = 10**(vmax/20)  # Maximum value in linear scale
# Apply the scaling to the spectrogram data
spec = np.clip(spec, vmin_lin, vmax_lin)  # Clip values to the range [vmin_lin, vmax_lin]
spec = 20*np.log10(spec)  # Convert back to dB scale

# Display the spectrogram
axes[0].imshow(spec, aspect='auto', cmap=cmap, extent=extent,vmin=vmin, vmax=vmax)

# Set axis labels
axes[0].set_ylabel('Time (s)')
axes[0].set_xlabel('Frequency (MHz)')
axes[0].set_xticks([-4000000,0,4000000],["2408","2412","2416"])
# axes[1].set_xlim((-100000,100000))
# plt.yticks(np.arange(0,24,2),[str(i) for i in range(24,-1,-2)])
axes[0].invert_yaxis()
rect = patches.Rectangle((-4900000, 0.1), 9800000, 8.5, linewidth=2, edgecolor='r', facecolor='none',label="Normal Traffic")
rect1 = patches.Rectangle((-4900000, 8.85), 9800000, (11.9-9), linewidth=2, edgecolor='yellow', facecolor='none',label="DPASS Packet")
rect2 = patches.Rectangle((-4900000, 12), 9800000, 24.3-12, linewidth=2, edgecolor='lime', facecolor='none',label="Non-DPASS Compliant traffic")


# add the rectangle patch to the plot
axes[0].add_patch(rect)
axes[0].add_patch(rect1)
axes[0].add_patch(rect2)






dat = np.fromfile("/home/apal6981/work/IEEE_MASS_experiment_data/srsran_4.iq",dtype=np.float32)
# # print(dat)
dat = dat.astype(np.float32).view(np.complex64)[21000000:266000000]
NFFT = 1024  # FFT size
noverlap = NFFT // 2  # Overlap between segments
spec, freqs, times, im = axes[1].specgram(dat, Fs=10e6, NFFT=NFFT, noverlap=noverlap, mode='magnitude', cmap=cmap, sides='twosided')

# Swap X and Y axes of the spectrogram
spec = spec.T
spec = np.flip(spec,axis=0)

# Set the extent of the plot to match the data
extent = [ -5000000,5000000,times[0], times[-1]]

vmin = -100  # Minimum value in dB
vmax = 0  # Maximum value in dB
vmin_lin = 10**(vmin/20)  # Minimum value in linear scale
vmax_lin = 10**(vmax/20)  # Maximum value in linear scale
# Apply the scaling to the spectrogram data
spec = np.clip(spec, vmin_lin, vmax_lin)  # Clip values to the range [vmin_lin, vmax_lin]
spec = 20*np.log10(spec)  # Convert back to dB scale

# Display the spectrogram
axes[1].imshow(spec, aspect='auto', cmap=cmap, extent=extent,vmin=vmin, vmax=vmax)

# Set axis labels
# axes[1].set_ylabel('Time (s)')
axes[1].set_xlabel('Frequency (MHz)')
axes[1].set_xticks([-4000000,0,4000000],["2463","2467","2471"])
# axes[1].set_xlim((-100000,100000))
# plt.yticks(np.arange(0,24,2),[str(i) for i in range(24,-1,-2)])
axes[1].invert_yaxis()
rect = patches.Rectangle((-4900000, 0.1), 9800000, 8.5, linewidth=2, edgecolor='r', facecolor='none',label="Normal Traffic")
rect1 = patches.Rectangle((-4900000, 8.85), 9800000, (11.9-9), linewidth=2, edgecolor='yellow', facecolor='none',label="DPASS Packet")
rect2 = patches.Rectangle((-4900000, 12), 9800000, 24.3-12, linewidth=2, edgecolor='lime', facecolor='none',label="Non-DPASS Compliant traffic")


# add the rectangle patch to the plot
axes[1].add_patch(rect)
axes[1].add_patch(rect1)
axes[1].add_patch(rect2)
plt.legend(handles=[rect,rect1,rect2], loc='lower right',ncols=1)



plt.tight_layout()
plt.show()