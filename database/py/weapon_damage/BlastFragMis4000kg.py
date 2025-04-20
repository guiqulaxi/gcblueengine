import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis4000kg'
    dbObj.maxRange_m=11420.455078
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=381.774261
    dbObj.fragCharge_kg=2065.483887
    dbObj.radCharge_kg=38.177425
    dbObj.fragMetal_kg=1552.741943
    dbObj.fragFragment_kg=0.428106
    dbObj.fragSpread=0.300000
    return dbObj
