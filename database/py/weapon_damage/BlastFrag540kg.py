import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag540kg'
    dbObj.maxRange_m=3535.703125
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=194.244827
    dbObj.fragCharge_kg=167.503448
    dbObj.radCharge_kg=19.424482
    dbObj.fragMetal_kg=178.251724
    dbObj.fragFragment_kg=0.036171
    dbObj.fragSpread=0.300000
    return dbObj
