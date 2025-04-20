import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='1800 1lb bomblet'
    dbObj.maxRange_m=604.867859
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=277.779999
    dbObj.fragCharge_kg=269.609985
    dbObj.radCharge_kg=0.000000
    dbObj.fragMetal_kg=269.609985
    dbObj.fragFragment_kg=0.000340
    dbObj.fragSpread=1.000000
    return dbObj
