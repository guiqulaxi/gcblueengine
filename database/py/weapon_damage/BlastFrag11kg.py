import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag11kg'
    dbObj.maxRange_m=595.366333
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.900861
    dbObj.fragCharge_kg=3.449426
    dbObj.radCharge_kg=0.390086
    dbObj.fragMetal_kg=3.649713
    dbObj.fragFragment_kg=0.001408
    dbObj.fragSpread=0.300000
    return dbObj
