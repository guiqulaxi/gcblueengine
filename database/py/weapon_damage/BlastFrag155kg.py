import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag155kg'
    dbObj.maxRange_m=2093.622803
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=55.675613
    dbObj.fragCharge_kg=48.132923
    dbObj.radCharge_kg=5.567561
    dbObj.fragMetal_kg=51.191463
    dbObj.fragFragment_kg=0.012747
    dbObj.fragSpread=0.300000
    return dbObj
