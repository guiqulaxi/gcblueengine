import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1325kg'
    dbObj.maxRange_m=5121.594727
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=476.822693
    dbObj.fragCharge_kg=410.868195
    dbObj.radCharge_kg=47.682270
    dbObj.fragMetal_kg=437.309113
    dbObj.fragFragment_kg=0.078315
    dbObj.fragSpread=0.300000
    return dbObj
