import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag170kg'
    dbObj.maxRange_m=2182.505859
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=61.073334
    dbObj.fragCharge_kg=52.784443
    dbObj.radCharge_kg=6.107334
    dbObj.fragMetal_kg=56.142223
    dbObj.fragFragment_kg=0.013815
    dbObj.fragSpread=0.300000
    return dbObj
