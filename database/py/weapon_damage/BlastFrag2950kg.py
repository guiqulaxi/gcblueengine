import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2950kg'
    dbObj.maxRange_m=7017.683105
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1061.802979
    dbObj.fragCharge_kg=914.631348
    dbObj.radCharge_kg=106.180298
    dbObj.fragMetal_kg=973.565674
    dbObj.fragFragment_kg=0.154045
    dbObj.fragSpread=0.300000
    return dbObj
