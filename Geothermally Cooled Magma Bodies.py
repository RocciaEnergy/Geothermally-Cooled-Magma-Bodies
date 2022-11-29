# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:45:45 2022

@author: tamir
"""

from magmageotherm import*
##
## SET MODEL PARAMETERS
## 
Vi = 100*1.e9         # initial volume [m^3]
Ti = 800.+273         # initial temperature [K]
z = 4.5e3             # burial depth [m]
dz = 1.e3             # sill thickness [m]
Pi = z*9.81*2.7e3     # initial pressure [Pa]
Pc = 20.e6            # critical pressure, Jellinek 2003, could be as high as 40 MPa
                      # also uses Spieler 2004 fragmentation model
qfld = 1.2/(365.25*24*3600)*1.e3*0.02    # geothermal mass flux 
                      # (rainfall volume rate x density x infiltration) [kg/s]
Min = 100.            # magma influx rate [kg/s]
ks = 1.e-19           # shell permeability [m^2]
etar = 1.e20          # shell viscosity (elastic host rock) [Pa s]
gamma = 10.           # strength of geothermal circulation
Merupt = 1.e7         # mass flux rate during eruption [kg/s]
Ne_max = 10           # maximum number of eruptions to model
tmax = 6.e3*365.25*24*3600           # maximum simulation time [s]


##
## CREATE AND RUN THE MODEL
## 
model = MagmaChamber(Min=Min, Vi=Vi, z=z, Ti=Ti, Pc=Pc, Plith=Pi, qfld=qfld, 
                     ks=ks, dz=dz, etar=etar, gamma=gamma, Ne_max=Ne_max, Merupt= Merupt, tmax=tmax)
model.run()           


##
## SHOW THE MODEL OUTPUT
##
defaults = ['deltaP','V','eX','T','eg','egW']     # default to show, but can be changed interactively
show_model(model, defaults)