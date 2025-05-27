### 5 Verification

 cases occur out near the edges of state-space, but most of the runs will be
“right down the middle”; using conventional MonteCarlo techniques, most of these runs are completely unnecessary. With
a Sequential-MonteCarlo configuration, a small number of runs can be executed, allowing for identification of problem
areas, and a focussing of the distribution on those areas of state-space, thereby reducing the overall number of runs while
adding complexity to the setup. While this model does not (at this time) provide a Sequential-MonteCarlo capability, the
organization of the model has been designed to support external tools seeking to sequentially modify the distributions being
applied to the dispersed variables, and generate new dispersion sets.

# 2 Requirements

1. The model shall provide common statistical distribution capabilities, including:
    1. Uniform distribution between specified values
        1. as a floating-point value
        1. as an integer value
    1. Normal distribution, specified by mean and standard deviation
    1. Truncated Normal Distribution, including
        1. symmetric and asymmetric truncations
        1. it shall be possible to specify truncations by:
            1. some number of standard deviations from the mean,
            1. a numerical difference from the mean, and
            1. an upper and lower limit
1. The model shall provide an extensible framework suitable for supporting other statistical distributions
1. The model shall provide the ability to assign a common value to all runs:
    1. This value could be a fixed, user-defined value
    1. This value could be a random assignment, generated once and then applied to all runs
