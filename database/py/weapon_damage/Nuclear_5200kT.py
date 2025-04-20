import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-5200kT'
    dbObj.maxRange_m=52102.792969
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=5720000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2600000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
