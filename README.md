# ABS-Waterfall-Cash-Flow-Analysis
Python script that simulates an ABS cash flow waterfall for structured finance. It allocates periodic cash flows to tranches (Senior, Mezzanine, Junior) in priority order—paying interest, then principal—and captures residual distributions once all debt is repaid. Results are tabulated and plotted.

Expected results: 
  ABS Cash Flow Waterfall Payment Schedule:
   Period  AssetPoolCash  Senior_Interest_Due  Senior_Interest_Paid  \
0       1           30.0             5.000000              5.000000   
1       2           30.0             4.130000              4.130000   
2       3           30.0             3.216500              3.216500   
3       4           30.0             2.257325              2.257325   
4       5           30.0             1.250191              1.250191   
5       6           30.0             0.192701              0.192701   
6       7           30.0             0.000000              0.000000   
7       8           30.0             0.000000              0.000000   
8       9           30.0             0.000000              0.000000   

   Mezzanine_Interest_Due  Mezzanine_Interest_Paid  Junior_Interest_Due  \
0                4.000000                 4.000000             3.600000   
1                4.000000                 4.000000             3.600000   
2                4.000000                 4.000000             3.600000   
3                4.000000                 4.000000             3.600000   
4                4.000000                 4.000000             3.600000   
5                4.000000                 4.000000             3.600000   
6                2.531737                 2.531737             3.600000   
7                0.622276                 0.622276             3.600000   
8                0.000000                 0.000000             1.440088   

   Junior_Interest_Paid  Senior_Principal_Paid  Senior_Remaining_Balance  \
0              3.600000              17.400000                 82.600000   
1              3.600000              18.270000                 64.330000   
2              3.600000              19.183500                 45.146500   
3              3.600000              20.142675                 25.003825   
4              3.600000              21.149809                  3.854016   
5              3.600000               3.854016                  0.000000   
6              3.600000               0.000000                  0.000000   
7              3.600000               0.000000                  0.000000   
8              1.440088               0.000000                  0.000000   

   Mezzanine_Principal_Paid  Mezzanine_Remaining_Balance  \
0                  0.000000                    50.000000   
1                  0.000000                    50.000000   
2                  0.000000                    50.000000   
3                  0.000000                    50.000000   
4                  0.000000                    50.000000   
5                 18.353283                    31.646717   
6                 23.868263                     7.778454   
7                  7.778454                     0.000000   
8                  0.000000                     0.000000   

   Junior_Principal_Paid  Junior_Remaining_Balance  Residual_Distribution  \
0               0.000000                 30.000000               0.000000   
1               0.000000                 30.000000               0.000000   
2               0.000000                 30.000000               0.000000   
3               0.000000                 30.000000               0.000000   
4               0.000000                 30.000000               0.000000   
5               0.000000                 30.000000               0.000000   
6               0.000000                 30.000000               0.000000   
7              17.999269                 12.000731               0.000000   
8              12.000731                  0.000000              16.559182   

   Cash_Unused  All_Tranches_Paid  
0          0.0              False  
1          0.0              False  
2          0.0              False  
3          0.0              False  
4          0.0              False  
5          0.0              False  
6          0.0              False  
7          0.0              False  
8          0.0               True  
