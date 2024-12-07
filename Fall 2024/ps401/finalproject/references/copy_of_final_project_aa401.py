# -*- coding: utf-8 -*-

'Normalized Flux (mW/m^2/Å)'

NO_VALUES_TO_CALCULATE_THE_AVERAGE = "No values to calculate the average."


# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate



#Read in the spectral atlas data
file1 = '/content/drive/MyDrive/Colab Notebooks/5-Stellar Atlas/spectra1.dat'
 #Spectra #1
file10 = '/content/drive/MyDrive/Colab Notebooks/5-Stellar Atlas/spectra10.dat'
 #Spectra #10
file11 = '/content/drive/MyDrive/Colab Notebooks/5-Stellar Atlas/spectra11.dat'
 #Spectra #11
file12 = '/content/drive/MyDrive/Colab Notebooks/5-Stellar Atlas/spectra12.dat'
 #Spectra #12
file13 = '/content/drive/MyDrive/Colab Notebooks/5-Stellar Atlas/spectra13.dat'
 #Spectra #13
file14 = '/content/drive/MyDrive/Colab Notebooks/5-Stellar Atlas/spectra14.dat'
 #Spectra #14
file15 = '/content/drive/MyDrive/Colab Notebooks/5-Stellar Atlas/spectra15.dat'
 #Spectra #15
file2 = '/content/drive/MyDrive/Colab Notebooks/5-Stellar Atlas/spectra2.dat'
 #Spectra #2
file3 = '/content/drive/MyDrive/Colab Notebooks/5-Stellar Atlas/spectra3.dat'
 #Spectra #3
file4 = '/content/drive/MyDrive/Colab Notebooks/5-Stellar Atlas/spectra4.dat'
 #Spectra #4
file5 = '/content/drive/MyDrive/Colab Notebooks/5-Stellar Atlas/spectra5.dat'
 #Spectra #5
file6 = '/content/drive/MyDrive/Colab Notebooks/5-Stellar Atlas/spectra6.dat'
 #Spectra #6
file7 = '/content/drive/MyDrive/Colab Notebooks/5-Stellar Atlas/spectra7.dat'
 #Spectra #7
file8 = '/content/drive/MyDrive/Colab Notebooks/5-Stellar Atlas/spectra8.dat'
 #Spectra #8
file9 = '/content/drive/MyDrive/Colab Notebooks/5-Stellar Atlas/spectra9.dat'
 #Spectra #9
Spectra1 = np.loadtxt(file1, skiprows=3)
Spectra10 = np.loadtxt(file10, skiprows=3)
Spectra11 = np.loadtxt(file11, skiprows=3)
Spectra12 = np.loadtxt(file12, skiprows=3)
Spectra13 = np.loadtxt(file13, skiprows=3)
Spectra14 = np.loadtxt(file14, skiprows=3)
Spectra15 = np.loadtxt(file15, skiprows=3)
Spectra2 = np.loadtxt(file2, skiprows=3)
Spectra3 = np.loadtxt(file3, skiprows=3)
Spectra4 = np.loadtxt(file4, skiprows=3)
Spectra5 = np.loadtxt(file5, skiprows=3)
Spectra6 = np.loadtxt(file6, skiprows=3)
Spectra7 = np.loadtxt(file7, skiprows=3)
Spectra8 = np.loadtxt(file8, skiprows=3)
Spectra9 = np.loadtxt(file9, skiprows=3)

#Read in my Mystery star data (star 12 in section 2)
file16 = '/content/drive/MyDrive/Colab Notebooks/star12.txt'
 #Mystery star spectra
Spectra16 = np.loadtxt(file16, skiprows=1)


#Plotting my mystery star alone to see the full spectra of my star to then plot with the other normalized spectral data
fig = plt.figure(figsize=(12, 8))
axes = fig.add_subplot(111)
axes.plot(Spectra16[:, 0], Spectra16[:, 1] / max(Spectra16[:, 1]) + 0, label='MStar12')
plt.xlim(3500, 9500)
plt.title('Stellar Atlas Spectra of Mystery Star 12')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")

fig = plt.figure(figsize=(12, 8))
axes = fig.add_subplot(111)

axes.plot(Spectra1[:, 0], Spectra1[:, 1] / max(Spectra1[:, 1]) + 8, label='F2 V')
axes.plot(Spectra2[:, 0], Spectra2[:, 1] / max(Spectra2[:, 1]) + 5, label='G8 V')
axes.plot(Spectra3[:, 0], Spectra3[:, 1] / max(Spectra3[:, 1]) + 6, label='G2 V')
axes.plot(Spectra4[:, 0], Spectra4[:, 1] / max(Spectra4[:, 1]) + 3, label='M0 V')
axes.plot(Spectra5[:, 0], Spectra5[:, 1] / max(Spectra5[:, 1]) + 12, label='B3 V')
axes.plot(Spectra6[:, 0], Spectra6[:, 1] / max(Spectra6[:, 1]) + 14, label='O9 V')
axes.plot(Spectra7[:, 0], Spectra7[:, 1] / max(Spectra7[:, 1]) + 4, label='K5 V')
axes.plot(Spectra8[:, 0], Spectra8[:, 1] / max(Spectra8[:, 1]) + 7, label='F8 V')
axes.plot(Spectra9[:, 0], Spectra9[:, 1] / max(Spectra9[:, 1]) + 2, label='M6 V')
axes.plot(Spectra10[:, 0], Spectra10[:, 1] / max(Spectra10[:, 1]) + 11, label='B9 V')
axes.plot(Spectra11[:, 0], Spectra11[:, 1] / max(Spectra11[:, 1]) + 10, label='A0 V')
axes.plot(Spectra12[:, 0], Spectra12[:, 1] / max(Spectra12[:, 1]) + 13, label='O5 V')
axes.plot(Spectra13[:, 0], Spectra13[:, 1] / max(Spectra13[:, 1]) + 9, label='A5 V')
axes.plot(Spectra14[:, 0], Spectra14[:, 1] / max(Spectra14[:, 1]) + 15, label=' WN5')
axes.plot(Spectra15[:, 0], Spectra15[:, 1] / max(Spectra15[:, 1]) + 1, label='L5')
axes.plot(Spectra16[:, 0], Spectra16[:, 1] / max(Spectra16[:, 1]) + 0, label='MStar12')

