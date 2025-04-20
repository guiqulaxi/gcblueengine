import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir380kg'
    dbObj.maxRange_m=5058.411133
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=58.328995
    dbObj.fragCharge_kg=181.514008
    dbObj.radCharge_kg=5.832899
    dbObj.fragMetal_kg=140.156998
    dbObj.fragFragment_kg=0.071802
    dbObj.fragSpread=0.300000
    return dbObj
