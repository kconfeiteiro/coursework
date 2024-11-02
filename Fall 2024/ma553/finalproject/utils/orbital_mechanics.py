import numpy as np

def keplerian_to_cartesian(a, e, i, omega, w, M, mu=398600.4418):
    # mu -> Gravitational parameter for Earth, km^3/s^2
    # Solve Kepler's equation for E
    E = M
    for _ in range(100):
        E = M + e * np.sin(E)

    # Compute the true anomaly
    nu = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))

    # Compute the distance
    r = a * (1 - e * np.cos(E))

    # Position in the orbital plane

    x_orb = r * np.cos(nu)
    y_orb = r * np.sin(nu)

    # Velocity in the orbital plane

    vx_orb = -np.sqrt(mu / (a * (1 - e**2))) * np.sin(E)
    vy_orb = np.sqrt(mu / (a * (1 - e**2))) * np.sqrt(1 - e**2) * np.cos(E)

    # Rotation matrices

    r1 = np.array(
        [[np.cos(omega), -np.sin(omega), 0], [np.sin(omega), np.cos(omega), 0], [0, 0, 1]]
    )

    r2 = np.array([[1, 0, 0], [0, np.cos(i), -np.sin(i)], [0, np.sin(i), np.cos(i)]])
    r3 = np.array([[np.cos(w), -np.sin(w), 0], [np.sin(w), np.cos(w), 0], [0, 0, 1]])

    R = r1 @ r2 @ r3

    # Position and velocity in the inertial frame

    r_vec = R @ np.array([x_orb, y_orb, 0])
    v_vec = R @ np.array([vx_orb, vy_orb, 0])

    return r_vec, v_vec


def cartesian_to_keplerian(state_vector):
    r_vec, v_vec = state_vector

    # Constants
    mu = 398600.4418  # Gravitational parameter for Earth, km^3/s^2

    # Compute specific angular momentum
    h_vec = np.cross(r_vec, v_vec)
    h = np.linalg.norm(h_vec)

    # Compute the eccentricity vector
    e_vec = (np.cross(v_vec, h_vec) / mu) - (r_vec / np.linalg.norm(r_vec))
    e = np.linalg.norm(e_vec)

    # Compute the semi-major axis
    r = np.linalg.norm(r_vec)
    v = np.linalg.norm(v_vec)
    a = 1 / ((2 / r) - (v**2 / mu))

    # Compute the inclination
    i = np.arccos(h_vec[2] / h)

    # Compute the longitude of the ascending node
    omega = np.arctan2(h_vec[0], -h_vec[1])

    # Compute the argument of periapsis
    w = np.arctan2(e_vec[2] / np.sin(i), e_vec[0] * np.cos(omega) + e_vec[1] * np.sin(omega))

    # Compute the true anomaly
    nu = np.arctan2(np.dot(np.cross(e_vec, r_vec), h_vec) / h, np.dot(e_vec, r_vec))

    # Compute the mean anomaly
    E = 2 * np.arctan2(np.sqrt(1 - e) * np.tan(nu / 2), np.sqrt(1 + e))
    m = E - e * np.sin(E)

    return a, e, i, omega, w, m

def propagate_orbit(initial_state, time, dt=60):
    def acceleration(state):
        r = state[:3]
        r_norm = np.linalg.norm(r)
        a = -mu * r / r_norm**3
        return np.hstack((state[3:], a))

    mu = 398600.4418  # Gravitational parameter for Earth, km^3/s^2
    state = np.array(initial_state)
    t = 0

    while t < time:
        k1 = dt * acceleration(state)
        k2 = dt * acceleration(state + 0.5 * k1)
        k3 = dt * acceleration(state + 0.5 * k2)
        k4 = dt * acceleration(state + k3)

        state += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += dt
    return state[:3], state[3:]
