import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1.6kg'
    dbObj.maxRange_m=200.136017
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.564408
    dbObj.fragCharge_kg=0.503728
    dbObj.radCharge_kg=0.056441
    dbObj.fragMetal_kg=0.531864
    dbObj.fragFragment_kg=0.000329
    dbObj.fragSpread=0.300000
    return dbObj
