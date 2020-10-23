# with a simple greenhouse gas (ghg) model, we assume a simple atmosphere 
# where there sufficient conduction/convection allows a homogenous temperature
print("""
 \       /
  \     /
 ##\######## Atmosphere
    \  /\ 
 ____\/__\__ Ground
""")
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

# NO ATMOSTPHERE (Moon):

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
print("no layer model\n")
print("Temperature of the Moon (at noon):", Tm)



print('\n2 layer model (stronger ghg effect):')
print("""
 Strong Atmosphere (2 layers)

 \          /
  \        /
 ##\################ Layer 2 (T2)
    \     /\ 
 ####\############## Layer 1 (T1)
      \  /\ 
 ______\/__\________ Ground

 L (1-α) / 4 = ε σ T2^4      Outer most layer
 Temperature outer layer:
 T2 = (L (1-α) / (4 ε σ))^.25
 """)
def temp_ghg(L,a,e=1):
    o = 5.67E-8
    return (L*(1-a) / (4*e*o))**.25

T2 = temp_ghg(L,.3) # Assuming albedo of 30%
print('outer layer temperature:',T2)

# Ratio of temperatures layer 1 to layer 2:
# ε σ T1^4 = 2 * ε σ T2^4
# T1/T2 = 2^.25
print("ratio of T1 to T2:", 2**.25)

# Ratio of Ground to Layer 2. Let's look at the energy balance of Layer 1:
# ε σ Tg^4 + ε σ T2^4 = 2 ε σ T1^4 
# divide through by T2^4
# (Tg/T2)^4 + 1 = 2 (T1/T2)^4
# above we found T1/T2, substituting:
# (Tg/T2)^4 + 1 = 2*2
# Tg/T2 = 3^.25
print("Ratio of Tg to T2:", 3**.25)

# Note how the hottest layers are on the inside, like a person wrapped in layers
# of a blanket with the heat source technically emanating from below 
# (as the atmosphere mostly doesn't attenuate the light incoming from space)


# Nuclear Winter (1 layer model with atmospheric aerosols) #
print("""Nuclear Winter Model
 \    / 
 ============ Dusty Atmosphere
     /\ 
 ___/__\_____ Ground


 L(1-α) + εσTg^4  = 2εσTa^4     # Dusty Atmosphere
 εσTa^4 = εσTg^4                # Ground
""")
# Clearly the Tground = Tatmosphere in this model
# In this model,  visible light is blocked, It's likely that L is reduced
# by around 40% (curosry google search shows that visible spectrum encompasses
# 40% of sunlight. IR and UV are 50% and 10% respectively
# Unsure of the analysis that follows
def temp_aerosols(L,a,e=1):
    o = 5.67E-8
    return (.6*L*(1-a)/(e*o))**.25 #.6 reduces the incoming solar energy to 60%

print(temp_aerosols(L,.3))


