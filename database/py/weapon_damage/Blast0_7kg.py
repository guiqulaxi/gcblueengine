import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast0.7kg'
    dbObj.maxRange_m=11.110380
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.700000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.070000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
