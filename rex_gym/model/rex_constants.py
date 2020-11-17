import numpy as np

ARM_POSES = {
    'rest': np.array([
        -1.6, -1.6, 0.,
        0., 1.6, 0.
    ])
}

INIT_POSES = {
    'stand': np.array([
        0.17, 0.78, -1.04,
        -0.17, 0.78, -1.04,
        0.17, 0.78, -1.04,
        -0.17, 0.78, -1.04
    ]),
    'stand_ol': np.array([
        0.17, 0.78, -1.04,
        -0.17, 0.78, -1.04,
        0.17, 0.78, -1.04,
        -0.17, 0.78, -1.04
    ]),
    'gallop': np.array([
        0.15192765, -0.90412283, 1.48156545,
        -0.15192765, -0.90412283, 1.48156545,
        0.15192765, -0.90412283, 1.48156545,
        -0.15192765, -0.90412283, 1.48156545
    ]),
    'stand_low': np.array([
        -0.17, 1.88, -2.67,
        0.17, 1.88, -2.67,
        -0.17, 1.88, -2.67,
        0.17, 1.88, -2.67
    ]),
    'stand_high': np.array([
        0.17, 0.78, -1.04,
        -0.17, 0.78, -1.04,
        0.17, 0.78, -1.04,
        -0.17, 0.78, -1.04
    ]),
    'rest_position': np.array([
        -0.17, 1.88, -2.67,
        0.17, 1.88, -2.67,
        -0.17, 1.88, -2.67,
        0.17, 1.88, -2.67
    ])
}
