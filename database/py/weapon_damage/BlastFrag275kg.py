import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag275kg'
    dbObj.maxRange_m=2677.306885
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=98.861473
    dbObj.fragCharge_kg=85.342354
    dbObj.radCharge_kg=9.886147
    dbObj.fragMetal_kg=90.796173
    dbObj.fragFragment_kg=0.020635
    dbObj.fragSpread=0.300000
    return dbObj
