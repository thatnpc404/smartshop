import pandas as pd 

amazon_data=pd.read_excel('C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\amazon_data.xlsx',nrows=4)
amazon_data['Price']=pd.to_numeric(amazon_data['Price'].apply(lambda x:x.replace(",","")))

amazon_data=amazon_data.sort_values('Price')
best_val_amazon=amazon_data.head(1).values


flip_data=pd.read_excel('C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\flipkart_data.xlsx',nrows=4)
flip_data['Price']=flip_data['Price'].apply(lambda x:x.replace(",",""))
flip_data['Price']=flip_data['Price'].apply(lambda x:x.replace("₹",""))
flip_data['Price']=pd.to_numeric(flip_data['Price'])
flip_data=flip_data.sort_values('Price')
best_val_flip=flip_data.head(1).values



website=["Amazon","Flipkart"]
pricing=[best_val_amazon[0][2],best_val_flip[0][2]]
prod_name=[best_val_amazon[0][0],best_val_flip[0][0]]
url=[best_val_amazon[0][1],best_val_flip[0][1]]

merged=pd.DataFrame(
    {
        'Website':website,
        'Product Name':prod_name,
        'Price':pricing,
        'Url':url

    }
)

merged=merged.sort_values("Price")
print(merged.head(1).values[0])