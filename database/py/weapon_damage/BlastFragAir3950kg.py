import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir3950kg'
    dbObj.maxRange_m=11373.673828
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=378.227509
    dbObj.fragCharge_kg=2038.848389
    dbObj.radCharge_kg=37.822750
    dbObj.fragMetal_kg=1532.924194
    dbObj.fragFragment_kg=0.424163
    dbObj.fragSpread=0.300000
    return dbObj
