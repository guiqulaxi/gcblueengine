import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir21kg'
    dbObj.maxRange_m=2899.999756
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.723170
    dbObj.fragCharge_kg=9.031220
    dbObj.radCharge_kg=0.472317
    dbObj.fragMetal_kg=7.245610
    dbObj.fragFragment_kg=0.022785
    dbObj.fragSpread=0.195069
    return dbObj