plt.xlim(3500, 9500)
plt.title('Stellar Atlas Spectra')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")

#Labelling each line and giving it coordinates that correspond to the relevant lines
plt.text(9500, 14, 'O5 V', size=15)
plt.text(9500, 13, 'O9 V', size=15)
plt.text(9500, 12, 'B3 V', size=15)
plt.text(9500, 11, 'B9 V', size=15)
plt.text(9500, 10, 'A0 V', size=15)
plt.text(9500, 9, 'A5 V', size=15)
plt.text(9500, 8, 'F2 V', size=15)
plt.text(9500, 7.15, 'F8 V', size=15)
plt.text(9500, 6, 'G2 V', size=15)
plt.text(9500, 5.3, 'G8 V', size=15)
plt.text(9500, 4.7, 'K5 V', size=15)
plt.text(9500, 3.7, 'M0 V', size=15)
plt.text(9500, 2.375, 'M6 V', size=15)
plt.text(9500, 1, 'L5', size=15)
plt.text(9500, 15, 'WN5', size=15)
plt.text(9500, 0.28, 'MStar12', size=15)

fig = plt.figure(figsize=(12, 8))
axes = fig.add_subplot(111)

axes.plot(Spectra1[:, 0], Spectra1[:, 1] / max(Spectra1[:, 1]) + 8, label='F2 V')
axes.plot(Spectra2[:, 0], Spectra2[:, 1] / max(Spectra2[:, 1]) + 5, label='G8 V')
axes.plot(Spectra3[:, 0], Spectra3[:, 1] / max(Spectra3[:, 1]) + 6, label='G2 V')
axes.plot(Spectra4[:, 0], Spectra4[:, 1] / max(Spectra4[:, 1]) + 3, label='M0 V')
axes.plot(Spectra5[:, 0], Spectra5[:, 1] / max(Spectra5[:, 1]) + 12, label='B3 V')
axes.plot(Spectra6[:, 0], Spectra6[:, 1] / max(Spectra6[:, 1]) + 14, label='O9 V')
axes.plot(Spectra7[:, 0], Spectra7[:, 1] / max(Spectra7[:, 1]) + 4, label='K5 V')
axes.plot(Spectra8[:, 0], Spectra8[:, 1] / max(Spectra8[:, 1]) + 7, label='F8 V')
axes.plot(Spectra9[:, 0], Spectra9[:, 1] / max(Spectra9[:, 1]) + 2, label='M6 V')
axes.plot(Spectra10[:, 0], Spectra10[:, 1] / max(Spectra10[:, 1]) + 11, label='B9 V')
axes.plot(Spectra11[:, 0], Spectra11[:, 1] / max(Spectra11[:, 1]) + 10, label='A0 V')
axes.plot(Spectra12[:, 0], Spectra12[:, 1] / max(Spectra12[:, 1]) + 13, label='O5 V')
axes.plot(Spectra13[:, 0], Spectra13[:, 1] / max(Spectra13[:, 1]) + 9, label='A5 V')
axes.plot(Spectra14[:, 0], Spectra14[:, 1] / max(Spectra14[:, 1]) + 15, label=' WN5')
axes.plot(Spectra15[:, 0], Spectra15[:, 1] / max(Spectra15[:, 1]) + 1, label='L5')
axes.plot(Spectra16[:, 0], Spectra16[:, 1] / max(Spectra16[:, 1]) + 0, label='MStar12')

plt.xlim(3500, 7500)
plt.title('Stellar Atlas Spectra in the Visible Wavelenth Range')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")

#Labelling each line and giving it coordinates that correspond to the relevant lines
plt.text(7500, 14, 'O5 V', size=15)
plt.text(7500, 13, 'O9 V', size=15)
plt.text(7500, 12, 'B3 V', size=15)
plt.text(7500, 11, 'B9 V', size=15)
plt.text(7500, 10, 'A0 V', size=15)
plt.text(7500, 9, 'A5 V', size=15)
plt.text(7500, 8, 'F2 V', size=15)
plt.text(7500, 7.15, 'F8 V', size=15)
plt.text(7500, 6, 'G2 V', size=15)
plt.text(7500, 5.3, 'G8 V', size=15)
plt.text(7500, 4.7, 'K5 V', size=15)
plt.text(7500, 3.7, 'M0 V', size=15)
plt.text(7500, 2.375, 'M6 V', size=15)
plt.text(7500, 1, 'L5', size=15)
plt.text(7500, 15, 'WN5', size=15)
plt.text(7500, 0.28, 'MStar12', size=15)
#defining the wavelengths of my mystery star to interpolate that data
x_old = Spectra16[:, 0]
#the wavelength and flux values for the spectral atlas data
x_grid = Spectra1[:, 0]
y_grid = Spectra1[:, 1]
y_new = np.interp(x_old, x_grid, y_grid)
#creating the arrays for the new interpolated plot
xnew = np.array(Spectra16)[:, 0]
ynew = np.array(y_new)
#inputting parameters for the new mystery plot
wopt = np.where((Spectra16[:, 0] > 3500) & (Spectra16[:, 0] < 7500))
x_old = Spectra16[:, 0]
y_old = Spectra16[:, 1]
x_list = x_old[wopt]
y_list = y_old[wopt]
slope, intercept = np.polyfit(x_list, y_list, 1)
ynorm = y_list / (slope * x_list + intercept)
variance = np.std(ynorm)
obs = Spectra16[:, 1] / np.max(Spectra16[:, 1])
exp = ynew

