import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen18kg'
    dbObj.maxRange_m=29.089380
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=12.600000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=1.800000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
