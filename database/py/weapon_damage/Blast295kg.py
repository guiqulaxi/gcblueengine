import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast295kg'
    dbObj.maxRange_m=83.130768
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=295.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=29.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
