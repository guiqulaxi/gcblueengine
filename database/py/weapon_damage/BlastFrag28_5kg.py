import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag28.5kg'
    dbObj.maxRange_m=945.415344
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=10.177382
    dbObj.fragCharge_kg=8.890079
    dbObj.radCharge_kg=1.017738
    dbObj.fragMetal_kg=9.432540
    dbObj.fragFragment_kg=0.002993
    dbObj.fragSpread=0.300000
    return dbObj