#computing the Chi Squared function and printing the function
vals = []
for i in range(len(exp)):
    val = (obs[i] - exp[i]) ** 2 / variance
    vals.append(val)
chi2 = sum(vals)
red_chi2 = chi2 / (len(y_old) - 1)
print(chi2)
print(red_chi2)

#plotting the first spectral atlas interpolated data against the interpolated mystery star data within the visible wavelength range
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(111)
plt.xlim(3500, 7500)
plt.title('Interpolated Data: Spectra1 vs. Spectra16')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")
axes.plot(x_old, y_new - 0.4, label="Interpolated Spectra 1 Data (F2 V-Type Star)")
axes.plot(x_old, Spectra16[:, 1] / np.max(Spectra16[:, 1]), label="Mystery Star 12")
axes.plot(6000, 0, label="Reduced Chi Squared Value = 0.0081438", color="white")
axes.legend()
#defining the wavelengths of my mystery star to interpolate that data
x_old = Spectra16[:, 0]
#the wavelength and flux values for the spectral atlas data
x_grid = Spectra2[:, 0]
y_grid = Spectra2[:, 1]
y_new = np.interp(x_old, x_grid, y_grid)
#creating the arrays for the new interpolated plot
xnew = np.array(Spectra16)[:, 0]
ynew = np.array(y_new)
#inputting parameters for the new mystery plot
wopt = np.where((Spectra16[:, 0] > 3500) & (Spectra16[:, 0] < 7500))
x_old = Spectra16[:, 0]
y_old = Spectra16[:, 1]
x_list = x_old[wopt]
y_list = y_old[wopt]
slope, intercept = np.polyfit(x_list, y_list, 1)
ynorm = y_list / (slope * x_list + intercept)
variance = np.std(ynorm)
obs = Spectra16[:, 1] / np.max(Spectra16[:, 1])
exp = ynew

#computing the Chi Squared function and printing the function
vals = []
for i in range(len(exp)):
    val = (obs[i] - exp[i]) ** 2 / variance
    vals.append(val)
chi2 = sum(vals)
red_chi2 = chi2 / (len(y_old) - 1)
print(chi2)
print(red_chi2)

#plotting the first spectral atlas interpolated data against the interpolated mystery star data within the visible wavelength range
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(111)
plt.xlim(3500, 7500)
plt.title('Interpolated Data: Spectra2 vs. Spectra16')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")
axes.plot(x_old, y_new - 0.4, label="Interpolated Spectra 2 Data (G8 V-Type Star)")
axes.plot(x_old, Spectra16[:, 1] / np.max(Spectra16[:, 1]), label="Mystery Star 12")
axes.plot(6000, 0, label="Reduced Chi Squared Value = 0.0062272", color="white")
axes.legend()
#defining the wavelengths of my mystery star to interpolate that data
x_old = Spectra16[:, 0]
#the wavelength and flux values for the spectral atlas data
x_grid = Spectra3[:, 0]
y_grid = Spectra3[:, 1]
y_new = np.interp(x_old, x_grid, y_grid)
#creating the arrays for the new interpolated plot
xnew = np.array(Spectra16)[:, 0]
ynew = np.array(y_new)
#inputting parameters for the new mystery plot
wopt = np.where((Spectra16[:, 0] > 3500) & (Spectra16[:, 0] < 7500))
x_old = Spectra16[:, 0]
y_old = Spectra16[:, 1]
x_list = x_old[wopt]
y_list = y_old[wopt]
slope, intercept = np.polyfit(x_list, y_list, 1)
ynorm = y_list / (slope * x_list + intercept)
variance = np.std(ynorm)
obs = Spectra16[:, 1] / np.max(Spectra16[:, 1])
exp = ynew

#computing the Chi Squared function and printing the function
vals = []
for i in range(len(exp)):
    val = (obs[i] - exp[i]) ** 2 / variance
    vals.append(val)
chi2 = sum(vals)
red_chi2 = chi2 / (len(y_old) - 1)
print(chi2)
print(red_chi2)

#ploting the first spectral atlas interpolated data against the interpolated mystery star data within the visible wavelength range
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(111)
plt.xlim(3500, 7500)
plt.title('Interpolated Data: Spectra3 vs. Spectra16')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")
axes.plot(x_old, y_new - 0.4, label="Interpolated Spectra 3 Data (G2 V-Type Star)")
axes.plot(x_old, Spectra16[:, 1] / np.max(Spectra16[:, 1]), label="Mystery Star 12")
axes.plot(6000, 0, label="Reduced Chi Squared Value = 0.0067063", color="white")
axes.legend()
#defining the wavelengths of my mystery star to interpolate that data
x_old = Spectra16[:, 0]
#the wavelength and flux values for the spectral atlas data
x_grid = Spectra4[:, 0]
y_grid = Spectra4[:, 1]
y_new = np.interp(x_old, x_grid, y_grid)
#creating the arrays for the new interpolated plot
xnew = np.array(Spectra16)[:, 0]
ynew = np.array(y_new)
#inputting parameters for the new mystery plot
wopt = np.where((Spectra16[:, 0] > 3500) & (Spectra16[:, 0] < 7500))
x_old = Spectra16[:, 0]
y_old = Spectra16[:, 1]
x_list = x_old[wopt]
y_list = y_old[wopt]
slope, intercept = np.polyfit(x_list, y_list, 1)
ynorm = y_list / (slope * x_list + intercept)
variance = np.std(ynorm)
obs = Spectra16[:, 1] / np.max(Spectra16[:, 1])
exp = ynew

#computing the Chi Squared function and printing the function
vals = []
for i in range(len(exp)):
    val = (obs[i] - exp[i]) ** 2 / variance
    vals.append(val)
chi2 = sum(vals)
red_chi2 = chi2 / (len(y_old) - 1)
print(chi2)
print(red_chi2)

