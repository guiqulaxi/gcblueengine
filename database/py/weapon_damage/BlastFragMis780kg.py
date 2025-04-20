import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis780kg'
    dbObj.maxRange_m=6234.187988
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=105.894051
    dbObj.fragCharge_kg=381.803955
    dbObj.radCharge_kg=10.589405
    dbObj.fragMetal_kg=292.301971
    dbObj.fragFragment_kg=0.112337
    dbObj.fragSpread=0.300000
    return dbObj
