#!/usr/bin/env python3

# Temperature conversion functions
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp

def c_to_f(c_temp):
    f_temp = c_temp * 9 / 5 + 32
    return f_temp

# Force and energy calculation functions
def get_force(mass, acceleration):
    return mass * acceleration

def get_energy(mass, c=3*10**8):
    return mass * c**2

def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    work = force * distance
    return work

# Define variables
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

# Test temperature conversion functions
f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)

# Test force and energy calculation functions
train_force = get_force(train_mass, train_acceleration)
bomb_energy = get_energy(bomb_mass)

# Test work calculation function
train_work = get_work(train_mass, train_acceleration, train_distance)

# Print results
print(f"100 degrees Fahrenheit is {f100_in_celsius:.2f} degrees Celsius")
print(f"0 degrees Celsius is {c0_in_fahrenheit:.2f} degrees Fahrenheit")
print(f"The GE train supplies {train_force:.2f} Newtons of force.")
print(f"A 1kg bomb supplies {bomb_energy:.2f} Joules.")
print(f"The GE train does {train_work:.2f} Joules of work over {train_distance} meters.")