#ploting the first spectral atlas interpolated data against the interpolated mystery star data within the visible wavelength range
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(111)
plt.xlim(3500, 7500)
plt.title('Interpolated Data: Spectra4 vs. Spectra16')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")
axes.plot(x_old, y_new - 0.4, label="Interpolated Spectra 4 Data (M0 V-Type Star)")
axes.plot(x_old, Spectra16[:, 1] / np.max(Spectra16[:, 1]), label="Mystery Star 12")
axes.plot(6000, 0, label="Reduced Chi Squared Value = 0.0121638", color="white")
axes.legend()
#defining the wavelengths of my mystery star to interpolate that data
x_old = Spectra16[:, 0]
#the wavelength and flux values for the spectral atlas data
x_grid = Spectra5[:, 0]
y_grid = Spectra5[:, 1]
y_new = np.interp(x_old, x_grid, y_grid)
#creating the arrays for the new interpolated plot
xnew = np.array(Spectra16)[:, 0]
ynew = np.array(y_new)
#inputting parameters for the new mystery plot
wopt = np.where((Spectra16[:, 0] > 3500) & (Spectra16[:, 0] < 7500))
x_old = Spectra16[:, 0]
y_old = Spectra16[:, 1]
x_list = x_old[wopt]
y_list = y_old[wopt]
slope, intercept = np.polyfit(x_list, y_list, 1)
ynorm = y_list / (slope * x_list + intercept)
variance = np.std(ynorm)
obs = Spectra16[:, 1] / np.max(Spectra16[:, 1])
exp = ynew

#computing the Chi Squared function and printing the function
vals = []
for i in range(len(exp)):
    val = (obs[i] - exp[i]) ** 2 / variance
    vals.append(val)
chi2 = sum(vals)
red_chi2 = chi2 / (len(y_old) - 1)
print(chi2)
print(red_chi2)

#ploting the first spectral atlas interpolated data against the interpolated mystery star data within the visible wavelength range
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(111)
plt.xlim(3500, 7500)
plt.title('Interpolated Data: Spectra5 vs. Spectra16')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")
axes.plot(x_old, y_new - 0.4, label="Interpolated Spectra 5 Data (B3 V-Type Star)")
axes.plot(x_old, Spectra16[:, 1] / np.max(Spectra16[:, 1]), label="Mystery Star 12")
axes.plot(6000, 0, label="Reduced Chi Squared Value = 0.0293842", color="white")
axes.legend()
#defining the wavelengths of my mystery star to interpolate that data
x_old = Spectra16[:, 0]
#the wavelength and flux values for the spectral atlas data
x_grid = Spectra6[:, 0]
y_grid = Spectra6[:, 1]
y_new = np.interp(x_old, x_grid, y_grid)
#creating the arrays for the new interpolated plot
xnew = np.array(Spectra16)[:, 0]
ynew = np.array(y_new)
#inputting parameters for the new mystery plot
wopt = np.where((Spectra16[:, 0] > 3500) & (Spectra16[:, 0] < 7500))
x_old = Spectra16[:, 0]
y_old = Spectra16[:, 1]
x_list = x_old[wopt]
y_list = y_old[wopt]
slope, intercept = np.polyfit(x_list, y_list, 1)
ynorm = y_list / (slope * x_list + intercept)
variance = np.std(ynorm)
obs = Spectra16[:, 1] / np.max(Spectra16[:, 1])
exp = ynew

#computing the Chi Squared function and printing the function
vals = []
for i in range(len(exp)):
    val = (obs[i] - exp[i]) ** 2 / variance
    vals.append(val)
chi2 = sum(vals)
red_chi2 = chi2 / (len(y_old) - 1)
print(chi2)
print(red_chi2)

#ploting the first spectral atlas interpolated data against the interpolated mystery star data within the visible wavelength range
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(111)
plt.xlim(3500, 7500)
plt.title('Interpolated Data: Spectra6 vs. Spectra16')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")
axes.plot(x_old, y_new - 0.4, label="Interpolated Spectra 6 Data (09 V-Type Star)")
axes.plot(x_old, Spectra16[:, 1] / np.max(Spectra16[:, 1]), label="Mystery Star 12")
axes.plot(6000, 0, label="Reduced Chi Squared Value = 0.0619823", color="white")
axes.legend()
#defining the wavelengths of my mystery star to interpolate that data
x_old = Spectra16[:, 0]
#the wavelength and flux values for the spectral atlas data
x_grid = Spectra7[:, 0]
y_grid = Spectra7[:, 1]
y_new = np.interp(x_old, x_grid, y_grid)
#creating the arrays for the new interpolated plot
xnew = np.array(Spectra16)[:, 0]
ynew = np.array(y_new)
#inputting parameters for the new mystery plot
wopt = np.where((Spectra16[:, 0] > 3500) & (Spectra16[:, 0] < 7500))
x_old = Spectra16[:, 0]
y_old = Spectra16[:, 1]
x_list = x_old[wopt]
y_list = y_old[wopt]
slope, intercept = np.polyfit(x_list, y_list, 1)
ynorm = y_list / (slope * x_list + intercept)
variance = np.std(ynorm)
obs = Spectra16[:, 1] / np.max(Spectra16[:, 1])
exp = ynew

#computing the Chi Squared function and printing the function
vals = []
for i in range(len(exp)):
    val = (obs[i] - exp[i]) ** 2 / variance
    vals.append(val)
chi2 = sum(vals)
red_chi2 = chi2 / (len(y_old) - 1)
print(chi2)
print(red_chi2)

