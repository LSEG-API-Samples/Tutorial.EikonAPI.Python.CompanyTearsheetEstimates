# Company Tearsheet Estimates
# Eikon API Python
# Tutorial

We would like to start this tutorial where Eikon API Proxy Quickstart has left off.  This brief tutorial will discuss the steps required to retrieve the data that is presented in the Estmates section of "Company Tearsheet" Eikon Excel example.

####Introduction
This tuturial is one of the many learning materials published by Refinitiv to help developers learning Refinitiv APIs; it can also be read at  [Fundamentals API - Company Tearsheet Estimate](https://developers.refinitiv.com/en/api-catalog/eikon/eikon-data-api/tutorials#fundamentals-api-company-tearsheet-estimate).  Please consult this page for more learning materials and documentation about this API.

For any question related to this article or the examples please use the Developer Community [Q&A Forum](https://community.developers.refinitiv.com/index.html).

***Note:** To be able to ask questions and to benefit from the full content available on the [Refinitiv Developer Community portal](https://developers.refinitiv.com) we recommend you to [register here]( https://developers.refinitiv.com/en/register) or [login here]( https://community.developers.refinitiv.com/users/login.html).*

### Prerequisites

Please refer to [Quick Start Guide](https://developers.refinitiv.com/en/api-catalog/eikon/eikon-data-api/quick-start) for the details

1. TR Eikon API Proxy is installed
2. Python is installed
3. Eikon Python library is installed

### Expected Result

This is how the Estimates look in Eikon Excel Company Tearsheet template example
![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/excelEstimatesCropped.jpg "Excel Company Tearsheet Estimates")

We learn how to retrieve the same data content via Eikon API from Python
![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/pythonEstimatesCropped.jpg "Same data content, python")

### Approach (Detailed in the Next Sections)

1. Using Eikon Excel for lookupetailed in the next sections
2. Using Data Item Browser (DIB) as reference.
3. Using Eikon Python library to access data



### Using Excel for Lookup

1. From All Programs menu, we expand Refinitiv menu item and select Refinitiv Eikon - Microsoft Excel.
2. Once Excel is open, from Refinitiv menu item we choose "Sign In" option, and enter valid Refinitiv Eikon credentials, hitting "Sign In" button.  The status should change to "Online"

 ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonExcelSignIn.jpg "Eikon Excel Online")

3. Next, from Refinitiv ribbon, we choose Templates

![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonExcelTemplates.jpg "Eikon Excel Templates")

Select from the Template Library "Fundamentals" on the left, then "Company Tearsheet" on the right, then click "Open":

 ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonExcelTearsheet.jpg "Eikon Excel Company Tearsheet")

4. We are looking at the example spreadsheet named "Company Tearsheet".  In this tutorial we will aim to replicate the data retrieval in Estimates parts of this example by using Eikon API from Python.  Let's start by clicking on the bottom tab "Company Tearsheet", while zeroing-in on the section "Estimates"

![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonExcelTearsheetEstimatesMarked.jpg "Eikon Excel Company Tearsheet Estimates")

5. Now we are ready for the most important step in the lookup.  As we click on one of the cells that contain functions retrieving estimates for the company, for example E24, in the Excel formula bar we see the function call that is required to pull this data:

 ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/ExcelFunctionLookupMarked.jpg "Eikon Excel Function Lookup")

 For example, E24 contains TR.RevenueHigh field name with parameters signifying forecast period of next year ("FY1"), scale of 6 or one million, and currency #1, referring to "USD".

 The repeated lookup will allow us to learn how Company Tearsheet example is built, down to every cell,  every function call complete with the required information.  These details we are going to use to call the same  functions from Eikon Python library.

6. While we are still looking at Eikon Excel, let's step aside from Company Tearsheet Estimates example, and consider a generic approach to discovering Eikon data content.  We are going to discuss using _Excel Formula Builder_.
  
 We click on an empty Excel cel and from Refinitiv menu we choose "Build Formula":

 ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonExcelBuildFormulaMarked.jpg "Eikon Excel Build Formula")
 
 Once Formula Builder is up, in the "Instrument" input we type "IBM" and out of the offered options click on "International Business Machines":
  
 ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonExcelBuildFormulaIBM.jpg "Eikon Excel Formula Builder IBM")

 Next, in "Search Data Items" input we type "Revenue High":

 ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonExcelBuildFormulaRevenueHigh.jpg "Eikon Excel Formula Builder Revenue High")

 Now from "Category" selection list we select "Refinitiv Financials", from "Fields" selection list we pick "Total Revenue" and in "Parameter" on the right hand side we change "Financial Period" to "FY-1".

 Our selections are reflected in the ready to use formula in the bottom left corner.  Once we are satisfied with the inputs, we click on "Insert" button in the bottom right corner:

 ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonExcelBuildFormulaTotalRevenue.jpg "Eikon Excel Formula Builder Total Revenue")

 And our Excel spreadsheet, in the selected cell, now reflects the updated Total Revenue:

  ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonExcelTotalRevenue.jpg "Eikon Excel Total Revenue")

