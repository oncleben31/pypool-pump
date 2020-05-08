# PyPoolPump

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**PyPoolPump** is a python module providing classes for computing the duration needed for a swimming pool filtering pump.
This module will provide methods to define the filtering daily schedule.

Each classes is an implementation of a different algorithm found when searching Internet to find best way to compute the filtering pump duration.

## Classes description

### Base class

`FilteringDuration()` class is the base class with no duration computation. It gather all the common code for each implementation.
You will find a way to add a percentage modifier on the duration computed and a way to construct the daily filtering schedule.

You should not call directly this class except if you want to implement a new algorithm.

### Dumb algorithm

`DumbFilteringDuration()` is child class with an implementation of the common known algorithm using only the water temperature as parameter:
> filtering duration (in hour) = water temperature (in °C) / 2.

Reference: the poster delivered with my swimming pool

### Basic algorithm

`BasicFilteringDuration()` is  child class with an implementation of the previous algorithm with some optimizations:

- No need to filter if water temperature below 10°C
- Between 10°C and 14°C we can reduce the duration (water temperature in °C / 3)
- Between 14°C and 30°C we use the standard rule (water temperature in °C / 2)
- Above 30°C continuous filtering.

Reference: To be completed

### Abacus based algorithm

`AbacusFilteringDuration()` is a child class with an implementation of a water temperature based abacus. I found this when searching potential existing module on Github.

Reference: this abacus is used in the [Jeedom pool addon](https://github.com/scadinot/pool) by @scadinot.

### Advanced algorithm

`PumpCaracteristicFilteringDuration()` is a child class with an implementation of an algorithm based on the pool dimension, the pump characteristics and the water temperature.

## Contribute

If you want to contribute to the development:

- Start by cloning this repository.
- Setup a virtual environment
- Install the python package in edition mode: `pip install -e .`
- Create a branch for your feature
- Test your change using `tox`
- Send a PR when ready.

## License

This software is under the MIT License.
