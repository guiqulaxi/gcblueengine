import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2050kg'
    dbObj.maxRange_m=8979.279297
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=229.455856
    dbObj.fragCharge_kg=1036.029419
    dbObj.radCharge_kg=22.945585
    dbObj.fragMetal_kg=784.514709
    dbObj.fragFragment_kg=0.249925
    dbObj.fragSpread=0.300000
    return dbObj
