import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir16.5kg'
    dbObj.maxRange_m=2721.903320
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.809200
    dbObj.fragCharge_kg=7.030533
    dbObj.radCharge_kg=0.380920
    dbObj.fragMetal_kg=5.660266
    dbObj.fragFragment_kg=0.020072
    dbObj.fragSpread=0.153403
    return dbObj
