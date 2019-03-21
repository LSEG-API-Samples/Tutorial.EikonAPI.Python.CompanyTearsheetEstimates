import eikon as ek
ek.set_app_id('your app key')

dfFY0, err = ek.get_data("IBM", 
                 ['TR.RevenueActValue(Period=FY0, Scale=6, Curn=USD)',
                  'TR.EBITDAActValue(Period=FY0, Scale=6, Curn=USD)',
                  'TR.EPSActValue(Period=FY0, Curn=USD)'])
 
dfFY1, err = ek.get_data("IBM", 
                 ['TR.RevenueMeanEstimate(Period=FY1, Scale=6, Curn=USD, Precision=0)',
                  'TR.RevenueHigh(Period=FY1, Scale=6, Curn=USD, Precision=0)',
                  'TR.RevenueLow(Period=FY1, Scale=6, Curn=USD, Precision=0)',
                  'TR.EBITDAMean(Period=FY1, Scale=6, Curn=USD, Precision=0)',
                  'TR.EBITDAHigh(Period=FY1, Scale=6, Curn=USD, Precision=0)',
                  'TR.EBITDALow(Period=FY1, Scale=6, Curn=USD, Precision=0)',
                  'TR.EPSMeanEstimate(Period=FY1, Curn=USD)', 'TR.EPSHigh(Period=FY1, Curn=USD)', 'TR.EPSLow(Period=FY1, Curn=USD)'])

# there can be only one request to get the field in get_data call
# for the same field but with different parameters, we use another call                   
dfFY1Roll, err = ek.get_data("IBM", 
                     ['TR.RevenueMeanEstimate(Period=FY1, Scale=6, Curn=USD, RollPeriods=False, Precision=0)',
                      'TR.EBITDAMean(Period=FY1, Scale=6, Curn=USD, RollPeriods=False, Precision=0)',
                      'TR.EPSMeanEstimate(Period=FY1, Curn=USD, RollPeriods=False)'])

dfFY2, err = ek.get_data("IBM", 
                 ['TR.RevenueMeanEstimate(Period=FY2, Scale=6, Curn=USD, Precision=0)',
                  'TR.RevenueHigh(Period=FY2, Scale=6, Curn=USD, Precision=0)',
                  'TR.RevenueLow(Period=FY2, Scale=6, Curn=USD, Precision=0)',
                  'TR.EBITDAMean(Period=FY2, Scale=6, Curn=USD, Precision=0)',
                  'TR.EBITDAHigh(Period=FY2, Scale=6, Curn=USD, Precision=0)',
                  'TR.EBITDALow(Period=FY2, Scale=6, Curn=USD, Precision=0)',
                  'TR.EPSMeanEstimate(Period=FY2, Curn=USD)', 'TR.EPSHigh(Period=FY2, Curn=USD)', 'TR.EPSLow(Period=FY2, Curn=USD)'])

dfFY2Roll, err = ek.get_data("IBM", 
                     ['TR.RevenueMeanEstimate(Period=FY2, Scale=6, Curn=USD, RollPeriods=False, Precision=0)',
                      'TR.EBITDAMean(Period=FY2, Scale=6, Curn=USD, RollPeriods=False, Precision=0)',
                      'TR.EPSMeanEstimate(Period=FY2, Curn=USD, RollPeriods=False)'])

dfFY0
dfFY1
dfFY1Roll
dfFY2
dfFY2Roll

print("\n\nIBM\tSales (MIL)\t\t\t\t\tEst. 30\t\tEBITDA (MIL)\t\t\t\t\tEst.30\t\tEPS\n"+

"Period\tMean Est.\tHigh Est.\tLow Est.\t30 Days Ago\tMean Est.\tHigh Est.\tLow Est.\t30 Days Ago\tMean Est.\n"+

"FY0\t" + str(dfFY0['Revenue - Actual'][0])+"\t\t\t\t\t\t\t\t"+str(dfFY0['EBITDA - Actual'][0])+
"\t\t\t\t\t\t\t\t"+str(dfFY0['Earnings Per Share - Actual'][0])+"\n"+

"FY1\t" + str(dfFY1['Revenue - Mean Estimate'][0])+"\t\t"+ str(dfFY1['Revenue - High'][0])+"\t\t"+str(dfFY1['Revenue - Low'][0])+"\t\t"+
str(dfFY1Roll['Revenue - Mean Estimate'][0])+"\t\t"+str(dfFY1['EBITDA - Mean'][0])+"\t\t"+str(dfFY1['EBITDA - High'][0])+"\t\t"+
str(dfFY1['EBITDA - Low'][0])+"\t\t"+str(dfFY1Roll['EBITDA - Mean'][0])+"\t\t"+
str(dfFY1['Earnings Per Share - Mean Estimate'][0])+"\n"+

"FY2\t" + str(dfFY2['Revenue - Mean Estimate'][0])+"\t\t"+ str(dfFY2['Revenue - High'][0])+"\t\t"+str(dfFY2['Revenue - Low'][0])+"\t\t"+
str(dfFY2Roll['Revenue - Mean Estimate'][0])+"\t\t"+str(dfFY2['EBITDA - Mean'][0]) +"\t\t"+str(dfFY2['EBITDA - High'][0])+"\t\t"+
str(dfFY2['EBITDA - Low'][0])+"\t\t"+str(dfFY2Roll['EBITDA - Mean'][0])+"\t\t"+
str(dfFY2['Earnings Per Share - Mean Estimate'][0]))

