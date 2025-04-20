import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1925kg'
    dbObj.maxRange_m=8762.026367
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=218.451569
    dbObj.fragCharge_kg=970.865601
    dbObj.radCharge_kg=21.845156
    dbObj.fragMetal_kg=735.682800
    dbObj.fragFragment_kg=0.236706
    dbObj.fragSpread=0.300000
    return dbObj
