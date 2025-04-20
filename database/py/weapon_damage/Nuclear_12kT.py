import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-12kT'
    dbObj.maxRange_m=8429.743164
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=13200000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=6000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
