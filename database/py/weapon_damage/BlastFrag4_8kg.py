import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag4.8kg'
    dbObj.maxRange_m=387.997223
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.689313
    dbObj.fragCharge_kg=1.513791
    dbObj.radCharge_kg=0.168931
    dbObj.fragMetal_kg=1.596896
    dbObj.fragFragment_kg=0.000750
    dbObj.fragSpread=0.300000
    return dbObj
