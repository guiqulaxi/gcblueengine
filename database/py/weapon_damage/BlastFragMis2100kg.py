import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis2100kg'
    dbObj.maxRange_m=9062.462891
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=233.804276
    dbObj.fragCharge_kg=1062.130493
    dbObj.radCharge_kg=23.380426
    dbObj.fragMetal_kg=804.065247
    dbObj.fragFragment_kg=0.255097
    dbObj.fragSpread=0.300000
    return dbObj