#ploting the first spectral atlas interpolated data against the interpolated mystery star data within the visible wavelength range
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(111)
plt.xlim(3500, 7500)
plt.title('Interpolated Data: Spectra7 vs. Spectra16')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")
axes.plot(x_old, y_new - 0.4, label="Interpolated Spectra 7 Data (K5 V-Type Star)")
axes.plot(x_old, Spectra16[:, 1] / np.max(Spectra16[:, 1]), label="Mystery Star 12")
axes.plot(6000, 0, label="Reduced Chi Squared Value = 0.0077991", color="white")
axes.legend()
#defining the wavelengths of my mystery star to interpolate that data
x_old = Spectra16[:, 0]
#the wavelength and flux values for the spectral atlas data
x_grid = Spectra8[:, 0]
y_grid = Spectra8[:, 1]
y_new = np.interp(x_old, x_grid, y_grid)
#creating the arrays for the new interpolated plot
xnew = np.array(Spectra16)[:, 0]
ynew = np.array(y_new)
#inputting parameters for the new mystery plot
wopt = np.where((Spectra16[:, 0] > 3500) & (Spectra16[:, 0] < 7500))
x_old = Spectra16[:, 0]
y_old = Spectra16[:, 1]
x_list = x_old[wopt]
y_list = y_old[wopt]
slope, intercept = np.polyfit(x_list, y_list, 1)
ynorm = y_list / (slope * x_list + intercept)
variance = np.std(ynorm)
obs = Spectra16[:, 1] / np.max(Spectra16[:, 1])
exp = ynew

#computing the Chi Squared function and printing the function
vals = []
for i in range(len(exp)):
    val = (obs[i] - exp[i]) ** 2 / variance
    vals.append(val)
chi2 = sum(vals)
red_chi2 = chi2 / (len(y_old) - 1)
print(chi2)
print(red_chi2)

#ploting the first spectral atlas interpolated data against the interpolated mystery star data within the visible wavelength range
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(111)
plt.xlim(3500, 7500)
plt.title('Interpolated Data: Spectra8 vs. Spectra16')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")
axes.plot(x_old, y_new - 0.4, label="Interpolated Spectra 8 Data (F8 V-Type Star)")
axes.plot(x_old, Spectra16[:, 1] / np.max(Spectra16[:, 1]), label="Mystery Star 12")
axes.plot(6000, 0, label="Reduced Chi Squared Value = 0.0070148", color="white")
axes.legend()
#defining the wavelengths of my mystery star to interpolate that data
x_old = Spectra16[:, 0]
#the wavelength and flux values for the spectral atlas data
x_grid = Spectra9[:, 0]
y_grid = Spectra9[:, 1]
y_new = np.interp(x_old, x_grid, y_grid)
#creating the arrays for the new interpolated plot
xnew = np.array(Spectra16)[:, 0]
ynew = np.array(y_new)
#inputting parameters for the new mystery plot
wopt = np.where((Spectra16[:, 0] > 3500) & (Spectra16[:, 0] < 7500))
x_old = Spectra16[:, 0]
y_old = Spectra16[:, 1]
x_list = x_old[wopt]
y_list = y_old[wopt]
slope, intercept = np.polyfit(x_list, y_list, 1)
ynorm = y_list / (slope * x_list + intercept)
variance = np.std(ynorm)
obs = Spectra16[:, 1] / np.max(Spectra16[:, 1])
exp = ynew

#computing the Chi Squared function and printing the function
vals = []
for i in range(len(exp)):
    val = (obs[i] - exp[i]) ** 2 / variance
    vals.append(val)
chi2 = sum(vals)
red_chi2 = chi2 / (len(y_old) - 1)
print(chi2)
print(red_chi2)

#ploting the first spectral atlas interpolated data against the interpolated mystery star data within the visible wavelength range
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(111)
plt.xlim(3500, 7500)
plt.ylim(-0.5, 15)
plt.title('Interpolated Data: Spectra9 vs. Spectra16')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")
axes.plot(x_old, y_new - 0.4, label="Interpolated Spectra 9 Data (M6 V-Type Star)")
axes.plot(x_old, Spectra16[:, 1] / np.max(Spectra16[:, 1]), label="Mystery Star 12")
axes.plot(6000, 0, label="Reduced Chi Squared Value = 2.2311318", color="white")
axes.legend()
#defining the wavelengths of my mystery star to interpolate that data
x_old = Spectra16[:, 0]
#the wavelength and flux values for the spectral atlas data
x_grid = Spectra10[:, 0]
y_grid = Spectra10[:, 1]
y_new = np.interp(x_old, x_grid, y_grid)
#creating the arrays for the new interpolated plot
xnew = np.array(Spectra16)[:, 0]
ynew = np.array(y_new)
#inputting parameters for the new mystery plot
wopt = np.where((Spectra16[:, 0] > 3500) & (Spectra16[:, 0] < 7500))
x_old = Spectra16[:, 0]
y_old = Spectra16[:, 1]
x_list = x_old[wopt]
y_list = y_old[wopt]
slope, intercept = np.polyfit(x_list, y_list, 1)
ynorm = y_list / (slope * x_list + intercept)
variance = np.std(ynorm)
obs = Spectra16[:, 1] / np.max(Spectra16[:, 1])
exp = ynew

#computing the Chi Squared function and printing the function
vals = []
for i in range(len(exp)):
    val = (obs[i] - exp[i]) ** 2 / variance
    vals.append(val)
chi2 = sum(vals)
red_chi2 = chi2 / (len(y_old) - 1)
print(chi2)
print(red_chi2)

