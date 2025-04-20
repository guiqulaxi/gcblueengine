import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag8.2kg'
    dbObj.maxRange_m=514.472900
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.900106
    dbObj.fragCharge_kg=2.576596
    dbObj.radCharge_kg=0.290011
    dbObj.fragMetal_kg=2.723298
    dbObj.fragFragment_kg=0.001127
    dbObj.fragSpread=0.300000
    return dbObj
