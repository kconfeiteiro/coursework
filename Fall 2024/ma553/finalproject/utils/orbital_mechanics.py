import numexpr as ne
import numpy as np
from line_profiler import profile


def keplerian_to_cartesian(
    semi_major_axis,
    eccentricity,
    inclination,
    omega,
    argument_of_periapsis,
    M,
    gravitational_parameter=398600.4418,
    loop_range=100,
):
    # mu -> Gravitational parameter for Earth, km^3/s^2
    # solve Kepler's equation for E

    e = M
    for _ in range(loop_range):
        E = M + eccentricity * np.sin(e)
    # compute the true anomaly

    true_anomaly = 2 * np.arctan2(
        np.sqrt(1 + eccentricity) * np.sin(e / 2), np.sqrt(1 - eccentricity) * np.cos(e / 2)
    )

    # compute the distance

    orbital_distance = semi_major_axis * (1 - eccentricity * np.cos(e))

    # position in the orbital plane

    x_orb = orbital_distance * np.cos(true_anomaly)
    y_orb = orbital_distance * np.sin(true_anomaly)

    # velocity in the orbital plane

    vx_orb = -np.sqrt(
        gravitational_parameter / (semi_major_axis * (1 - eccentricity**2))
    ) * np.sin(e)
    vy_orb = (
        np.sqrt(gravitational_parameter / (semi_major_axis * (1 - eccentricity**2)))
        * np.sqrt(1 - eccentricity**2)
        * np.cos(e)
    )

    # rotation matrices

    r1 = np.array(  # TODO - can use numexpr
        [[np.cos(omega), -np.sin(omega), 0], [np.sin(omega), np.cos(omega), 0], [0, 0, 1]]
    )

    r2 = np.array(
        [  # TODO - can use numexpr
            [1, 0, 0],
            [0, np.cos(inclination), -np.sin(inclination)],
            [0, np.sin(inclination), np.cos(inclination)],
    ])
    r3 = np.array([
        [np.cos(argument_of_periapsis), -np.sin(argument_of_periapsis), 0],
        [np.sin(argument_of_periapsis), np.cos(argument_of_periapsis), 0],
        [0, 0, 1],
    ])

    R = r1 @ r2 @ r3  # NOTE - test if faster than numba, numexpr, or numpy

    # position and velocity in the inertial frame

    position_vector = R @ np.array([x_orb, y_orb, 0])
    velocity_vector = R @ np.array([vx_orb, vy_orb, 0])

    return position_vector, velocity_vector




def cartesian_to_keplerian(state_vector, gravitational_parameter=398600.4418):
    # unpack position and velocity vectors
    position_vector, velocity_vector = state_vector

    # compute specific angular momentum
    specific_angular_momentum = np.cross(position_vector, velocity_vector)
    specific_angular_momentum_magnitude = np.linalg.norm(specific_angular_momentum)

    # compute the eccentricity vector
    eccentricity_vector = (
        np.cross(velocity_vector, specific_angular_momentum) / gravitational_parameter
    ) - (position_vector / np.linalg.norm(position_vector))
    eccentricity = np.linalg.norm(eccentricity_vector)

    # compute the semi-major axis
    radius_magnitude = np.linalg.norm(position_vector)
    velocity_magnitude = np.linalg.norm(velocity_vector)
    semi_major_axis = 1 / (
        (2 / radius_magnitude) - (velocity_magnitude**2 / gravitational_parameter)
    )

    inclination = np.arccos(specific_angular_momentum[2] / specific_angular_momentum_magnitude)
    omega = np.arctan2(specific_angular_momentum[0], -specific_angular_momentum[1])
    argument_of_periapsis = np.arctan2(
        eccentricity_vector[2] / np.sin(inclination),
        eccentricity_vector[0] * np.cos(omega) + eccentricity_vector[1] * np.sin(omega),
    )

    true_anomaly = np.arctan2(
        np.dot(np.cross(eccentricity_vector, position_vector), specific_angular_momentum)
        / specific_angular_momentum_magnitude,
        np.dot(eccentricity_vector, position_vector),
    )

    e = 2 * np.arctan2(
        np.sqrt(1 - eccentricity) * np.tan(true_anomaly / 2), np.sqrt(1 + eccentricity)
    )

    mean_anomaly = e - eccentricity * np.sin(e)
    return semi_major_axis, eccentricity, inclination, omega, argument_of_periapsis, mean_anomaly


def acceleration(state, mu):
    r = state[:3]
    r_norm = np.linalg.norm(r)
    a = -mu * r / r_norm**3
    return np.hstack((state[3:], a))


def rk4_method(initial_state, time, dt=60, mu=398600.4418, t=0):
    state = np.array(initial_state)
    while t < time:
        k1 = dt * acceleration(state, mu)
        k2 = dt * acceleration(state + 0.5 * k1, mu)
        k3 = dt * acceleration(state + 0.5 * k2, mu)
        k4 = dt * acceleration(state + k3, mu)
        state += (k1 + 2 * k2 + 2 * k3 + k4) / 6

        t += dt

    return state[:3], state[3:]


def calculate_orbital_elements(
    semi_major_axis, eccentricity, inclination, omega, argument_of_periapsis, mean_anomaly
):
    # Solve Kepler's equation for E
    E = mean_anomaly
    for _ in range(100):  # Iterative solution
        E = mean_anomaly + eccentricity * np.sin(E)

    # Compute the true anomaly
    true_anomaly = ne.evaluate('2 * arctan2(sqrt(1 + eccentricity) * sin(E / 2), sqrt(1 - eccentricity) * cos(E / 2))')

    # Compute the distance
    orbital_distance = ne.evaluate('semi_major_axis * (1 - eccentricity * cos(E))')

    # Position in the orbital plane
    x_orb = ne.evaluate('orbital_distance * cos(true_anomaly)')
    y_orb = ne.evaluate('orbital_distance * sin(true_anomaly)')

    # Velocity in the orbital plane
    vx_orb = ne.evaluate('-sqrt(398600.4418 / (semi_major_axis * (1 - eccentricity**2))) * sin(E)')
    vy_orb = ne.evaluate('sqrt(398600.4418 / (semi_major_axis * (1 - eccentricity**2))) * sqrt(1 - eccentricity**2) * cos(E)')

    # Rotation matrices
    r1 = np.array([[np.cos(omega), -np.sin(omega), 0], [np.sin(omega), np.cos(omega), 0], [0, 0, 1]])
    r2 = np.array([[1, 0, 0], [0, np.cos(inclination), -np.sin(inclination)], [0, np.sin(inclination), np.cos(inclination)]])
    r3 = np.array([[np.cos(argument_of_periapsis), -np.sin(argument_of_periapsis), 0], [np.sin(argument_of_periapsis), np.cos(argument_of_periapsis), 0], [0, 0, 1]])

    R = r1 @ r2 @ r3

    # Position and velocity in the inertial frame
    position_vector = R @ np.array([x_orb, y_orb, 0])
    velocity_vector = R @ np.array([vx_orb, vy_orb, 0])

    return position_vector, velocity_vector
