import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='NuclearUW-5kT'
    dbObj.maxRange_m=2000.000000
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=5500000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2500000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
