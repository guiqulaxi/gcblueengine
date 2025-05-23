# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcDamageEffect()
    dbObj.databaseClass='Light Patrol Boat PBF durability'
    dbObj.blastEffect=[pygcb.DamagePoint()]*13
    dbObj.blastEffect[0].effectLevel=0.000000
    dbObj.blastEffect[0].damageFactor=0.000000
    dbObj.blastEffect[1].effectLevel=1.890000
    dbObj.blastEffect[1].damageFactor=0.000000
    dbObj.blastEffect[2].effectLevel=1.910000
    dbObj.blastEffect[2].damageFactor=0.100000
    dbObj.blastEffect[3].effectLevel=1.970000
    dbObj.blastEffect[3].damageFactor=0.200000
    dbObj.blastEffect[4].effectLevel=2.080000
    dbObj.blastEffect[4].damageFactor=0.300000
    dbObj.blastEffect[5].effectLevel=2.230000
    dbObj.blastEffect[5].damageFactor=0.400000
    dbObj.blastEffect[6].effectLevel=2.430000
    dbObj.blastEffect[6].damageFactor=0.500000
    dbObj.blastEffect[7].effectLevel=2.670000
    dbObj.blastEffect[7].damageFactor=0.600000
    dbObj.blastEffect[8].effectLevel=2.950000
    dbObj.blastEffect[8].damageFactor=0.700000
    dbObj.blastEffect[9].effectLevel=3.270000
    dbObj.blastEffect[9].damageFactor=0.800000
    dbObj.blastEffect[10].effectLevel=3.640000
    dbObj.blastEffect[10].damageFactor=0.900000
    dbObj.blastEffect[11].effectLevel=4.050000
    dbObj.blastEffect[11].damageFactor=1.000000
    dbObj.blastEffect[12].effectLevel=5.110000
    dbObj.blastEffect[12].damageFactor=2.000000
    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*12
    dbObj.waterBlastEffect[0].effectLevel=0.000000
    dbObj.waterBlastEffect[0].damageFactor=0.000000
    dbObj.waterBlastEffect[1].effectLevel=40.092999
    dbObj.waterBlastEffect[1].damageFactor=0.111000
    dbObj.waterBlastEffect[2].effectLevel=45.521000
    dbObj.waterBlastEffect[2].damageFactor=0.125000
    dbObj.waterBlastEffect[3].effectLevel=51.797001
    dbObj.waterBlastEffect[3].damageFactor=0.143000
    dbObj.waterBlastEffect[4].effectLevel=59.137001
    dbObj.waterBlastEffect[4].damageFactor=0.167000
    dbObj.waterBlastEffect[5].effectLevel=67.884003
    dbObj.waterBlastEffect[5].damageFactor=0.200000
    dbObj.waterBlastEffect[6].effectLevel=78.625000
    dbObj.waterBlastEffect[6].damageFactor=0.250000
    dbObj.waterBlastEffect[7].effectLevel=92.528999
    dbObj.waterBlastEffect[7].damageFactor=0.333000
    dbObj.waterBlastEffect[8].effectLevel=112.475998
    dbObj.waterBlastEffect[8].damageFactor=0.500000
    dbObj.waterBlastEffect[9].effectLevel=149.220001
    dbObj.waterBlastEffect[9].damageFactor=1.000000
    dbObj.waterBlastEffect[10].effectLevel=192.447998
    dbObj.waterBlastEffect[10].damageFactor=2.000000
    dbObj.waterBlastEffect[11].effectLevel=245.873001
    dbObj.waterBlastEffect[11].damageFactor=4.000000
    dbObj.fragEffect=[pygcb.DamagePoint()]*18
    dbObj.fragEffect[0].effectLevel=0.000000
    dbObj.fragEffect[0].damageFactor=0.000000
    dbObj.fragEffect[1].effectLevel=1500.000000
    dbObj.fragEffect[1].damageFactor=0.000000
    dbObj.fragEffect[2].effectLevel=3000.000000
    dbObj.fragEffect[2].damageFactor=0.041030
    dbObj.fragEffect[3].effectLevel=6000.000000
    dbObj.fragEffect[3].damageFactor=0.058020
    dbObj.fragEffect[4].effectLevel=10000.000000
    dbObj.fragEffect[4].damageFactor=0.074910
    dbObj.fragEffect[5].effectLevel=30000.000000
    dbObj.fragEffect[5].damageFactor=0.129740
    dbObj.fragEffect[6].effectLevel=60000.000000
    dbObj.fragEffect[6].damageFactor=0.183480
    dbObj.fragEffect[7].effectLevel=100000.000000
    dbObj.fragEffect[7].damageFactor=0.236880
    dbObj.fragEffect[8].effectLevel=300000.000000
    dbObj.fragEffect[8].damageFactor=0.410280
    dbObj.fragEffect[9].effectLevel=600000.000000
    dbObj.fragEffect[9].damageFactor=0.580230
    dbObj.fragEffect[10].effectLevel=1000000.000000
    dbObj.fragEffect[10].damageFactor=0.749070
    dbObj.fragEffect[11].effectLevel=3000000.000000
    dbObj.fragEffect[11].damageFactor=1.297420
    dbObj.fragEffect[12].effectLevel=6000000.000000
    dbObj.fragEffect[12].damageFactor=1.834830
    dbObj.fragEffect[13].effectLevel=10000000.000000
    dbObj.fragEffect[13].damageFactor=2.368760
    dbObj.fragEffect[14].effectLevel=30000000.000000
    dbObj.fragEffect[14].damageFactor=4.102810
    dbObj.fragEffect[15].effectLevel=60000000.000000
    dbObj.fragEffect[15].damageFactor=5.802250
    dbObj.fragEffect[16].effectLevel=100000000.000000
    dbObj.fragEffect[16].damageFactor=7.490670
    dbObj.fragEffect[17].effectLevel=300000000.000000
    dbObj.fragEffect[17].damageFactor=12.974230
    dbObj.radEffect=[pygcb.DamagePoint()]*6
    dbObj.radEffect[0].effectLevel=0.000000
    dbObj.radEffect[0].damageFactor=0.000000
    dbObj.radEffect[1].effectLevel=5000.000000
    dbObj.radEffect[1].damageFactor=0.000000
    dbObj.radEffect[2].effectLevel=25000.000000
    dbObj.radEffect[2].damageFactor=0.400000
    dbObj.radEffect[3].effectLevel=50000.000000
    dbObj.radEffect[3].damageFactor=2.000000
    dbObj.radEffect[4].effectLevel=125000.000000
    dbObj.radEffect[4].damageFactor=5.000000
    dbObj.radEffect[5].effectLevel=250000.000000
    dbObj.radEffect[5].damageFactor=20.000000
    dbObj.internalEffect=[pygcb.DamagePoint()]*2
    dbObj.internalEffect[0].effectLevel=0.000000
    dbObj.internalEffect[0].damageFactor=0.000000
    dbObj.internalEffect[1].effectLevel=1.000000
    dbObj.internalEffect[1].damageFactor=83.025032
    return dbObj
