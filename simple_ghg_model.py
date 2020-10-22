# with a simple greenhouse gas (ghg) model, we assume a simple atmosphere 
# where there sufficient conduction/convection allows a homogenous temperature

# \       /
#  \     /
# ##\######## Atmosphere
#    \  /\
# ____\/__\__ Ground

# Here we can consider two different energy balance systems for the planet:
# the atmosphere and the ground
# Radiation intensity is given by L=εσT^4, we use this to find the intensity
# of a blackbody given its temperature
# Incoming radiation from the sun is too energetic to be absorbed by the
# atmosphere, it is absorbed and re-emitted from the ground. The amount
# reflected can simply be expressed from the albedo α (thus 1-α gives reflected)
# L is intensity, power / area. Incident intensity only shines on the surface
# of one side of the planet. Outgoing intensity leaves in proportion to the
# surface area of the (spherical) planet

# In an energy balanced system, incoming energy = outgoing energy:
# Power In = Power Out
# We can look at each layer separately:
# εσTg^4 = 2εσTa^4    Atmosphere
# L(1-α) = εσTg^4     Ground

# While these can be solved algebraically (and easily). It's more intuitive to
# Consider the entire system using the outer edge of the atmostphere as the 
# boundary. The total energy in equals the total energy leaving and we have:
# L(1-α)(πR^2) = εσT^4 (4πR^2)     # Area included as described above
# L(1-α)/4 = εσT^4


### Specific Examples ###

# Temperature of the surface of the moon (at local noon)
# Assumptions: No atmosphere => no even mixing, can't use the surface area
# of a sphere, must look at a flat sheet

# Lin = Lout
# L(1-α) = εσTg^4
# Tg = (L(1-α)/(εσ))^.25
def temp_no_ghg(L,a,e=1):
    o = 5.67E-8 # Stefan-Boltzman Constant
    return (L*(1-a)/(e*o))**.25

L = 1350 # watts/m^2
Tm = temp_no_ghg(L, .33)
print("Temperature of the Moon (at noon):", Tm)
