import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag700kg'
    dbObj.maxRange_m=3948.745605
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=251.838425
    dbObj.fragCharge_kg=217.107712
    dbObj.radCharge_kg=25.183844
    dbObj.fragMetal_kg=231.053864
    dbObj.fragFragment_kg=0.045412
    dbObj.fragSpread=0.300000
    return dbObj
