# Company Tearsheet Estimates
# Eikon Scripting Tutorial
# Python

We would like to start this tutorial where Eikon Scrpting Proxy Quickstart has left off.  This brief tutorial will discuss the steps required to retrieve the data that is presented in the Estmates section of "Company Tearsheet" Eikon Excel example.

### Prerequisites

Please refer to [Quick Start](https://developers.thomsonreuters.com/tr-eikon-scripting-apis-eap-limited-access/eikon-web-and-scripting-apis-beta/quick-start) for the details

1. TR Eikon Scripting Proxy is installed
2. Python is installed
3. Eikon Python library is installed

### Expected Result

This is how the Estimates look in Eikon Excel Company Tearsheet template example
![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/excelEstimatesCropped.jpg "Excel Company Tearsheet Estimates")

We learn how to retrieve the same data content via Eikon scripting from python
![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/pythonEstimatesCropped.jpg "Same data content, python")

### Approach
1. Using Eikon Excel for lookup
2. Using DIB as reference
3. Using Eikon Python library to access data

### Using Excel for Lookup

1. From All Programs menu, we expand Thomson Reuters menu item and select Thomson Reuters Eikon - Microsoft Excel.
2. Once Excel is open, from Thomson Reuters menu item we choose "Sign In" option, and enter your Thomson Reuters Eikon credentials, hitting "Sign In" button.  The status should change to "Online"

 ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonExcelSignIn.jpg "Eikon Excel Online")

3. Next, from Thomson Reuters menu item, we choose Templates

![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonExcelTemplates.jpg "Eikon Excel Templates")

And select from the Template Library first "Fundamentals" on the left, then "Company Tearsheet" on the right, then click "Open":

 ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonExcelTearsheet.jpg "Eikon Excel Company Tearsheet")

4. We are looking at the template, or example "Company Tearsheet".  In this tutorial we will aim to replicate the data retrieval in Estimates parts of this example by using eikon scripting from python.  Let's start by clicking on the bottom tab "Company Tearsheet", while zeroing-in on the section "Estimates"

![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonExcelTearsheetEstimatesMarked.jpg "Eikon Excel Company Tearsheet Estimates")

5. Now we are ready for the most important of the steps in lookup, the actual lookup.  As we click on one of the cells that contain the estimate functions, for example E24, in the Excel formula window we see the  function call that is required to pull this data:

 ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/ExcelFunctionLookupMarked.jpg "Eikon Excel Function Lookup")

 For example, E24 conpains TR.RevenueHigh with parameters period being "FY1", scale equaling 6, and currency #1,  referring to "USD"

 The repeated lookup will allow us to learn how Company Tearsheet example is built, down to every cell,  every function call complete with the required information.  These details we are going to use to call the same  functions from python eikon.

6. While we are still looking at Eikon Excel, let's step aside from Company Tearsheet Estimates example, and consider a generic approach to discovering Eikon data content.  We are are going to discuss using _Excel Formula Builder_.

  1. We click on an empty Excel cel and from ThomsonReuters menu we choose Formula Builder:

  ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonExcelFormulaBuilderMarked.jpg "Eikon Excel Formula Builder")
 
  2. Once Formula Builder is up, in the Instrument input we type "IBM" and out of the offered options click on "International Business Machines":
  
  ![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonExcelFormulaBuilderIBM.jpg "Eikon Excel Formula Builder IBM")

### Using DIB as Reference

 Eikon Data Item Browser is a tool that we use to reference eikon scripting.  Once we have started Eikon Scripting Proxy and signed into Thomson Reuters Eikon, we have an option to start DIB:

![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/EikonScriptingProxyMarked.jpg "Starting DIB")

We use DIB to search for the right data item, for example, for Instrument we enter "IBM", and Data Item Name we look up is TR.RevenueHigh,we are able to:  
 * Lookup the complete list of parameters with possible values (on the right side panel) 
 * Review the specific value we expect for IBM, on the main panel

![alt text](https://github.com/TR-API-Samples/EikonScriptingProxy_CompanyTearsheetEstimates_Python/blob/master/DIBMarked.jpg "Using DIB")

### Using Eikon Python Library to Access Data

And now we proceed to the most interesting part.  We know the data items we would like to use by lookingit up in Eikon Excel examples, and we can parametrize the data items per requirement, by looking up the data itemsin Data Item Browser.

1.  We start Python interpreter.  We will work on the python script in separate text editor, pasting and running the script into python interpreter when we are ready to test. 

2.  Let us flex our muscle by running the following little script:

 _Note, please be careful of the spaces and tabs, as python requires them sctrictly observed._
 
 ```
 df, err = ek.get_data("IBM", 
					[ 
                    ('TR.RevenueActValue', {'Period': 'FY0','Scale': 6, 'Curn': 'USD'}),
                    ('TR.RevenueMeanEstimate', {'Period': 'FY1','Scale': 6, 'Curn': 'USD'}),
                    ('TR.RevenueMeanEstimate', {'Period': 'FY2','Scale': 6, 'Curn': 'USD'})
                    ])
 df
 ```
 
 We should see the output:
 
 ```
   Instrument  Revenue - Actual  Revenue - Mean Estimate  \
 0        IBM             79919              78717.97129

   Revenue - Mean Estimate
 0              78663.43974
 ```
 
3. Next we try to retrieve data for the three different periods, as required for Esimatesdata region, while laying the results out into rows:

 ```
 df1, err = ek.get_data("IBM", 
					[ 
                    ('TR.RevenueActValue', {'Period': 'FY0','Scale': 6, 'Curn': 'USD'}),
                    ('TR.RevenueMeanEstimate', {'Period': 'FY1','Scale': 6, 'Curn': 'USD'}),
                    ('TR.RevenueMeanEstimate', {'Period': 'FY2','Scale': 6, 'Curn': 'USD'})
                    ],sort_on=None, output='pandas', debug=True)

 df2, err = ek.get_data("IBM", 
					[ 
                    ('TR.RevenueHigh', {'Period': 'FY1','Scale': 6, 'Curn': 'USD'}),
                    ('TR.RevenueHigh', {'Period': 'FY2','Scale': 6, 'Curn': 'USD'}),
                    ('TR.RevenueLow', {'Period': 'FY1','Scale': 6, 'Curn': 'USD'}),
                    ('TR.RevenueLow', {'Period': 'FY2','Scale': 6, 'Curn': 'USD'})
                    ],sort_on=None, output='pandas', debug=True)


 df3, err = ek.get_data("IBM", 
					[ 
                    ('TR.RevenueLow', {'Period': 'FY1','Scale': 6, 'Curn': 'USD'}),
                    ('TR.RevenueLow', {'Period': 'FY2','Scale': 6, 'Curn': 'USD'})
                    ],sort_on=None, output='pandas', debug=True)



 df4, err = ek.get_data("IBM", 
					[ 
                    ('TR.RevenueMeanEstimate', {'Period': 'FY1','RollPeriods': 'False','Scale': 6, 'Curn': 'USD'}),
                    ('TR.RevenueMeanEstimate', {'Period': 'FY2','RollPeriods': 'False','Scale': 6, 'Curn': 'USD'})
                    ],sort_on=None, output='pandas', debug=True)

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

[Q&A Forum](https://community.developers.thomsonreuters.com)
