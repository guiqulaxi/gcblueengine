import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag65kg'
    dbObj.maxRange_m=1394.109863
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=23.297047
    dbObj.fragCharge_kg=20.218636
    dbObj.radCharge_kg=2.329705
    dbObj.fragMetal_kg=21.484318
    dbObj.fragFragment_kg=0.005941
    dbObj.fragSpread=0.300000
    return dbObj
