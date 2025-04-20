import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag35kg'
    dbObj.maxRange_m=1040.641113
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=12.512315
    dbObj.fragCharge_kg=10.908457
    dbObj.radCharge_kg=1.251231
    dbObj.fragMetal_kg=11.579228
    dbObj.fragFragment_kg=0.003530
    dbObj.fragSpread=0.300000
    return dbObj