#ploting the first spectral atlas interpolated data against the interpolated mystery star data within the visible wavelength range
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(111)
plt.xlim(3500, 7500)
plt.title('Interpolated Data: Spectra10 vs. Spectra16')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")
axes.plot(x_old, y_new - 0.4, label="Interpolated Spectra 10 Data (B9 V-Type Star)")
axes.plot(x_old, Spectra16[:, 1] / np.max(Spectra16[:, 1]), label="Mystery Star 12")
axes.plot(6000, 0, label="Reduced Chi Squared Value = 0.0155356", color="white")
axes.legend()
#defining the wavelengths of my mystery star to interpolate that data
x_old = Spectra16[:, 0]
#the wavelength and flux values for the spectral atlas data
x_grid = Spectra11[:, 0]
y_grid = Spectra11[:, 1]
y_new = np.interp(x_old, x_grid, y_grid)
#creating the arrays for the new interpolated plot
xnew = np.array(Spectra16)[:, 0]
ynew = np.array(y_new)
#inputting parameters for the new mystery plot
wopt = np.where((Spectra16[:, 0] > 3500) & (Spectra16[:, 0] < 7500))
x_old = Spectra16[:, 0]
y_old = Spectra16[:, 1]
x_list = x_old[wopt]
y_list = y_old[wopt]
slope, intercept = np.polyfit(x_list, y_list, 1)
ynorm = y_list / (slope * x_list + intercept)
variance = np.std(ynorm)
obs = Spectra16[:, 1] / np.max(Spectra16[:, 1])
exp = ynew

#computing the Chi Squared function and printing the function
vals = []
for i in range(len(exp)):
    val = (obs[i] - exp[i]) ** 2 / variance
    vals.append(val)
chi2 = sum(vals)
red_chi2 = chi2 / (len(y_old) - 1)
print(chi2)
print(red_chi2)

#ploting the first spectral atlas interpolated data against the interpolated mystery star data within the visible wavelength range
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(111)
plt.xlim(3500, 7500)
plt.title('Interpolated Data: Spectra11 vs. Spectra16')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")
axes.plot(x_old, y_new - 0.4, label="Interpolated Spectra 11 Data (A0 V-Type Star)")
axes.plot(x_old, Spectra16[:, 1] / np.max(Spectra16[:, 1]), label="Mystery Star 12")
axes.plot(6000, 0, label="Reduced Chi Squared Value = 0.0133243", color="white")
axes.legend()
#defining the wavelengths of my mystery star to interpolate that data
x_old = Spectra16[:, 0]
#the wavelength and flux values for the spectral atlas data
x_grid = Spectra12[:, 0]
y_grid = Spectra12[:, 1]
y_new = np.interp(x_old, x_grid, y_grid)
#creating the arrays for the new interpolated plot
xnew = np.array(Spectra16)[:, 0]
ynew = np.array(y_new)
#inputting parameters for the new mystery plot
wopt = np.where((Spectra16[:, 0] > 3500) & (Spectra16[:, 0] < 7500))
x_old = Spectra16[:, 0]
y_old = Spectra16[:, 1]
x_list = x_old[wopt]
y_list = y_old[wopt]
slope, intercept = np.polyfit(x_list, y_list, 1)
ynorm = y_list / (slope * x_list + intercept)
variance = np.std(ynorm)
obs = Spectra16[:, 1] / np.max(Spectra16[:, 1])
exp = ynew

#computing the Chi Squared function and printing the function
vals = []
for i in range(len(exp)):
    val = (obs[i] - exp[i]) ** 2 / variance
    vals.append(val)
chi2 = sum(vals)
red_chi2 = chi2 / (len(y_old) - 1)
print(chi2)
print(red_chi2)

#ploting the first spectral atlas interpolated data against the interpolated mystery star data within the visible wavelength range
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(111)
plt.xlim(3500, 7500)
plt.title('Interpolated Data: Spectra12 vs. Spectra16')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")
axes.plot(x_old, y_new - 0.4, label="Interpolated Spectra 12 Data (05 V-Type Star)")
axes.plot(x_old, Spectra16[:, 1] / np.max(Spectra16[:, 1]), label="Mystery Star 12")
axes.plot(6000, 0, label="Reduced Chi Squared Value = 0.0707363", color="white")
axes.legend()
#defining the wavelengths of my mystery star to interpolate that data
x_old = Spectra16[:, 0]
#the wavelength and flux values for the spectral atlas data
x_grid = Spectra13[:, 0]
y_grid = Spectra13[:, 1]
y_new = np.interp(x_old, x_grid, y_grid)
#creating the arrays for the new interpolated plot
xnew = np.array(Spectra16)[:, 0]
ynew = np.array(y_new)
#inputting parameters for the new mystery plot
wopt = np.where((Spectra16[:, 0] > 3500) & (Spectra16[:, 0] < 7500))
x_old = Spectra16[:, 0]
y_old = Spectra16[:, 1]
x_list = x_old[wopt]
y_list = y_old[wopt]
slope, intercept = np.polyfit(x_list, y_list, 1)
ynorm = y_list / (slope * x_list + intercept)
variance = np.std(ynorm)
obs = Spectra16[:, 1] / np.max(Spectra16[:, 1])
exp = ynew

#computing the Chi Squared function and printing the function
vals = []
for i in range(len(exp)):
    val = (obs[i] - exp[i]) ** 2 / variance
    vals.append(val)
chi2 = sum(vals)
red_chi2 = chi2 / (len(y_old) - 1)
print(chi2)
print(red_chi2)

#ploting the first spectral atlas interpolated data against the interpolated mystery star data within the visible wavelength range
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(111)
plt.xlim(3500, 7500)
plt.title('Interpolated Data: Spectra13 vs. Spectra16')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")
axes.plot(x_old, y_new - 0.4, label="Interpolated Spectra 13 Data (A5 V-Type Star)")
axes.plot(x_old, Spectra16[:, 1] / np.max(Spectra16[:, 1]), label="Mystery Star 12")
axes.plot(6000, 0, label="Reduced Chi Squared Value = 0.0104866", color="white")
axes.legend()
#defining the wavelengths of my mystery star to interpolate that data
x_old = Spectra16[:, 0]
#the wavelength and flux values for the spectral atlas data
x_grid = Spectra14[:, 0]
y_grid = Spectra14[:, 1]
y_new = np.interp(x_old, x_grid, y_grid)
#creating the arrays for the new interpolated plot
xnew = np.array(Spectra16)[:, 0]
ynew = np.array(y_new)
#inputting parameters for the new mystery plot
wopt = np.where((Spectra16[:, 0] > 3500) & (Spectra16[:, 0] < 7500))
x_old = Spectra16[:, 0]
y_old = Spectra16[:, 1]
x_list = x_old[wopt]
y_list = y_old[wopt]
slope, intercept = np.polyfit(x_list, y_list, 1)
ynorm = y_list / (slope * x_list + intercept)
variance = np.std(ynorm)
obs = Spectra16[:, 1] / np.max(Spectra16[:, 1])
exp = ynew

