import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag8.6kg'
    dbObj.maxRange_m=526.369995
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.042931
    dbObj.fragCharge_kg=2.701379
    dbObj.radCharge_kg=0.304293
    dbObj.fragMetal_kg=2.855690
    dbObj.fragFragment_kg=0.001167
    dbObj.fragSpread=0.300000
    return dbObj
