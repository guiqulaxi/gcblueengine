import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis2700kg'
    dbObj.maxRange_m=9958.749023
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=283.870422
    dbObj.fragCharge_kg=1376.753052
    dbObj.radCharge_kg=28.387041
    dbObj.fragMetal_kg=1039.376587
    dbObj.fragFragment_kg=0.314772
    dbObj.fragSpread=0.300000
    return dbObj
