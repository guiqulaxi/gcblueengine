import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis20kg'
    dbObj.maxRange_m=2864.825684
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.522323
    dbObj.fragCharge_kg=8.585118
    dbObj.radCharge_kg=0.452232
    dbObj.fragMetal_kg=6.892559
    dbObj.fragFragment_kg=0.022234
    dbObj.fragSpread=0.185378
    return dbObj
