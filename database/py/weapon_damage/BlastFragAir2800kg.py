import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2800kg'
    dbObj.maxRange_m=10091.423828
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=291.872711
    dbObj.fragCharge_kg=1429.418213
    dbObj.radCharge_kg=29.187271
    dbObj.fragMetal_kg=1078.709106
    dbObj.fragFragment_kg=0.324229
    dbObj.fragSpread=0.300000
    return dbObj
