import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag750kg'
    dbObj.maxRange_m=4063.895264
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=269.836731
    dbObj.fragCharge_kg=232.608841
    dbObj.radCharge_kg=26.983673
    dbObj.fragMetal_kg=247.554428
    dbObj.fragFragment_kg=0.048200
    dbObj.fragSpread=0.300000
    return dbObj
