import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir165kg'
    dbObj.maxRange_m=4246.205566
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=28.721863
    dbObj.fragCharge_kg=76.552094
    dbObj.radCharge_kg=2.872186
    dbObj.fragMetal_kg=59.726048
    dbObj.fragFragment_kg=0.049689
    dbObj.fragSpread=0.300000
    return dbObj
