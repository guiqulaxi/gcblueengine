import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1.9kg'
    dbObj.maxRange_m=227.352448
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.668170
    dbObj.fragCharge_kg=0.599553
    dbObj.radCharge_kg=0.066817
    dbObj.fragMetal_kg=0.632277
    dbObj.fragFragment_kg=0.000380
    dbObj.fragSpread=0.300000
    return dbObj
