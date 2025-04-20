import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir3.1kg'
    dbObj.maxRange_m=1433.651367
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.843498
    dbObj.fragCharge_kg=1.235668
    dbObj.radCharge_kg=0.084350
    dbObj.fragMetal_kg=1.020834
    dbObj.fragFragment_kg=0.005867
    dbObj.fragSpread=0.058403
    return dbObj
