import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir235kg'
    dbObj.maxRange_m=4467.699707
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=38.857262
    dbObj.fragCharge_kg=110.395157
    dbObj.radCharge_kg=3.885726
    dbObj.fragMetal_kg=85.747581
    dbObj.fragFragment_kg=0.055250
    dbObj.fragSpread=0.300000
    return dbObj
