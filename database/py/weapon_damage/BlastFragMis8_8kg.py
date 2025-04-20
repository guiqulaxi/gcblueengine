import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis8.8kg'
    dbObj.maxRange_m=2227.199463
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.168003
    dbObj.fragCharge_kg=3.658664
    dbObj.radCharge_kg=0.216800
    dbObj.fragMetal_kg=2.973332
    dbObj.fragFragment_kg=0.013515
    dbObj.fragSpread=0.093364
    return dbObj
