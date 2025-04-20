import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis27.5kg'
    dbObj.maxRange_m=3085.212402
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.002208
    dbObj.fragCharge_kg=11.948528
    dbObj.radCharge_kg=0.600221
    dbObj.fragMetal_kg=9.549264
    dbObj.fragFragment_kg=0.025809
    dbObj.fragSpread=0.264082
    return dbObj
