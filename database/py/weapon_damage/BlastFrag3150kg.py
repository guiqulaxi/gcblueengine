import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3150kg'
    dbObj.maxRange_m=7198.956055
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1133.801392
    dbObj.fragCharge_kg=976.632446
    dbObj.radCharge_kg=113.380135
    dbObj.fragMetal_kg=1039.566162
    dbObj.fragFragment_kg=0.162839
    dbObj.fragSpread=0.300000
    return dbObj
