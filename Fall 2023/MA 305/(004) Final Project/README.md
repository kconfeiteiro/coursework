# MA-305 Final Project

The main object of this project is to pick a project from the [list of projects](https://drive.google.com/file/d/1uu50InrSzw6umkXOIvHz8SUAgQlYyXd0/view?usp=drive_link) and solve the problems (of that project) accordingly.

For this project, my partner [Antonio Cascio](https://www.linkedin.com/in/antonio-cascio
) and I have chose ***Project II: Root Finding using Newton’s Method***. Our project will be outlined in this `README.md` file.

## Project II: Root Finding using Newton’s Method
Write a function, `newton()`, to implement [Newton’s method](https://en.wikipedia.org/wiki/Newton%27s_method) for finding a root of a given function, $F(x)$;

$$
\begin{gather}
x_0=\text{ given};\quad x_{n+1}=x_n-\frac{F(x_n)}{F'(x_n)}; \\
n = 0,\space 1,\space 2,\space 3, \dots,\space N.
\end{gather}
$$

Where, a good way to decide convergence is to test both the relative change and the residual;

$$
\begin{gather}
\left|1-\frac{x_{n+1}}{x_n}\right| \lt \text{TOL}\text{\quad and \quad} \left|F(x_n)\right|\lt \text{TOL}
\end{gather}
$$

The main program should read in initial guess for the root $x_0$, and tolerance for testing convergence (these could also be set in the code, if you prefer).

Your program should output the input values ($x_0$ and $\epsilon$) at the beginning, then at each iteration print out: $n$, $x_n$, and $F(x_n)$.

Then, upon convergence, the number of iterations $n$, the root $x_n$ and the residual $|F(x_n)|$. The values of $F(x_n)$ and $F_0(x_n)$ may be computed in a function or two separate functions.

### Part (a)

Set $\text{TOL} = 10^{-12}$, and find the real root of the ***************Newton’s cubic***************, $x^3-2x-5=0$ (the only equation Newton ever bothered to solve with his method, in 1671!)

### Part (b)

In a building, two intersecting halls with widths $w_1=9$ and $w_2=7$ feet at the angle $\alpha = 125\deg$, as shown below:

![Alt text](<src/project 2 figure.png>)

Assuming a two-dimensional situation (i.e., ignoring the thickness of the board), what is the longest board that can negotiate the turn? $[$**Hints**: Express length of the board $l = l_1 + l_2$ in terms of the angle $\gamma$, then find the maximum of the function $l(\gamma)$ by solving the nonlinear equation $l'(\gamma) = 0$$]$.

### Part (c)

Commissioner Gordon has been found dead in his office. At 8:00 PM, the county coroner determined the core temperature of the corpse to be $90\degree\text{F}$   F. One hour later, the core temperature had dropped to $85\degree\text{F}$. Maintenance reported that the building’s air conditioning unit broke down at 4:00 PM. The temperature in the commissioner’s office was $68\degree\text{F}$ at that time.

The computerized climate control system recorded that the office temperature rose at a rate of $1\degree\text{F}$ per hour after the air conditioning stopped working. Captain Furillo believes that the infamous Doc B killed the commissioner. Doc B, however, claims that he has an alibi.

Lois Lane was interviewing him at the *Daily Planet Building*, just across the street from the commissioner’s office.

The receptionist at the *Daily Planet Building* checked Doc B into the building at 6:35 PM, and the interview tapes confirm that Doc B was occupied from 6:40 PM to 7:15 PM.

> ***Could Doc B have killed the commissioner?***
>

### Hints

Assume that the core temperature of the corpse was $98.6\degree\text{F}$ at the time of death and began
decreasing immediately obeying Newton’s Law of Cooling. Let $T(t)$ be the temperature $(\degree\text{F})$ of the corpse at time $t$ (in hours).

Set $t=0$ to correspond to 8:00 PM. Then use

$$
\begin{equation}
\frac{dT}{dt}=-k(T-72-t)\space \degree\text{F/s},
\end{equation}
$$

with the conditions

$$
\begin{gather}
T(0)=90\degree\text{F}\text{\quad and \quad} T(1)=85\degree\text{F}.
\end{gather}
$$

Now, to answer the question, you will need to determine the exact time of death. Meaning find $t$ such that $T(t)=98.6\degree\text{F}$.


## Project Checklist

- [x]  Create `main.py` and `helpers.py`
- [x]  Write (simple) function for Newton’s cubic (called `newtons_cubic()`)
- [ ]  Create configuration dictionary `CONFIG` for this project
- [ ]  Write a function `newton_raphson()`
- [ ]  Implement Newton's method for finding a root of a given function using
- [ ]  Set `TOL = 10^-12` and find the real root of Newton's cubic, $x^3 - 2x - 5 = 0$
- [ ]  Determine the longest board that can negotiate the turn in a building with intersecting halls
- [ ]  Determine if Doc B could have killed Commissioner Gordon based on temperature data and alibi
