import eikon as ek
ek.set_app_id('F1968B7782740096D4E66')

dfFY0, err = ek.get_data("IBM", 
                         [ 
                    {'TR.RevenueActValue':{'params':{'Period': 'FY0','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.EBITDAActValue':{'params':{'Period': 'FY0','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.EPSActValue':{'params':{'Period': 'FY0','Curn': 'USD'}}}
                    ],debug=True)
 
dfFY1, err = ek.get_data("IBM", 
                    [
                    {'TR.RevenueMeanEstimate':{'params':{'Period': 'FY1','Scale': 6, 'Curn': 'USD', 'Precision':2}}},
                    {'TR.RevenueHigh':{'params':{'Period': 'FY1','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.RevenueLow':{'params':{'Period': 'FY1','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.EBITDAMean':{'params':{'Period': 'FY1','Scale': 6, 'Curn': 'USD', 'Precision':2}}},
                    {'TR.EBITDAHigh':{'params':{'Period': 'FY1','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.EBITDALow':{'params':{'Period': 'FY1','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.EPSMeanEstimate':{'params':{'Period': 'FY1','Curn': 'USD'}}},
                    {'TR.EPSHigh':{'params':{'Period': 'FY1','Curn': 'USD'}}},
                    {'TR.EPSLow':{'params':{'Period': 'FY1','Curn': 'USD'}}}
                    ],debug=True)

# there can be only one request to get the field in get_data call
# for the same field but with different parameters, we use another call                   
dfFY1Roll, err = ek.get_data("IBM", 
                    [
                    {'TR.RevenueMeanEstimate':{'params':{'Period': 'FY1','RollPeriods': 'False','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.EBITDAMean':{'params':{'Period': 'FY1','RollPeriods': 'False','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.EPSMeanEstimate':{'params':{'Period': 'FY1','RollPeriods': 'False','Curn': 'USD','Precision':2}}}
                    ], debug=True)

dfFY2, err = ek.get_data("IBM", 
                    [
                    {'TR.RevenueMeanEstimate':{'params':{'Period': 'FY2','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.RevenueHigh':{'params':{'Period': 'FY2','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.RevenueLow':{'params':{'Period': 'FY2','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.EBITDAMean':{'params':{'Period': 'FY2','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.EBITDAHigh':{'params':{'Period': 'FY2','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.EBITDALow':{'params':{'Period': 'FY2','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.EPSMeanEstimate':{'params':{'Period': 'FY2','Curn': 'USD'}}},
                    {'TR.EPSHigh':{'params':{'Period': 'FY2','Curn': 'USD'}}},
                    {'TR.EPSLow':{'params':{'Period': 'FY2','Curn': 'USD'}}},
                    ],debug=True)

dfFY2Roll, err = ek.get_data("IBM", 
                    [
                    {'TR.RevenueMeanEstimate':{'params':{'Period': 'FY2','RollPeriods': 'False','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.EBITDAMean':{'params':{'Period': 'FY2','RollPeriods': 'False','Scale': 6, 'Curn': 'USD'}}},
                    {'TR.EPSMeanEstimate':{'params':{'Period': 'FY2','RollPeriods': 'False','Curn': 'USD','Precision':2}}}
                    ],debug=True)

dfFY0
dfFY1
dfFY1Roll
dfFY2
dfFY2Roll

print("\n\nIBM\tSales (MIL)\t\t\t\t\tEst. 30\t\tEBITDA (MIL)\t\t\t\t\tEst.30\t\tEPS\n"+

"Period\tMean Est.\tHigh Est.\tLow Est.\t30 Days Ago\tMean Est.\tHigh Est.\tLow Est.\t30 Days Ago\tMean Est.\n"+

"FY0\t" + str(dfFY0['Revenue - Actual'][0])+"\t\t\t\t\t\t\t\t"+str(dfFY0['EBITDA - Actual'][0])+
"\t\t\t\t\t\t\t\t"+str(dfFY0['Earnings Per Share - Actual'][0])+"\n"+

"FY1\t" + str(dfFY1['Revenue - Mean Estimate'][0])+"\t"+ str(dfFY1['Revenue - High'][0])+"\t\t"+str(dfFY1['Revenue - Low'][0])+"\t\t"+
str(dfFY1Roll['Revenue - Mean Estimate'][0])+"\t"+str(dfFY1['EBITDA - Mean'][0])+"\t"+str(dfFY1['EBITDA - High'][0])+"\t\t"+
str(dfFY1['EBITDA - Low'][0])+"\t"+str(dfFY1Roll['EBITDA - Mean'][0])+"\t"+
str(dfFY1['Earnings Per Share - Mean Estimate'][0])+"\n"+

"FY2\t" + str(dfFY2['Revenue - Mean Estimate'][0])+"\t"+ str(dfFY2['Revenue - High'][0])+"\t\t"+str(dfFY2['Revenue - Low'][0])+"\t\t"+
str(dfFY2Roll['Revenue - Mean Estimate'][0])+"\t"+str(dfFY2['EBITDA - Mean'][0]) +"\t"+str(dfFY2['EBITDA - High'][0])+"\t"+
str(dfFY2['EBITDA - Low'][0])+"\t"+str(dfFY2Roll['EBITDA - Mean'][0])+"\t"+
str(dfFY2['Earnings Per Share - Mean Estimate'][0]))

