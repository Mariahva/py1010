"""

Arbeidskrav 1  - sammenlikne årlige kostnader ved elbil vs. bensinbil
Grunnleggende programmering med Python

Av Maria Helene Vinje Antonsen (maant4799@usn.no)

Oppdatert 2025 09 20

"""

#%% Utregning årlige kostnader ved bensinbil

FORSIKRING_BENSIN = 7500            #  [Forsikring bensinbil/år]
TRAFIKKFORSIKRING_BENSIN = 8.38*365 #  [Trafikkforsikringsavgift bensinbil/år] 
DRIVSTOFF_BENSIN = 1*10000          #  [Bensinutgifter/år] 
BOMAVGIFT_BENSIN = 0.3*10000        # [Bomavgift/år] 

TOTALT_BENSINBIL = FORSIKRING_BENSIN + TRAFIKKFORSIKRING_BENSIN + DRIVSTOFF_BENSIN + BOMAVGIFT_BENSIN #  [Totale årlige kostnader ved bensinbil]


#%% Utregning årlige kostnader ved elbil

FORSIKRING_EL = 5000            #  [Forikring elbil/år] 
TRAFIKKFORSIKRING_EL = 8.38*365 #  [Trafikkforsikringsavgift elbil/år] 
DRIVSTOFF_EL = (0.2*10000)*2    #  [Strømutgifter elbil/år] 
BOMAVGIFT_EL = 0.1*10000        #  (Bomavgift elbil/år)

TOTALT_ELBIL = FORSIKRING_EL + TRAFIKKFORSIKRING_EL + DRIVSTOFF_EL + BOMAVGIFT_EL #  [Totale årlige kostnader ved elbil] 


#%% Utregning årlig kostnadsdifferanse elbil vs. bensinbil

differanse = TOTALT_BENSINBIL - TOTALT_ELBIL


#%% Utskrift

print('Totale utgifter bensinbil =', TOTALT_BENSINBIL)
print('Totale utgifter elbil =', TOTALT_ELBIL)
print('Differanse =', differanse)










