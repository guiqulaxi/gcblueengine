import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1525kg'
    dbObj.maxRange_m=7984.831055
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=181.819855
    dbObj.fragCharge_kg=763.286743
    dbObj.radCharge_kg=18.181984
    dbObj.fragMetal_kg=579.893372
    dbObj.fragFragment_kg=0.192784
    dbObj.fragSpread=0.300000
    return dbObj
