import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis850kg'
    dbObj.maxRange_m=6394.602539
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=113.595703
    dbObj.fragCharge_kg=417.269531
    dbObj.radCharge_kg=11.359571
    dbObj.fragMetal_kg=319.134766
    dbObj.fragFragment_kg=0.118682
    dbObj.fragSpread=0.300000
    return dbObj
