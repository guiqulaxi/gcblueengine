import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag13kg'
    dbObj.maxRange_m=651.926270
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.616741
    dbObj.fragCharge_kg=4.072173
    dbObj.radCharge_kg=0.461674
    dbObj.fragMetal_kg=4.311087
    dbObj.fragFragment_kg=0.001623
    dbObj.fragSpread=0.300000
    return dbObj
