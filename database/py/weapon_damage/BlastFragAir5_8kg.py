import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir5.8kg'
    dbObj.maxRange_m=1895.120361
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.488546
    dbObj.fragCharge_kg=2.371636
    dbObj.radCharge_kg=0.148855
    dbObj.fragMetal_kg=1.939818
    dbObj.fragFragment_kg=0.009897
    dbObj.fragSpread=0.074105
    return dbObj
