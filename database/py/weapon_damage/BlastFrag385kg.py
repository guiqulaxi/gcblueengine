import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag385kg'
    dbObj.maxRange_m=3047.651855
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=138.453171
    dbObj.fragCharge_kg=119.447884
    dbObj.radCharge_kg=13.845318
    dbObj.fragMetal_kg=127.098938
    dbObj.fragFragment_kg=0.026746
    dbObj.fragSpread=0.300000
    return dbObj
