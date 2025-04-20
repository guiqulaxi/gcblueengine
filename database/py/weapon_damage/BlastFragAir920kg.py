import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir920kg'
    dbObj.maxRange_m=6539.894043
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=121.155014
    dbObj.fragCharge_kg=452.829987
    dbObj.radCharge_kg=12.115501
    dbObj.fragMetal_kg=346.014984
    dbObj.fragFragment_kg=0.124600
    dbObj.fragSpread=0.300000
    return dbObj
