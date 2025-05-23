# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcDamageEffect()
    dbObj.databaseClass='Pr 1559V Morskoy Prostor durability'
    dbObj.blastEffect=[pygcb.DamagePoint()]*13
    dbObj.blastEffect[0].effectLevel=0.000000
    dbObj.blastEffect[0].damageFactor=0.000000
    dbObj.blastEffect[1].effectLevel=2.010000
    dbObj.blastEffect[1].damageFactor=0.000000
    dbObj.blastEffect[2].effectLevel=2.110000
    dbObj.blastEffect[2].damageFactor=0.100000
    dbObj.blastEffect[3].effectLevel=2.390000
    dbObj.blastEffect[3].damageFactor=0.200000
    dbObj.blastEffect[4].effectLevel=2.860000
    dbObj.blastEffect[4].damageFactor=0.300000
    dbObj.blastEffect[5].effectLevel=3.510000
    dbObj.blastEffect[5].damageFactor=0.400000
    dbObj.blastEffect[6].effectLevel=4.360000
    dbObj.blastEffect[6].damageFactor=0.500000
    dbObj.blastEffect[7].effectLevel=5.390000
    dbObj.blastEffect[7].damageFactor=0.600000
    dbObj.blastEffect[8].effectLevel=6.610000
    dbObj.blastEffect[8].damageFactor=0.700000
    dbObj.blastEffect[9].effectLevel=8.010000
    dbObj.blastEffect[9].damageFactor=0.800000
    dbObj.blastEffect[10].effectLevel=9.610000
    dbObj.blastEffect[10].damageFactor=0.900000
    dbObj.blastEffect[11].effectLevel=11.390000
    dbObj.blastEffect[11].damageFactor=1.000000
    dbObj.blastEffect[12].effectLevel=14.350000
    dbObj.blastEffect[12].damageFactor=2.000000
    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*28
    dbObj.waterBlastEffect[0].effectLevel=0.000000
    dbObj.waterBlastEffect[0].damageFactor=0.000000
    dbObj.waterBlastEffect[1].effectLevel=57.567001
    dbObj.waterBlastEffect[1].damageFactor=0.040000
    dbObj.waterBlastEffect[2].effectLevel=64.987999
    dbObj.waterBlastEffect[2].damageFactor=0.042000
    dbObj.waterBlastEffect[3].effectLevel=73.319000
    dbObj.waterBlastEffect[3].damageFactor=0.043000
    dbObj.waterBlastEffect[4].effectLevel=82.664001
    dbObj.waterBlastEffect[4].damageFactor=0.045000
    dbObj.waterBlastEffect[5].effectLevel=93.139000
    dbObj.waterBlastEffect[5].damageFactor=0.048000
    dbObj.waterBlastEffect[6].effectLevel=104.873001
    dbObj.waterBlastEffect[6].damageFactor=0.050000
    dbObj.waterBlastEffect[7].effectLevel=118.008003
    dbObj.waterBlastEffect[7].damageFactor=0.053000
    dbObj.waterBlastEffect[8].effectLevel=132.701004
    dbObj.waterBlastEffect[8].damageFactor=0.056000
    dbObj.waterBlastEffect[9].effectLevel=149.126007
    dbObj.waterBlastEffect[9].damageFactor=0.059000
    dbObj.waterBlastEffect[10].effectLevel=167.477005
    dbObj.waterBlastEffect[10].damageFactor=0.062000
    dbObj.waterBlastEffect[11].effectLevel=187.970993
    dbObj.waterBlastEffect[11].damageFactor=0.067000
    dbObj.waterBlastEffect[12].effectLevel=210.850006
    dbObj.waterBlastEffect[12].damageFactor=0.071000
    dbObj.waterBlastEffect[13].effectLevel=236.386002
    dbObj.waterBlastEffect[13].damageFactor=0.077000
    dbObj.waterBlastEffect[14].effectLevel=264.893005
    dbObj.waterBlastEffect[14].damageFactor=0.083000
    dbObj.waterBlastEffect[15].effectLevel=296.729004
    dbObj.waterBlastEffect[15].damageFactor=0.091000
    dbObj.waterBlastEffect[16].effectLevel=332.321991
    dbObj.waterBlastEffect[16].damageFactor=0.100000
    dbObj.waterBlastEffect[17].effectLevel=372.187012
    dbObj.waterBlastEffect[17].damageFactor=0.111000
    dbObj.waterBlastEffect[18].effectLevel=416.976013
    dbObj.waterBlastEffect[18].damageFactor=0.125000
    dbObj.waterBlastEffect[19].effectLevel=467.549988
    dbObj.waterBlastEffect[19].damageFactor=0.143000
    dbObj.waterBlastEffect[20].effectLevel=525.125977
    dbObj.waterBlastEffect[20].damageFactor=0.167000
    dbObj.waterBlastEffect[21].effectLevel=591.568970
    dbObj.waterBlastEffect[21].damageFactor=0.200000
    dbObj.waterBlastEffect[22].effectLevel=670.057007
    dbObj.waterBlastEffect[22].damageFactor=0.250000
    dbObj.waterBlastEffect[23].effectLevel=766.843994
    dbObj.waterBlastEffect[23].damageFactor=0.333000
    dbObj.waterBlastEffect[24].effectLevel=897.184021
    dbObj.waterBlastEffect[24].damageFactor=0.500000
    dbObj.waterBlastEffect[25].effectLevel=1116.758057
    dbObj.waterBlastEffect[25].damageFactor=1.000000
    dbObj.waterBlastEffect[26].effectLevel=1352.545044
    dbObj.waterBlastEffect[26].damageFactor=2.000000
    dbObj.waterBlastEffect[27].effectLevel=1623.239990
    dbObj.waterBlastEffect[27].damageFactor=4.000000
    dbObj.fragEffect=[pygcb.DamagePoint()]*27
    dbObj.fragEffect[0].effectLevel=0.000000
    dbObj.fragEffect[0].damageFactor=0.000000
    dbObj.fragEffect[1].effectLevel=1500.000000
    dbObj.fragEffect[1].damageFactor=0.000000
    dbObj.fragEffect[2].effectLevel=3000.000000
    dbObj.fragEffect[2].damageFactor=0.001550
    dbObj.fragEffect[3].effectLevel=6000.000000
    dbObj.fragEffect[3].damageFactor=0.002200
    dbObj.fragEffect[4].effectLevel=10000.000000
    dbObj.fragEffect[4].damageFactor=0.002840
    dbObj.fragEffect[5].effectLevel=30000.000000
    dbObj.fragEffect[5].damageFactor=0.004920
    dbObj.fragEffect[6].effectLevel=60000.000000
    dbObj.fragEffect[6].damageFactor=0.006950
    dbObj.fragEffect[7].effectLevel=100000.000000
    dbObj.fragEffect[7].damageFactor=0.008980
    dbObj.fragEffect[8].effectLevel=300000.000000
    dbObj.fragEffect[8].damageFactor=0.015550
    dbObj.fragEffect[9].effectLevel=600000.000000
    dbObj.fragEffect[9].damageFactor=0.021990
    dbObj.fragEffect[10].effectLevel=1000000.000000
    dbObj.fragEffect[10].damageFactor=0.028390
    dbObj.fragEffect[11].effectLevel=3000000.000000
    dbObj.fragEffect[11].damageFactor=0.049170
    dbObj.fragEffect[12].effectLevel=6000000.000000
    dbObj.fragEffect[12].damageFactor=0.069540
    dbObj.fragEffect[13].effectLevel=10000000.000000
    dbObj.fragEffect[13].damageFactor=0.089770
    dbObj.fragEffect[14].effectLevel=30000000.000000
    dbObj.fragEffect[14].damageFactor=0.155490
    dbObj.fragEffect[15].effectLevel=60000000.000000
    dbObj.fragEffect[15].damageFactor=0.219890
    dbObj.fragEffect[16].effectLevel=100000000.000000
    dbObj.fragEffect[16].damageFactor=0.283880
    dbObj.fragEffect[17].effectLevel=300000000.000000
    dbObj.fragEffect[17].damageFactor=0.491700
    dbObj.fragEffect[18].effectLevel=600000000.000000
    dbObj.fragEffect[18].damageFactor=0.695360
    dbObj.fragEffect[19].effectLevel=1000000000.000000
    dbObj.fragEffect[19].damageFactor=0.897710
    dbObj.fragEffect[20].effectLevel=3000000000.000000
    dbObj.fragEffect[20].damageFactor=1.554880
    dbObj.fragEffect[21].effectLevel=6000000000.000000
    dbObj.fragEffect[21].damageFactor=2.198930
    dbObj.fragEffect[22].effectLevel=10000000000.000000
    dbObj.fragEffect[22].damageFactor=2.838810
    dbObj.fragEffect[23].effectLevel=30000001024.000000
    dbObj.fragEffect[23].damageFactor=4.916970
    dbObj.fragEffect[24].effectLevel=60000002048.000000
    dbObj.fragEffect[24].damageFactor=6.953640
    dbObj.fragEffect[25].effectLevel=99999997952.000000
    dbObj.fragEffect[25].damageFactor=8.977110
    dbObj.fragEffect[26].effectLevel=299999985664.000000
    dbObj.fragEffect[26].damageFactor=15.548810
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
    dbObj.internalEffect=[pygcb.DamagePoint()]*10
    dbObj.internalEffect[0].effectLevel=0.000000
    dbObj.internalEffect[0].damageFactor=0.000000
    dbObj.internalEffect[1].effectLevel=1.000000
    dbObj.internalEffect[1].damageFactor=0.060970
    dbObj.internalEffect[2].effectLevel=2.000000
    dbObj.internalEffect[2].damageFactor=0.121910
    dbObj.internalEffect[3].effectLevel=4.000000
    dbObj.internalEffect[3].damageFactor=0.243840
    dbObj.internalEffect[4].effectLevel=8.000000
    dbObj.internalEffect[4].damageFactor=0.487750
    dbObj.internalEffect[5].effectLevel=16.000000
    dbObj.internalEffect[5].damageFactor=0.975310
    dbObj.internalEffect[6].effectLevel=32.000000
    dbObj.internalEffect[6].damageFactor=1.950730
    dbObj.internalEffect[7].effectLevel=64.000000
    dbObj.internalEffect[7].damageFactor=3.901080
    dbObj.internalEffect[8].effectLevel=128.000000
    dbObj.internalEffect[8].damageFactor=7.802460
    dbObj.internalEffect[9].effectLevel=256.000000
    dbObj.internalEffect[9].damageFactor=15.603590
    return dbObj
