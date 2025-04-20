import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag67.5kg'
    dbObj.maxRange_m=1419.764404
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=24.196115
    dbObj.fragCharge_kg=20.994255
    dbObj.radCharge_kg=2.419612
    dbObj.fragMetal_kg=22.309628
    dbObj.fragFragment_kg=0.006143
    dbObj.fragSpread=0.300000
    return dbObj
