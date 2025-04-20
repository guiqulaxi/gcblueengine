import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir340kg'
    dbObj.maxRange_m=4914.608887
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=53.121773
    dbObj.fragCharge_kg=161.785477
    dbObj.radCharge_kg=5.312178
    dbObj.fragMetal_kg=125.092743
    dbObj.fragFragment_kg=0.067545
    dbObj.fragSpread=0.300000
    return dbObj
