import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir600kg'
    dbObj.maxRange_m=5740.413086
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=85.339378
    dbObj.fragCharge_kg=291.107086
    dbObj.radCharge_kg=8.533938
    dbObj.fragMetal_kg=223.553543
    dbObj.fragFragment_kg=0.094049
    dbObj.fragSpread=0.300000
    return dbObj
