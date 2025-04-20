import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1.1kg'
    dbObj.maxRange_m=827.098572
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.327414
    dbObj.fragCharge_kg=0.419724
    dbObj.radCharge_kg=0.032741
    dbObj.fragMetal_kg=0.352862
    dbObj.fragFragment_kg=0.002233
    dbObj.fragSpread=0.048156
    return dbObj
