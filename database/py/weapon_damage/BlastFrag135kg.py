import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag135kg'
    dbObj.maxRange_m=1964.841675
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=48.479019
    dbObj.fragCharge_kg=41.930653
    dbObj.radCharge_kg=4.847902
    dbObj.fragMetal_kg=44.590328
    dbObj.fragFragment_kg=0.011283
    dbObj.fragSpread=0.300000
    return dbObj
