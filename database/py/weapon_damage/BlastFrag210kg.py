import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag210kg'
    dbObj.maxRange_m=2393.699707
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=75.468124
    dbObj.fragCharge_kg=65.187920
    dbObj.radCharge_kg=7.546813
    dbObj.fragMetal_kg=69.343956
    dbObj.fragFragment_kg=0.016542
    dbObj.fragSpread=0.300000
    return dbObj
