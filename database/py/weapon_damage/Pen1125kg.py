import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen1125kg'
    dbObj.maxRange_m=115.282272
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=787.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=112.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
