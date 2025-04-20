import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis300kg'
    dbObj.maxRange_m=4749.002441
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=47.798225
    dbObj.fragCharge_kg=142.134521
    dbObj.radCharge_kg=4.779822
    dbObj.fragMetal_kg=110.067261
    dbObj.fragFragment_kg=0.062824
    dbObj.fragSpread=0.300000
    return dbObj
