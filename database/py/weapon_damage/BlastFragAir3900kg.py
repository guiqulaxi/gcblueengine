import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir3900kg'
    dbObj.maxRange_m=11324.921875
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=374.665131
    dbObj.fragCharge_kg=2012.223267
    dbObj.radCharge_kg=37.466511
    dbObj.fragMetal_kg=1513.111572
    dbObj.fragFragment_kg=0.420075
    dbObj.fragSpread=0.300000
    return dbObj
