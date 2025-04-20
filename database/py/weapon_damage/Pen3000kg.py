import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen3000kg'
    dbObj.maxRange_m=159.812271
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2100.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=300.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
