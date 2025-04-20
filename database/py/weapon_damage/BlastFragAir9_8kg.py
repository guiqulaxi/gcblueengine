import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir9.8kg'
    dbObj.maxRange_m=2313.811768
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.388353
    dbObj.fragCharge_kg=4.091764
    dbObj.radCharge_kg=0.238835
    dbObj.fragMetal_kg=3.319882
    dbObj.fragFragment_kg=0.014561
    dbObj.fragSpread=0.100278
    return dbObj
