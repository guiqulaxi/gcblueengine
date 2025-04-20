import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag380kg'
    dbObj.maxRange_m=3033.029297
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=136.653503
    dbObj.fragCharge_kg=117.897667
    dbObj.radCharge_kg=13.665350
    dbObj.fragMetal_kg=125.448837
    dbObj.fragFragment_kg=0.026488
    dbObj.fragSpread=0.300000
    return dbObj
