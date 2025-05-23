# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcDamageEffect()
    dbObj.databaseClass='Pr 11435 Brezhnev durability'
    dbObj.blastEffect=[pygcb.DamagePoint()]*13
    dbObj.blastEffect[0].effectLevel=0.000000
    dbObj.blastEffect[0].damageFactor=0.000000
    dbObj.blastEffect[1].effectLevel=2.850000
    dbObj.blastEffect[1].damageFactor=0.000000
    dbObj.blastEffect[2].effectLevel=3.090000
    dbObj.blastEffect[2].damageFactor=0.100000
    dbObj.blastEffect[3].effectLevel=3.830000
    dbObj.blastEffect[3].damageFactor=0.200000
    dbObj.blastEffect[4].effectLevel=5.060000
    dbObj.blastEffect[4].damageFactor=0.300000
    dbObj.blastEffect[5].effectLevel=6.790000
    dbObj.blastEffect[5].damageFactor=0.400000
    dbObj.blastEffect[6].effectLevel=9.010000
    dbObj.blastEffect[6].damageFactor=0.500000
    dbObj.blastEffect[7].effectLevel=11.720000
    dbObj.blastEffect[7].damageFactor=0.600000
    dbObj.blastEffect[8].effectLevel=14.920000
    dbObj.blastEffect[8].damageFactor=0.700000
    dbObj.blastEffect[9].effectLevel=18.620001
    dbObj.blastEffect[9].damageFactor=0.800000
    dbObj.blastEffect[10].effectLevel=22.799999
    dbObj.blastEffect[10].damageFactor=0.900000
    dbObj.blastEffect[11].effectLevel=27.490000
    dbObj.blastEffect[11].damageFactor=1.000000
    dbObj.blastEffect[12].effectLevel=34.630001
    dbObj.blastEffect[12].damageFactor=2.000000
    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*27
    dbObj.waterBlastEffect[0].effectLevel=0.000000
    dbObj.waterBlastEffect[0].damageFactor=0.000000
    dbObj.waterBlastEffect[1].effectLevel=83.592003
    dbObj.waterBlastEffect[1].damageFactor=0.042000
    dbObj.waterBlastEffect[2].effectLevel=95.012001
    dbObj.waterBlastEffect[2].damageFactor=0.043000
    dbObj.waterBlastEffect[3].effectLevel=107.936996
    dbObj.waterBlastEffect[3].damageFactor=0.045000
    dbObj.waterBlastEffect[4].effectLevel=122.558998
    dbObj.waterBlastEffect[4].damageFactor=0.048000
    dbObj.waterBlastEffect[5].effectLevel=139.091995
    dbObj.waterBlastEffect[5].damageFactor=0.050000
    dbObj.waterBlastEffect[6].effectLevel=157.781006
    dbObj.waterBlastEffect[6].damageFactor=0.053000
    dbObj.waterBlastEffect[7].effectLevel=178.901001
    dbObj.waterBlastEffect[7].damageFactor=0.056000
    dbObj.waterBlastEffect[8].effectLevel=202.761993
    dbObj.waterBlastEffect[8].damageFactor=0.059000
    dbObj.waterBlastEffect[9].effectLevel=229.720001
    dbObj.waterBlastEffect[9].damageFactor=0.062000
    dbObj.waterBlastEffect[10].effectLevel=260.179993
    dbObj.waterBlastEffect[10].damageFactor=0.067000
    dbObj.waterBlastEffect[11].effectLevel=294.606995
    dbObj.waterBlastEffect[11].damageFactor=0.071000
    dbObj.waterBlastEffect[12].effectLevel=333.545013
    dbObj.waterBlastEffect[12].damageFactor=0.077000
    dbObj.waterBlastEffect[13].effectLevel=377.631012
    dbObj.waterBlastEffect[13].damageFactor=0.083000
    dbObj.waterBlastEffect[14].effectLevel=427.627991
    dbObj.waterBlastEffect[14].damageFactor=0.091000
    dbObj.waterBlastEffect[15].effectLevel=484.464996
    dbObj.waterBlastEffect[15].damageFactor=0.100000
    dbObj.waterBlastEffect[16].effectLevel=549.312012
    dbObj.waterBlastEffect[16].damageFactor=0.111000
    dbObj.waterBlastEffect[17].effectLevel=623.689026
    dbObj.waterBlastEffect[17].damageFactor=0.125000
    dbObj.waterBlastEffect[18].effectLevel=709.666016
    dbObj.waterBlastEffect[18].damageFactor=0.143000
    dbObj.waterBlastEffect[19].effectLevel=810.237976
    dbObj.waterBlastEffect[19].damageFactor=0.167000
    dbObj.waterBlastEffect[20].effectLevel=930.075989
    dbObj.waterBlastEffect[20].damageFactor=0.200000
    dbObj.waterBlastEffect[21].effectLevel=1077.240967
    dbObj.waterBlastEffect[21].damageFactor=0.250000
    dbObj.waterBlastEffect[22].effectLevel=1267.739990
    dbObj.waterBlastEffect[22].damageFactor=0.333000
    dbObj.waterBlastEffect[23].effectLevel=1541.042969
    dbObj.waterBlastEffect[23].damageFactor=0.500000
    dbObj.waterBlastEffect[24].effectLevel=2044.463013
    dbObj.waterBlastEffect[24].damageFactor=1.000000
    dbObj.waterBlastEffect[25].effectLevel=2636.740967
    dbObj.waterBlastEffect[25].damageFactor=2.000000
    dbObj.waterBlastEffect[26].effectLevel=3368.709961
    dbObj.waterBlastEffect[26].damageFactor=4.000000
    dbObj.fragEffect=[pygcb.DamagePoint()]*19
    dbObj.fragEffect[0].effectLevel=0.000000
    dbObj.fragEffect[0].damageFactor=0.000000
    dbObj.fragEffect[1].effectLevel=7705099.500000
    dbObj.fragEffect[1].damageFactor=0.000000
    dbObj.fragEffect[2].effectLevel=10000000.000000
    dbObj.fragEffect[2].damageFactor=0.020920
    dbObj.fragEffect[3].effectLevel=30000000.000000
    dbObj.fragEffect[3].damageFactor=0.036240
    dbObj.fragEffect[4].effectLevel=60000000.000000
    dbObj.fragEffect[4].damageFactor=0.051250
    dbObj.fragEffect[5].effectLevel=100000000.000000
    dbObj.fragEffect[5].damageFactor=0.066170
    dbObj.fragEffect[6].effectLevel=300000000.000000
    dbObj.fragEffect[6].damageFactor=0.114600
    dbObj.fragEffect[7].effectLevel=600000000.000000
    dbObj.fragEffect[7].damageFactor=0.162070
    dbObj.fragEffect[8].effectLevel=1000000000.000000
    dbObj.fragEffect[8].damageFactor=0.209240
    dbObj.fragEffect[9].effectLevel=3000000000.000000
    dbObj.fragEffect[9].damageFactor=0.362410
    dbObj.fragEffect[10].effectLevel=6000000000.000000
    dbObj.fragEffect[10].damageFactor=0.512520
    dbObj.fragEffect[11].effectLevel=10000000000.000000
    dbObj.fragEffect[11].damageFactor=0.661670
    dbObj.fragEffect[12].effectLevel=30000001024.000000
    dbObj.fragEffect[12].damageFactor=1.146040
    dbObj.fragEffect[13].effectLevel=60000002048.000000
    dbObj.fragEffect[13].damageFactor=1.620740
    dbObj.fragEffect[14].effectLevel=99999997952.000000
    dbObj.fragEffect[14].damageFactor=2.092370
    dbObj.fragEffect[15].effectLevel=299999985664.000000
    dbObj.fragEffect[15].damageFactor=3.624090
    dbObj.fragEffect[16].effectLevel=599999971328.000000
    dbObj.fragEffect[16].damageFactor=5.125240
    dbObj.fragEffect[17].effectLevel=999999995904.000000
    dbObj.fragEffect[17].damageFactor=6.616650
    dbObj.fragEffect[18].effectLevel=3000000053248.000000
    dbObj.fragEffect[18].damageFactor=11.460380
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
    dbObj.internalEffect=[pygcb.DamagePoint()]*15
    dbObj.internalEffect[0].effectLevel=0.000000
    dbObj.internalEffect[0].damageFactor=0.000000
    dbObj.internalEffect[1].effectLevel=1.000000
    dbObj.internalEffect[1].damageFactor=0.000220
    dbObj.internalEffect[2].effectLevel=2.000000
    dbObj.internalEffect[2].damageFactor=0.000430
    dbObj.internalEffect[3].effectLevel=4.000000
    dbObj.internalEffect[3].damageFactor=0.000860
    dbObj.internalEffect[4].effectLevel=8.000000
    dbObj.internalEffect[4].damageFactor=0.001730
    dbObj.internalEffect[5].effectLevel=16.000000
    dbObj.internalEffect[5].damageFactor=0.003450
    dbObj.internalEffect[6].effectLevel=32.000000
    dbObj.internalEffect[6].damageFactor=0.006900
    dbObj.internalEffect[7].effectLevel=64.000000
    dbObj.internalEffect[7].damageFactor=0.013800
    dbObj.internalEffect[8].effectLevel=128.000000
    dbObj.internalEffect[8].damageFactor=0.027600
    dbObj.internalEffect[9].effectLevel=256.000000
    dbObj.internalEffect[9].damageFactor=0.055210
    dbObj.internalEffect[10].effectLevel=512.000000
    dbObj.internalEffect[10].damageFactor=0.110400
    dbObj.internalEffect[11].effectLevel=1024.000000
    dbObj.internalEffect[11].damageFactor=0.220810
    dbObj.internalEffect[12].effectLevel=2048.000000
    dbObj.internalEffect[12].damageFactor=0.441620
    dbObj.internalEffect[13].effectLevel=4096.000000
    dbObj.internalEffect[13].damageFactor=0.883290
    dbObj.internalEffect[14].effectLevel=8192.000000
    dbObj.internalEffect[14].damageFactor=1.766570
    return dbObj
