import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen1825kg'
    dbObj.maxRange_m=135.434494
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1277.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=182.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