#computing the Chi Squared function and printing the function
vals = []
for i in range(len(exp)):
    val = (obs[i] - exp[i]) ** 2 / variance
    vals.append(val)
chi2 = sum(vals)
red_chi2 = chi2 / (len(y_old) - 1)
print(chi2)
print(red_chi2)

#ploting the first spectral atlas interpolated data against the interpolated mystery star data within the visible wavelength range
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(111)
plt.xlim(3500, 7500)
plt.title('Interpolated Data: Spectra14 vs. Spectra16')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")
axes.plot(x_old, y_new - 0.4, label="Interpolated Spectra 14 Data (WN5 V-Type Star)")
axes.plot(x_old, Spectra16[:, 1] / np.max(Spectra16[:, 1]), label="Mystery Star 12")
axes.plot(6000, 0, label="Reduced Chi Squared Value = 21366.44", color="white")
axes.legend()
#defining the wavelengths of my mystery star to interpolate that data
x_old = Spectra16[:, 0]
#the wavelength and flux values for the spectral atlas data
x_grid = Spectra15[:, 0]
y_grid = Spectra15[:, 1]
y_new = np.interp(x_old, x_grid, y_grid)
#creating the arrays for the new interpolated plot
xnew = np.array(Spectra16)[:, 0]
ynew = np.array(y_new)
#inputting parameters for the new mystery plot
wopt = np.where((Spectra16[:, 0] > 3500) & (Spectra16[:, 0] < 7500))
x_old = Spectra16[:, 0]
y_old = Spectra16[:, 1]
x_list = x_old[wopt]
y_list = y_old[wopt]
slope, intercept = np.polyfit(x_list, y_list, 1)
ynorm = y_list / (slope * x_list + intercept)
variance = np.std(ynorm)
obs = Spectra16[:, 1] / np.max(Spectra16[:, 1])
exp = ynew

#computing the Chi Squared function and printing the function
vals = []
for i in range(len(exp)):
    val = (obs[i] - exp[i]) ** 2 / variance
    vals.append(val)
chi2 = sum(vals)
red_chi2 = chi2 / (len(y_old) - 1)
print(chi2)
print(red_chi2)

#ploting the first spectral atlas interpolated data against the interpolated mystery star data within the visible wavelength range
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(111)
plt.xlim(3500, 7500)
plt.ylim(-0.5, 1)
plt.title('Interpolated Data: Spectra15 vs. Spectra16')
plt.xlabel("Wavelength (Å)")
plt.ylabel("Normalized Flux (mW/m^2/Å)")
axes.plot(x_old, y_new - 0.4, label="Interpolated Spectra 15 Data (L5-Type Star)")
axes.plot(x_old, Spectra16[:, 1] / np.max(Spectra16[:, 1]), label="Mystery Star 12")
axes.plot(6000, 0, label="Reduced Chi Squared Value = 0.0306634", color="white")
axes.legend()

data = [
    ['F2 (V-Type)', 54.555431090807566, 0.008143817150441494],
    ['G8 (V-Type)', 41.71608857188808, 0.006227211310925225],
    ['G2 (V-Type)', 44.925947104578015, 0.006706366189666818],
    ['M0 (V-Type)', 81.48587945420759, 0.01216388706586171],
    ['B3 (V-Type)', 196.84510144298085, 0.02938425159620553],
    ['O9 (V-Type)', 415.21949484902893, 0.061982310023739204],
    ['K5 (V-Type)', 52.246334346889235, 0.0077991243986996915],
    ['F8 (V-Type)', 46.992450265891975, 0.007014845539019552],
    ['M6 (V-Type)', 14946.352219096643, 2.2311318434238907],
    ['B9 (V-Type)', 104.07355107931133, 0.015535684591627307],
    ['A0 (V-Type)', 89.25961059653973, 0.013324318644057281],
    ['O5 (V-Type)', 473.862693686076, 0.07073633283864397],
    ['A5 (V-Type)', 70.24999517021132, 0.010486639076013035],
    ['WN5 (V-Type)', 143133820.36522728, 21366.44579268955],
    ['L5-Type', 205.41446699639673, 0.03066345230577649],
]
#displaying the table
print(
    tabulate(
        data,
        headers=[
            'Spectral Type',
            'Chi Squared Value with Respect to Mystery Star',
            'Reduced Chi Squared Value with Respect to Mystery Star',
        ],
        tablefmt='grid',
))


import sys

sys.path.append('/content/drive/MyDrive/Colab Notebooks')

from mesa_web import read_history, read_profile

#creating a variable for the history file data as the history file provides general information about the entire stellar model as a function of time
history_file = read_history('/content/drive/MyDrive/Colab Notebooks/trimmed_history.data')

#obtaining the information that will be used later from the history file
historyLum = history_file['log_L']
historyTeff = history_file['log_Teff']
historyRadius = history_file['log_R']
historyStarAge = history_file['star_age']
historyStarMass = history_file['star_mass']
historyCenterTemp = history_file['log_center_T']
historyNuclearTimescale = history_file['nuc_timescale']
historyPPcycle = history_file['pp']
historyCNOcycle = history_file['cno']

