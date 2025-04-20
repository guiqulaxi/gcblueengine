import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir125kg'
    dbObj.maxRange_m=4042.982910
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=22.614891
    dbObj.fragCharge_kg=57.423405
    dbObj.radCharge_kg=2.261489
    dbObj.fragMetal_kg=44.961704
    dbObj.fragFragment_kg=0.044872
    dbObj.fragSpread=0.300000
    return dbObj
