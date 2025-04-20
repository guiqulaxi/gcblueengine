import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3100kg'
    dbObj.maxRange_m=7154.515625
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1115.801758
    dbObj.fragCharge_kg=961.132202
    dbObj.radCharge_kg=111.580170
    dbObj.fragMetal_kg=1023.066101
    dbObj.fragFragment_kg=0.160657
    dbObj.fragSpread=0.300000
    return dbObj
