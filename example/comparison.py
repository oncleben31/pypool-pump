#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os

try:
    os.chdir(os.path.join(os.getcwd(), "example"))
    print(os.getcwd())
except:
    pass
#%% [markdown]
# Initialisation

#%%
import sys
import matplotlib.pyplot as plt
import numpy as np

# Add local package in the path
sys.path.append("../src/")

#%% [markdown]
# Import the modelisation classes, set the temperature scale and create the instances.

#%%

from pypool_pump import (
    PumpCaracteristicFilteringDuration,
    AbacusFilteringDuration,
    BasicFilteringDuration,
    DumbFilteringDuration,
)


#%%
# Temperature is in °C
temperatures = np.arange(1, 35, 1)


#%%
pool_controler_caracteristics = PumpCaracteristicFilteringDuration(40, 21.9)
pool_controler_abacus = AbacusFilteringDuration()
pool_controler_basic = BasicFilteringDuration()
pool_contorler_dumb = DumbFilteringDuration()


#%%
# Durations are in hours.
durations_caracteristics = [
    pool_controler_caracteristics.duration(temperature) for temperature in temperatures
]
durations_abacus = [
    pool_controler_abacus.duration(temperature) for temperature in temperatures
]
durations_basic = [
    pool_controler_basic.duration(temperature) for temperature in temperatures
]
durations_dumb = [
    pool_contorler_dumb.duration(temperature) for temperature in temperatures
]


#%%
plt.plot(
    temperatures,
    durations_abacus,
    temperatures,
    durations_caracteristics,
    temperatures,
    durations_basic,
    temperatures,
    durations_dumb,
)
plt.xlabel("temperature (°C)")
plt.ylabel("duration (hours)")
plt.show()


#%%

