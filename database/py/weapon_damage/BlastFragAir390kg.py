import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir390kg'
    dbObj.maxRange_m=5091.478516
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=59.614120
    dbObj.fragCharge_kg=186.457260
    dbObj.radCharge_kg=5.961412
    dbObj.fragMetal_kg=143.928619
    dbObj.fragFragment_kg=0.072802
    dbObj.fragSpread=0.300000
    return dbObj
