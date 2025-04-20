import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag860kg'
    dbObj.maxRange_m=4295.289062
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=309.433350
    dbObj.fragCharge_kg=266.711090
    dbObj.radCharge_kg=30.943335
    dbObj.fragMetal_kg=283.855560
    dbObj.fragFragment_kg=0.054088
    dbObj.fragSpread=0.300000
    return dbObj
