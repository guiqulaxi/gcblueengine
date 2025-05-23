# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcDamageEffect()
    dbObj.databaseClass='Pr 705 Lira durability'
    dbObj.blastEffect=[pygcb.DamagePoint()]*13
    dbObj.blastEffect[0].effectLevel=0.000000
    dbObj.blastEffect[0].damageFactor=0.000000
    dbObj.blastEffect[1].effectLevel=2.700000
    dbObj.blastEffect[1].damageFactor=0.000000
    dbObj.blastEffect[2].effectLevel=2.850000
    dbObj.blastEffect[2].damageFactor=0.100000
    dbObj.blastEffect[3].effectLevel=3.310000
    dbObj.blastEffect[3].damageFactor=0.200000
    dbObj.blastEffect[4].effectLevel=4.070000
    dbObj.blastEffect[4].damageFactor=0.300000
    dbObj.blastEffect[5].effectLevel=5.140000
    dbObj.blastEffect[5].damageFactor=0.400000
    dbObj.blastEffect[6].effectLevel=6.510000
    dbObj.blastEffect[6].damageFactor=0.500000
    dbObj.blastEffect[7].effectLevel=8.190000
    dbObj.blastEffect[7].damageFactor=0.600000
    dbObj.blastEffect[8].effectLevel=10.170000
    dbObj.blastEffect[8].damageFactor=0.700000
    dbObj.blastEffect[9].effectLevel=12.460000
    dbObj.blastEffect[9].damageFactor=0.800000
    dbObj.blastEffect[10].effectLevel=15.060000
    dbObj.blastEffect[10].damageFactor=0.900000
    dbObj.blastEffect[11].effectLevel=17.959999
    dbObj.blastEffect[11].damageFactor=1.000000
    dbObj.blastEffect[12].effectLevel=22.620001
    dbObj.blastEffect[12].damageFactor=2.000000
    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*13
    dbObj.waterBlastEffect[0].effectLevel=0.000000
    dbObj.waterBlastEffect[0].damageFactor=0.000000
    dbObj.waterBlastEffect[1].effectLevel=54.904999
    dbObj.waterBlastEffect[1].damageFactor=0.100000
    dbObj.waterBlastEffect[2].effectLevel=86.586998
    dbObj.waterBlastEffect[2].damageFactor=0.111000
    dbObj.waterBlastEffect[3].effectLevel=135.003998
    dbObj.waterBlastEffect[3].damageFactor=0.125000
    dbObj.waterBlastEffect[4].effectLevel=207.912003
    dbObj.waterBlastEffect[4].damageFactor=0.143000
    dbObj.waterBlastEffect[5].effectLevel=315.920013
    dbObj.waterBlastEffect[5].damageFactor=0.167000
    dbObj.waterBlastEffect[6].effectLevel=473.067993
    dbObj.waterBlastEffect[6].damageFactor=0.200000
    dbObj.waterBlastEffect[7].effectLevel=697.312988
    dbObj.waterBlastEffect[7].damageFactor=0.250000
    dbObj.waterBlastEffect[8].effectLevel=1011.273010
    dbObj.waterBlastEffect[8].damageFactor=0.333000
    dbObj.waterBlastEffect[9].effectLevel=1446.612061
    dbObj.waterBlastEffect[9].damageFactor=0.500000
    dbObj.waterBlastEffect[10].effectLevel=2083.600098
    dbObj.waterBlastEffect[10].damageFactor=1.000000
    dbObj.waterBlastEffect[11].effectLevel=2617.298096
    dbObj.waterBlastEffect[11].damageFactor=2.000000
    dbObj.waterBlastEffect[12].effectLevel=3141.117920
    dbObj.waterBlastEffect[12].damageFactor=4.000000
    dbObj.fragEffect=[pygcb.DamagePoint()]*21
    dbObj.fragEffect[0].effectLevel=0.000000
    dbObj.fragEffect[0].damageFactor=0.000000
    dbObj.fragEffect[1].effectLevel=1500.000000
    dbObj.fragEffect[1].damageFactor=0.000000
    dbObj.fragEffect[2].effectLevel=3000.000000
    dbObj.fragEffect[2].damageFactor=0.014040
    dbObj.fragEffect[3].effectLevel=6000.000000
    dbObj.fragEffect[3].damageFactor=0.019850
    dbObj.fragEffect[4].effectLevel=10000.000000
    dbObj.fragEffect[4].damageFactor=0.025620
    dbObj.fragEffect[5].effectLevel=30000.000000
    dbObj.fragEffect[5].damageFactor=0.044380
    dbObj.fragEffect[6].effectLevel=60000.000000
    dbObj.fragEffect[6].damageFactor=0.062770
    dbObj.fragEffect[7].effectLevel=100000.000000
    dbObj.fragEffect[7].damageFactor=0.081030
    dbObj.fragEffect[8].effectLevel=300000.000000
    dbObj.fragEffect[8].damageFactor=0.140350
    dbObj.fragEffect[9].effectLevel=600000.000000
    dbObj.fragEffect[9].damageFactor=0.198490
    dbObj.fragEffect[10].effectLevel=1000000.000000
    dbObj.fragEffect[10].damageFactor=0.256250
    dbObj.fragEffect[11].effectLevel=3000000.000000
    dbObj.fragEffect[11].damageFactor=0.443840
    dbObj.fragEffect[12].effectLevel=6000000.000000
    dbObj.fragEffect[12].damageFactor=0.627680
    dbObj.fragEffect[13].effectLevel=10000000.000000
    dbObj.fragEffect[13].damageFactor=0.810330
    dbObj.fragEffect[14].effectLevel=30000000.000000
    dbObj.fragEffect[14].damageFactor=1.403530
    dbObj.fragEffect[15].effectLevel=60000000.000000
    dbObj.fragEffect[15].damageFactor=1.984900
    dbObj.fragEffect[16].effectLevel=100000000.000000
    dbObj.fragEffect[16].damageFactor=2.562490
    dbObj.fragEffect[17].effectLevel=300000000.000000
    dbObj.fragEffect[17].damageFactor=4.438360
    dbObj.fragEffect[18].effectLevel=600000000.000000
    dbObj.fragEffect[18].damageFactor=6.276790
    dbObj.fragEffect[19].effectLevel=1000000000.000000
    dbObj.fragEffect[19].damageFactor=8.103310
    dbObj.fragEffect[20].effectLevel=3000000000.000000
    dbObj.fragEffect[20].damageFactor=14.035340
    dbObj.radEffect=[pygcb.DamagePoint()]*5
    dbObj.radEffect[0].effectLevel=0.000000
    dbObj.radEffect[0].damageFactor=0.000000
    dbObj.radEffect[1].effectLevel=15000.000000
    dbObj.radEffect[1].damageFactor=0.000000
    dbObj.radEffect[2].effectLevel=20000.000000
    dbObj.radEffect[2].damageFactor=1.000000
    dbObj.radEffect[3].effectLevel=40000.000000
    dbObj.radEffect[3].damageFactor=2.000000
    dbObj.radEffect[4].effectLevel=60000.000000
    dbObj.radEffect[4].damageFactor=20.000000
    dbObj.internalEffect=[pygcb.DamagePoint()]*8
    dbObj.internalEffect[0].effectLevel=0.000000
    dbObj.internalEffect[0].damageFactor=0.000000
    dbObj.internalEffect[1].effectLevel=1.000000
    dbObj.internalEffect[1].damageFactor=0.275660
    dbObj.internalEffect[2].effectLevel=2.000000
    dbObj.internalEffect[2].damageFactor=0.551750
    dbObj.internalEffect[3].effectLevel=4.000000
    dbObj.internalEffect[3].damageFactor=1.103310
    dbObj.internalEffect[4].effectLevel=8.000000
    dbObj.internalEffect[4].damageFactor=2.206530
    dbObj.internalEffect[5].effectLevel=16.000000
    dbObj.internalEffect[5].damageFactor=4.411970
    dbObj.internalEffect[6].effectLevel=32.000000
    dbObj.internalEffect[6].damageFactor=8.823190
    dbObj.internalEffect[7].effectLevel=64.000000
    dbObj.internalEffect[7].damageFactor=17.647100
    return dbObj
