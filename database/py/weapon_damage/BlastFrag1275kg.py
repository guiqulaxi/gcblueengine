import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1275kg'
    dbObj.maxRange_m=5043.115723
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=458.823639
    dbObj.fragCharge_kg=395.367584
    dbObj.radCharge_kg=45.882362
    dbObj.fragMetal_kg=420.808777
    dbObj.fragFragment_kg=0.075794
    dbObj.fragSpread=0.300000
    return dbObj
