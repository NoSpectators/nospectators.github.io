# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 11:44:15 2016

@author: John
"""

import csv
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults #GetUpdatedPropertyDetails


def getZillowResults(address,zipcode):
    zillow_data = ZillowWrapper("your-api-key")
    deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
    result = GetDeepSearchResults(deep_search_response)
    return result
#try:
#    new = getZillowResults('5521 4TH ST','20009')
#    print new.home_type
#except:
#    print 'not working'
    

    
blighted_zillow_data=[]
myFile = open('blighted.csv','rt')
myReader = csv.reader(myFile) 
for row in myReader:
    if row[0] != 'Street Address':
        
        try:                    
            result = getZillowResults(row[0], row[7])
            home_type = result.home_type                
            tax_year = result.tax_year
            tax_value = result.tax_value
            year_built = result.year_built
            property_size = result.property_size
            home_size = result.home_size
            bathrooms = result.bathrooms
            bedrooms = result.bedrooms
            last_sold_date = result.last_sold_date
            last_sold_price_currency = result.last_sold_price_currency
            last_sold_price = result.last_sold_price
            zestimate_amount = result.zestimate_amount
            zestimate_last_updated = result.zestimate_last_updated
            zestimate_value_change = result.zestimate_value_change
            zestimate_valuation_range_high = result.zestimate_valuation_range_high
            zestimate_valuationRange_low = result.zestimate_valuationRange_low
            zestimate_percentile = result.zestimate_percentile
                          
            
        except:
            home_type = 'unknown'               
            tax_year = 'unknown'
            tax_value = 'unknown'
            year_built = 'unknown'
            property_size = 'unknown'
            home_size = 'unknown'
            bathrooms = 'unknown'
            bedrooms = 'unknown'
            last_sold_date = 'unknown'
            last_sold_price_currency = 'unknown'
            last_sold_price = 'unknown'
            zestimate_amount = 'unknown'
            zestimate_last_updated = 'unknown'
            zestimate_value_change = 'unknown'
            zestimate_valuation_range_high = 'unknown'
            zestimate_valuationRange_low = 'unknown'
            zestimate_percentile = 'unknown'
            
        
        blighted_zillow_data.append((home_type, tax_year, year_built,
                                    property_size, home_size, bathrooms,
                                    bedrooms, last_sold_date, 
                                    last_sold_price_currency,
                                    last_sold_price, zestimate_amount, 
                                    zestimate_last_updated, 
                                    zestimate_value_change,
                                    zestimate_valuation_range_high,
                                    zestimate_valuationRange_low,
                                    zestimate_percentile))
                                    
                                    
vacant_zillow_data=[]
myFile = open('vacant.csv','rt')
myReader = csv.reader(myFile) 
for row in myReader:
    if row[0] != 'Street Address':
        
        try:                    
            result = getZillowResults(row[0], row[7])
            home_type = result.home_type                
            tax_year = result.tax_year
            tax_value = result.tax_value
            year_built = result.year_built
            property_size = result.property_size
            home_size = result.home_size
            bathrooms = result.bathrooms
            bedrooms = result.bedrooms
            last_sold_date = result.last_sold_date
            last_sold_price_currency = result.last_sold_price_currency
            last_sold_price = result.last_sold_price
            zestimate_amount = result.zestimate_amount
            zestimate_last_updated = result.zestimate_last_updated
            zestimate_value_change = result.zestimate_value_change
            zestimate_valuation_range_high = result.zestimate_valuation_range_high
            zestimate_valuationRange_low = result.zestimate_valuationRange_low
            zestimate_percentile = result.zestimate_percentile
                          
            
        except:
            home_type = 'unknown'               
            tax_year = 'unknown'
            tax_value = 'unknown'
            year_built = 'unknown'
            property_size = 'unknown'
            home_size = 'unknown'
            bathrooms = 'unknown'
            bedrooms = 'unknown'
            last_sold_date = 'unknown'
            last_sold_price_currency = 'unknown'
            last_sold_price = 'unknown'
            zestimate_amount = 'unknown'
            zestimate_last_updated = 'unknown'
            zestimate_value_change = 'unknown'
            zestimate_valuation_range_high = 'unknown'
            zestimate_valuationRange_low = 'unknown'
            zestimate_percentile = 'unknown'
            
        
        vacant_zillow_data.append((home_type, tax_year, year_built,
                                    property_size, home_size, bathrooms,
                                    bedrooms, last_sold_date, 
                                    last_sold_price_currency,
                                    last_sold_price, zestimate_amount, 
                                    zestimate_last_updated, 
                                    zestimate_value_change,
                                    zestimate_valuation_range_high,
                                    zestimate_valuationRange_low,
                                    zestimate_percentile))
                                    
with open('blighted_zillow_data.csv','wb') as fp1:
    a = csv.writer(fp1, delimiter=",")
    a.writerow(['home_type', 'tax_year', 'year_built',                
                'property_size', 'home_size', 'bathrooms',
                'bedrooms', 'last_sold_date', 
                'last_sold_price_currency',
                'last_sold_price', 'zestimate_amount', 
                'zestimate_last_updated', 
                'zestimate_value_change',
                'zestimate_valuation_range_high',
                'zestimate_valuationRange_low',
                'zestimate_percentile'])
    a.writerows(blighted_zillow_data)       
        
        
with open('vacant_zillow_data.csv','wb') as fp:
    a = csv.writer(fp, delimiter=",")
    a.writerow(['home_type', 'tax_year', 'year_built',                
                'property_size', 'home_size', 'bathrooms',
                'bedrooms', 'last_sold_date', 
                'last_sold_price_currency',
                'last_sold_price', 'zestimate_amount', 
                'zestimate_last_updated', 
                'zestimate_value_change',
                'zestimate_valuation_range_high',
                'zestimate_valuationRange_low',
                'zestimate_percentile'])
    a.writerows(vacant_zillow_data)  
        

            
            
            
            
            
            
>>>>>>> 2b93400195eb6dd38d578f49b17fa2d6eb187742