### Using DIB as Reference

 Eikon Data Item Browser is a lookup tool that we can use as an alternative to Excel.  It is particularly useful for development on Linux and Mac, as it allows to avoid switching between Linux or Mac and Windows machines.  Once we have started Eikon API Proxy and signed into Refinitiv Eikon, we have an option to start DIB:

![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonAPIProxyMarked.jpg "Starting DIB")

 We use DIB to search for instruments and field names.

 Let's look at the following example.

 For Instrument we enter "IBM", and choose "International Business Machines":

 ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/DIBIBM.jpg "DIB IBM")

 In Data Item Name we look up TR.RevenueHigh,  so we start typing "TR.RevenueH" and once TR.RevenueHigh appears in the main window, we select it.  We are able to:  
 * Lookup the complete list of parameters with possible values (on the right side panel) 
 * Review the specific value we expect for IBM, on the main panel

 ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/DIBMarked.jpg "Using DIB")

### Using Eikon Python Library to Access Data

And now we proceed to the most interesting part.  We know the data items we would like to use by looking it up in Eikon Excel examples, and we can parametrize the data items per requirement, by looking up the data items in Data Item Browser.

1.  We start Python interpreter.  We will work on the python script in separate text editor, pasting and running the script into python interpreter when we are ready to test. 

2.  Let us flex our muscle by running the following little script:

 _Note, please be careful of the spaces and tabs, as python requires them sctrictly observed._
 
 ```
df, err = ek.get_data("IBM", ['TR.RevenueActValue(Period=FY0, Scale=6, Curn=USD)',
                    'TR.RevenueMeanEstimate(Period=FY1, Scale=6, Curn=USD)',
                    'TR.RevenueMeanEstimate(Period=FY2, Scale=6, Curn=USD)'])
df
 ```
 
 We should see the output:
 
 ```
   Instrument  Revenue - Actual  Revenue - Mean Estimate  \
 0        IBM             79919              78717.97129

   Revenue - Mean Estimate
 0              78663.43974
 ```
 
3. Next we try to retrieve data for the three different periods, as required for Esimates in the Excel example spreadsheet, while laying the results out into rows:

 ```
df1, err = ek.get_data("IBM", ['TR.RevenueActValue(Period=FY0, Scale=6, Curn=USD)',
                    'TR.RevenueMeanEstimate(Period=FY1, Scale=6, Curn=USD)',
                    'TR.RevenueMeanEstimate(Period=FY2, Scale=6, Curn=USD)'])

df2, err = ek.get_data("IBM", ['TR.RevenueHigh(Period=FY1, Scale=6, Curn=USD)',
                    'TR.RevenueHigh(Period=FY2, Scale=6, Curn=USD)',
                    'TR.RevenueLow(Period=FY1, Scale=6, Curn=USD)',
                    'TR.RevenueLow(Period=FY2, Scale=6, Curn=USD)'])

df3, err = ek.get_data("IBM", ['TR.RevenueLow(Period=FY1, Scale=6, Curn=USD)',
                    'TR.RevenueLow(Period=FY2, Scale=6, Curn=USD)'])

df4, err = ek.get_data("IBM", ['TR.RevenueMeanEstimate(Period=FY1, RollPeriods=False, Scale=6, Curn=USD)',
                    'TR.RevenueMeanEstimate(Period=FY2, RollPeriods=False, Scale=6, Curn=USD)'])

df1
df2
df3
df4

 ```
 
 We see the output:

 ```
 >>> df1
  Instrument  Revenue - Actual  Revenue - Mean Estimate  \
 0        IBM             79919              78717.97129

   Revenue - Mean Estimate
 0              78663.43974
 >>> df2
  Instrument  Revenue - High  Revenue - High  Revenue - Low  Revenue - Low
 0        IBM           80564           81180          76706          76078
 >>> df3
  Instrument  Revenue - Low  Revenue - Low
 0        IBM          76706          76078
 >>> df4
  Instrument  Revenue - Mean Estimate  Revenue - Mean Estimate
 0        IBM              78717.97129              78663.43974
 >>>
 ```
 
4. Now we are looking to retrieve the complete set of data required, while formatting the output into columns:

Please refer to the [complete script](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/Estimates3.py)

_Note, that there can be only one request to get the field in get_data call.  Therefore, for the same field call, but with different parameters, we use another call._

 When we run this script, the result should be:
 
 ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/pythonEstimatesCropped.jpg "Same data content, python")

We'd like to conclude this tutorial by inviting you to experiment with both the tools and the approach.  Hope you will find the tools useful and approach working, but not set in stone.  We encourage you to share your results and successes, as well as your questions and problems with us on

[Q&A Forum](https://community.developers.refinitiv.com)
