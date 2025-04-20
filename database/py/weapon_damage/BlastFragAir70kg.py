import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir70kg'
    dbObj.maxRange_m=3707.501221
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=13.665345
    dbObj.fragCharge_kg=31.489771
    dbObj.radCharge_kg=1.366534
    dbObj.fragMetal_kg=24.844885
    dbObj.fragFragment_kg=0.037530
    dbObj.fragSpread=0.300000
    return dbObj
