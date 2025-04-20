import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir245kg'
    dbObj.maxRange_m=4491.071289
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=40.258957
    dbObj.fragCharge_kg=115.260696
    dbObj.radCharge_kg=4.025896
    dbObj.fragMetal_kg=89.480347
    dbObj.fragFragment_kg=0.055855
    dbObj.fragSpread=0.300000
    return dbObj
