import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag19kg'
    dbObj.maxRange_m=789.158875
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.767381
    dbObj.fragCharge_kg=5.938413
    dbObj.radCharge_kg=0.676738
    dbObj.fragMetal_kg=6.294206
    dbObj.fragFragment_kg=0.002210
    dbObj.fragSpread=0.300000
    return dbObj
