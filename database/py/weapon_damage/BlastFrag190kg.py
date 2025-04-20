import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag190kg'
    dbObj.maxRange_m=2292.352295
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=68.270592
    dbObj.fragCharge_kg=58.986271
    dbObj.radCharge_kg=6.827059
    dbObj.fragMetal_kg=62.743137
    dbObj.fragFragment_kg=0.015199
    dbObj.fragSpread=0.300000
    return dbObj
