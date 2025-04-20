import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag28kg'
    dbObj.maxRange_m=938.472107
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=9.997818
    dbObj.fragCharge_kg=8.734788
    dbObj.radCharge_kg=0.999782
    dbObj.fragMetal_kg=9.267394
    dbObj.fragFragment_kg=0.002955
    dbObj.fragSpread=0.300000
    return dbObj
