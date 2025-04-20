import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag82.5kg'
    dbObj.maxRange_m=1560.825928
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=29.591167
    dbObj.fragCharge_kg=25.647554
    dbObj.radCharge_kg=2.959117
    dbObj.fragMetal_kg=27.261278
    dbObj.fragFragment_kg=0.007313
    dbObj.fragSpread=0.300000
    return dbObj
