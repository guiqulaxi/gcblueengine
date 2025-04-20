import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1875kg'
    dbObj.maxRange_m=8672.761719
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=213.994492
    dbObj.fragCharge_kg=944.837036
    dbObj.radCharge_kg=21.399448
    dbObj.fragMetal_kg=716.168518
    dbObj.fragFragment_kg=0.231395
    dbObj.fragSpread=0.300000
    return dbObj