#creating variables for each profile as the profiles contain information about the internal structure of the stellar model at a single timestep
profile1_file = read_profile('/content/drive/MyDrive/Colab Notebooks/profile1.data')
profile2_file = read_profile('/content/drive/MyDrive/Colab Notebooks/profile2.data')
profile3_file = read_profile('/content/drive/MyDrive/Colab Notebooks/profile3.data')
profile4_file = read_profile('/content/drive/MyDrive/Colab Notebooks/profile4.data')
profile5_file = read_profile('/content/drive/MyDrive/Colab Notebooks/profile5.data')
profile6_file = read_profile('/content/drive/MyDrive/Colab Notebooks/profile6.data')
#reading in the track files to form the ZAMS line
file = '/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track1.25].tsv'
Track1 = np.loadtxt(file, skiprows=49)
file = '/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track85]asu.tsv'
Track2 = np.loadtxt(file, skiprows=49)
file = '/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track0.8]asu.tsv'
Track3 = np.loadtxt(file, skiprows=49)
file = '/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track0.9]asu.tsv'
Track4 = np.loadtxt(file, skiprows=49)
file = '/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track1]asu.tsv'
Track5 = np.loadtxt(file, skiprows=49)
file = '/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track1.1]asu.tsv'
Track6 = np.loadtxt(file, skiprows=49)
file = '/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track1.35]asu.tsv'
Track7 = np.loadtxt(file, skiprows=49)
file = '/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track1.5]asu.tsv'
Track8 = np.loadtxt(file, skiprows=49)
file = '/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track3]asu.tsv'
Track9 = np.loadtxt(file, skiprows=49)
file = '/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track4]asu.tsv'
Track10 = np.loadtxt(file, skiprows=49)
file = '/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track7]asu.tsv'
Track11 = np.loadtxt(file, skiprows=49)
file = '/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track20]asu.tsv'
Track12 = np.loadtxt(file, skiprows=49)
file = '/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track25]asu.tsv'
Track13 = np.loadtxt(file, skiprows=49)
file = '/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track32]asu.tsv'
Track14 = np.loadtxt(file, skiprows=49)
file = '/content/drive/MyDrive/Colab Notebooks/AA401 HR-Diagram Data/[Track120]asu.tsv'
Track15 = np.loadtxt(file, skiprows=49)
#the files above are all tracks, the first two are the ones I analyzed on my HR diagram (the first one being a mass of 1.25M_sun and the second one having a mass of 85M_sun)

fig = plt.figure(figsize=(8, 8))
axes = fig.add_subplot(111)

#below I put an x limit to invert the x-axis because otherwise the graph was backwards
plt.xlim(4, 3.2)
#putting a y limit to zoom in on my star
plt.ylim(-1.5, 1)

#below I am formulating the arrays for the ZAMS
x = (
    Track3[1, 1],
    Track4[1, 1],
    Track5[1, 1],
    Track6[1, 1],
    Track1[1, 1],
    Track7[1, 1],
    Track8[1, 1],
    Track9[1, 1],
    Track10[1, 1],
    Track11[1, 1],
    Track12[1, 1],
    Track13[1, 1],
    Track14[1, 1],
    Track2[1, 1],
    Track15[1, 1],
)

y = (
    Track3[1, 0],
    Track4[1, 0],
    Track5[1, 0],
    Track6[1, 0],
    Track1[1, 0],
    Track7[1, 0],
    Track8[1, 0],
    Track9[1, 0],
    Track10[1, 0],
    Track11[1, 0],
    Track12[1, 0],
    Track13[1, 0],
    Track14[1, 0],
    Track2[1, 0],
    Track15[1, 0],
)

#below is plotting the ZAMS
axes.plot(x, y, 'r', label='ZAMS')

#plotting the track of my star
axes.plot(historyTeff, historyLum, label='HD 18191', color='purple')

#below are the parameters and graph/axes titles
plt.title('HR Diagram')
plt.xlabel('Temperature [K]')
plt.ylabel('Luminosity [J/s]')
plt.legend()
#The code above will insert a legend on the plot labelling each one by their different temperatures

if len(historyLum) > 0:
  average = sum(historyLum) / len(historyLum)
  print("The average is:", average)
else:
  print(NO_VALUES_TO_CALCULATE_THE_AVERAGE)

if len(historyTeff) > 0:
  average = sum(historyTeff) / len(historyTeff)
  print("The average is:", average)
else:
  print(NO_VALUES_TO_CALCULATE_THE_AVERAGE)

if len(historyRadius) > 0:
  average = sum(historyRadius) / len(historyRadius)
  print("The average is:", average)
else:
  print(NO_VALUES_TO_CALCULATE_THE_AVERAGE)

if len(historyStarAge) > 0:
  average = sum(historyStarAge) / len(historyStarAge)
  print("The average is:", average)
else:
  print(NO_VALUES_TO_CALCULATE_THE_AVERAGE)

if len(historyStarMass) > 0:
  average = sum(historyStarMass) / len(historyStarMass)
  print("The average is:", average)
else:
  print(NO_VALUES_TO_CALCULATE_THE_AVERAGE)

if len(historyCenterTemp) > 0:
  average = sum(historyCenterTemp) / len(historyCenterTemp)
  print("The average is:", average)
else:
  print(NO_VALUES_TO_CALCULATE_THE_AVERAGE)

if len(historyNuclearTimescale) > 0:
  average = sum(historyNuclearTimescale) / len(historyNuclearTimescale)
  print("The average is:", average)
else:
  print(NO_VALUES_TO_CALCULATE_THE_AVERAGE)

#plotting the logarthmic radius data versus the star age data to obtain the radii at different stages
fig = plt.figure(figsize=(12, 8))
axes = fig.add_subplot(111)
axes.plot(historyStarAge, historyRadius)
plt.title('The Radius of an M6 (V-Type) Star Over its Lifetime ')
plt.xlabel('Star Age [yrs]')
plt.ylabel('Logarithmic Radius [m]')
