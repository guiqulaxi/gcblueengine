import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis97.5kg'
    dbObj.maxRange_m=3854.196045
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=18.237078
    dbObj.fragCharge_kg=44.391949
    dbObj.radCharge_kg=1.823708
    dbObj.fragMetal_kg=34.870975
    dbObj.fragFragment_kg=0.040642
    dbObj.fragSpread=0.300000
    return dbObj
