import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag9.6kg'
    dbObj.maxRange_m=553.996155
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.400218
    dbObj.fragCharge_kg=3.013188
    dbObj.radCharge_kg=0.340022
    dbObj.fragMetal_kg=3.186594
    dbObj.fragFragment_kg=0.001261
    dbObj.fragSpread=0.300000
    return dbObj
