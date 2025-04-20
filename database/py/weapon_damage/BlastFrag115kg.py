import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag115kg'
    dbObj.maxRange_m=1821.830200
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=41.282974
    dbObj.fragCharge_kg=35.728016
    dbObj.radCharge_kg=4.128297
    dbObj.fragMetal_kg=37.989010
    dbObj.fragFragment_kg=0.009771
    dbObj.fragSpread=0.300000
    return dbObj
