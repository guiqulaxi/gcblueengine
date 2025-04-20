import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag15kg'
    dbObj.maxRange_m=702.352295
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.333211
    dbObj.fragCharge_kg=4.694526
    dbObj.radCharge_kg=0.533321
    dbObj.fragMetal_kg=4.972263
    dbObj.fragFragment_kg=0.001828
    dbObj.fragSpread=0.300000
    return dbObj
