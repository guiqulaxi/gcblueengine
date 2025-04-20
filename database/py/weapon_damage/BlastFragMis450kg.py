import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis450kg'
    dbObj.maxRange_m=5269.743164
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=67.197334
    dbObj.fragCharge_kg=216.201782
    dbObj.radCharge_kg=6.719734
    dbObj.fragMetal_kg=166.600891
    dbObj.fragFragment_kg=0.078327
    dbObj.fragSpread=0.300000
    return dbObj
