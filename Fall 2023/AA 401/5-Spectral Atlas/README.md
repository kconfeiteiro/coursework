# Spectral Atlas

The goal of this portfolio assignment is to create a *Spectral Atlas* like the one displayed below:

![Alt text](<src/Example spectral atlas.png>)

using various tools like `numpy`, `matplotlib`, `pandas`, etc.


## Outline

> *For this exercise you will **create your own spectral atlas**, similar to the one attached (to the Notion page).*
>

**You will need to**:

- Plot the spectral models from early (O type) to late (M type) offset from each other
- Download the [spectra here](https://drive.google.com/drive/folders/1TrBuGH8CukEEQ9C8j9oyIEMmvHF2RyYr?usp=sharing) (Google Drive)
- For each file, read in the **first two column** (wavelength and flux)
- Normalize the spectra by dividing the maximum in the plotted region $[3500\space\AA,\space7000\space\AA]$
    - To offset the spectra, incrementally add `1` to your normalized flux
- Use [*Gray's Digital Spectral Atlas*](http://ned.ipac.caltech.edu/level5/Gray/Gray1.html) to sort the models
    - Plot hottest on top to coolest at the bottom
    - Also see *[An Atlas of Stellar Spectra](https://ned.ipac.caltech.edu/level5/ASS_Atlas/frames.html)*
- The model spectral classes are (use this to label the spectra accordingly):
    - O5V, O9V, B3V, B9V, A0V, A5V, F2V, F8V, G2V, G8V, K5V, M0V, M6V
- Denote certain significant features in the spectra listed in the lecture notes.
- Include a key (e.g. `spectra20.dat` $\to$ M8V) to your Atlas, assigning spectral type to all the different files you have read in

Submit your notebook on [Canvas](https://erau.instructure.com/courses/163207/assignments/3282016) (make sure you properly comment the code).
