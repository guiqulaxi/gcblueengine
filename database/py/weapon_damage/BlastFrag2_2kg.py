import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2.2kg'
    dbObj.maxRange_m=251.439545
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.772554
    dbObj.fragCharge_kg=0.694964
    dbObj.radCharge_kg=0.077255
    dbObj.fragMetal_kg=0.732482
    dbObj.fragFragment_kg=0.000428
    dbObj.fragSpread=0.300000
    return dbObj
