---

<aside>
<img src="/icons/link_gray.svg" alt="/icons/link_gray.svg" width="40px" /> **Content**

---

</aside>

---

# Assignment Outline

For this [portfolio assignment](https://colab.research.google.com/drive/1y8Uqn3rA-d7hWaACr7COO8_n5ZhMXVI2#scrollTo=T2JRGW8MInRf), create your own HR Diagram, similar to the one below:

![Alt text](References/hr_diagram.png)


To do this you will need to download data from the [Geneva Stellar Evolutionary code](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fwww.unige.ch%2Fsciences%2Fastro%2Fevolution%2Fen%2Fresearch%2Fgeneva-grids-stellar-evolution-models%2F%23grids92). This database provides a model grid of stellar parameters in different stages of a stars evolution.

The different models contain information for:

- Isochrones (**same age**, different masses)
- Evolutionary tracks (**one mass** over time)

## Relevant Python Libraries

Here we provide some of the libraries that need to be read in to be able to execute our code. Remember that:

1. **`numpy`:** A fundamental package of Python. It allows for a wide range of data types and data manipulation capabilities. To use it you will call it simply as `np`.
2. `matplotlib`: A Python 2D plotting library. We are only loading the `pyplot` capabilities, which provide a collection of command that make matplotlib work like MATLAB.
3. `%matplotlib notebook` allows for interactive plotting.

Include any other libraries that you may find useful.

## **Getting the Data**

For this assignment, we will use [Grids of Stellar Models with Rotation](https://www.unige.ch/sciences/astro/evolution/en/research/geneva-grids-stellar-evolution-models/#grids92), primarily using solar abundance models $(Z = 0.014)$.

You can download the tracks and isochrone grid on [VizieR](http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=J/A%2bA/537/A146&-out.max=50&-out.form=HTML%20Table&-out.add=_r&-out.add=_RAJ,_DEJ&-sort=_r&-oc.form=sexa).

To limit the output, you will need to specify:

- $Z = 0.014$ (and select it)
- Specify rotation models
- For isochrones: enter the age as $\log(t)$ in years. Example: for a $3\text{ Myr}$ isochrone, enter $6.5$
- For evolutionary tracks: enter the initial mass in solar masses
- Output the information in some plain text/ASCII friendly format (e.g. Tab separated, `;` separated, ascii text/plain) that will be downloaded. The default is an HTML table)

## **Assignment**

With this information, I would like you to create **one** H-R diagram with the following:

1. The ZAMS over the mass range provided $(0.8-120\text{ M}_\odot)$
2. Denote where the Sun is located on the H-R diagram
3. Isochrones over a sampling of the available ages (e.g. $\log (t) = \{6.5,\space 7.5,\space 8.5,\space 9.5,\space 10.1\text{ yr}\})$, showing how the Main Sequence changes over time.
4. Choose the evolutionary track of one star with $\text{M} \lt 8\text{M}_\odot$ and another with $\text{M} \gt 8\text{M}_\odot$, plot and label the tracks of these stars.
    1.  Some accepted values for masses are:
    $\text{M} = \{ 0.8,\space 0.9,\space 1,\space 1.1,\space 1.25,\space 1.35,\space 1.5,\space 3,\space 4,\space 7,\space 20,\space 25,\space 32,\space 85,\space 120\}$

Here is the [Jupyter Notebook (Google Colab)](https://drive.google.com/file/d/1WssGOFCsTnR66wHuPvpj1CHhfeKfyZWP/view?usp=sharing) to get you started. Make sure to include any references you use in creating this plot (e.g. solar values for luminosity and temperature).

## Grading Rubric

| Criteria | Points |
| --- | --- |
| ZAMS | 1 |
| Sun | 1 |
| Isochrones | 1 |
| Two evolutionary tracks | 2 |
| Label & legend | 1 |
| Legibility | 1 |
| Accuracy | 2 |
| Citations | 1 |
| Total Points: | 10 |

# Checklist

## Data Downloading

- [x]  Evolutionary tracks
    - [x] $\text{M}=0.8\text{ M}_\odot$
    - [x] $\text{M}=0.9\text{ M}_\odot$
    - [x] $\text{M}=1\text{ M}_\odot$
    - [x] $\text{M}=1.1\text{ M}_\odot$
    - [x] $\text{M}=1.25\text{ M}_\odot$
    - [x] $\text{M}=1.35\text{ M}_\odot$
    - [x] $\text{M}=1.5\text{ M}_\odot$
    - [x] $\text{M}=3\text{ M}_\odot$
    - [x] $\text{M}=4\text{ M}_\odot$
    - [x] $\text{M}=7\text{ M}_\odot$
    - [x] $\text{M}=20\text{ M}_\odot$
    - [x] $\text{M}=25\text{ M}_\odot$
    - [x] $\text{M}=32\text{ M}_\odot$
    - [x] $\text{M}=85\text{ M}_\odot$
    - [x] $\text{M}=120\text{ M}_\odot$
- [x]  Isochrones
    - [x] $\log(t)=6.5\text{ yr}$
    - [x] $\log(t)=7.5\text{ yr}$
    - [x] $\log(t)=8.5\text{ yr}$
    - [x] $\log(t)=9.5\text{ yr}$
    - [x] $\log(t)=10.1\text{ yr}$

## Coding

- [x] Download data for isochrones and tracks
- [x] Create one H-R diagram with the ZAMS over the mass range provided
- [x] Denote where the Sun is located on the H-R diagram
- [x] Plot isochrones over a sampling of the available ages
- [x] Choose the evolutionary track of one star with $M \lt 8M_\odot$ and another with $M \gt 8M_\odot$, plot and label the tracks of these stars
- [x] Include any references used in creating the plot

## Question Answers

- [x] <u>**Question 1**</u>: What information from the models do you need to build your ZAMS?
- [x] <u>**Question 2**</u>: What information about the Sun do you need to include it on your HR-Diagram? Provide your reference for this information.

---

# Open Response Questions

## Question 1

<u>**Prompt**</u>:

> *What information from the models do you need to build your ZAMS?*
>

<u>**My Response**</u>:

> To build the data form the zero-age main sequence stars (ZAMS), it requires the initial temperature, $T_\text{eff}$, and luminosity, $L$, where you will combine all of the data files into a single `pd.DataFrame()` object to then plot in the HR diagram.
>

## Question 2

<u>**Prompt**</u>:

> *What information about the Sun do you need to include it on your HR-Diagram? Provide your reference for this information.*
>

<u>**My Response**</u>:

> Including the Sun on the HR-Diagram requires the luminosity and effective temperature $(T_\text{eff}$ and $L)$ values, gathered from [NASA's official website](http://nasa.gov/). These will then be used to plot the single point in the HR diagram.
>

# Notes

- We are specifically **downloading 19 files** which *only* have columns for $\log(T_\text{eff})$ and $\log(g)$ (from [here](https://vizier.cds.unistra.fr/viz-bin/VizieR-3))

## Coding

### How to combine multiple `pd.DataFrame()` objects in [Python](https://www.notion.so/eabc50c375cc44b289823779f3ea50a8?pvs=21)

Using [this source](https://www.geeksforgeeks.org/how-to-combine-two-dataframe-in-python-pandas/), we start with

```python
# First DataFrame
df1 = pd.DataFrame(
    {"id": ["A01", "A02", "A03", "A04"], "Name": ["ABC", "PQR", "DEF", "GHI"]}
)

# Second DataFrame
df2 = pd.DataFrame(
    {"id": ["B05", "B06", "B07", "B08"], "Name": ["XYZ", "TUV", "MNO", "JKL"]}
)
```

when you combine the `pd.DataFrame()` objects into a single list then use the `pd.concat()` function to combine them into a single `pd.DataFrame()` object:

```python
result = pd.concat([df1, df2])
```

where `result` will print:

```
id    Name
0    A01    ABC
1    A02    PQR
2    A03    DEF
3    A04    GHI
0    B05    XYZ
1    B06    TUV
2    B07    MNO
3    B08    JKL
```

- *See* c*omplete code snippet*

    ```python
    # First DataFrame
    df1 = pd.DataFrame(
        {"id": ["A01", "A02", "A03", "A04"], "Name": ["ABC", "PQR", "DEF", "GHI"]}
    )

    # Second DataFrame
    df2 = pd.DataFrame(
        {"id": ["B05", "B06", "B07", "B08"], "Name": ["XYZ", "TUV", "MNO", "JKL"]}
    )

    result = pd.concat([df1, df2])
    ```


### How to remove selected rows in  `pd.DataFrame()` object in [Python](https://www.notion.so/eabc50c375cc44b289823779f3ea50a8?pvs=21)

Just use the `.iloc[]` method on the `pd.DataFrame()` object and index every column *except* the ones that you want to delete (it *is* ugly, *but* **it works**):

```python
DATA = pd.read_csv(file, **kwargs)
DATA = DATA.iloc[2:, :]
DATA = DATA.reset_index()
```

where we skip $2$ rows, specified in `[2:, :]`.

# Links/Sources

## Miscellaneous Sources

- [How to combine two dataframe in Python - Pandas? - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-combine-two-dataframe-in-python-pandas/)
- [pandas.DataFrame.drop — pandas 2.1.2 documentation (pydata.org)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)
- https://myerauedu-my.sharepoint.com/:x:/g/personal/confeitk_my_erau_edu/Ec2csS6yfyNEoG5d4QuaEGYB1y2cJeIfVCkHQ6IFFlk9xg?e=Ts6byk
- [Python | Delete rows/columns from DataFrame using Pandas.drop() - GeeksforGeeks](https://www.geeksforgeeks.org/python-delete-rows-columns-from-dataframe-using-pandas-drop/)
- [pandas.concat — pandas 2.1.2 documentation (pydata.org)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)
