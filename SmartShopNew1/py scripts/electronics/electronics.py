import pandas as pd 
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import time


amazon_data=pd.read_excel('C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\amazon_data.xlsx',nrows=4).dropna()
amazon_data['Price']=pd.to_numeric(amazon_data['Price'].apply(lambda x:str(x).replace(",","")))
amazon_data=amazon_data.sort_values('Price')
best_val_amazon=amazon_data.head(1).values

flipkart_data=pd.read_excel('C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\flipkart_data.xlsx',nrows=4)[::3]
flipkart_data['Price']=flipkart_data['Price'].apply(lambda x:x[1:].replace(",",""))
flipkart_data['Price']=pd.to_numeric(flipkart_data['Price'])
flipkart_data=flipkart_data.sort_values('Price')
best_val_flipkart_data=flipkart_data.head(1).values


croma_data=pd.read_excel('C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\croma_data.xlsx',nrows=4)
croma_data['Price']=pd.to_numeric(croma_data['Price'].apply(lambda x:x[1:].replace(",","")))
croma_data=croma_data.sort_values('Price')
best_val_croma=croma_data.head(1).values



website=["Amazon","Flipkart","Croma"]
pricing=[best_val_amazon[0][2],best_val_flipkart_data[0][2],best_val_croma[0][2]]
prod_name=[best_val_amazon[0][0],best_val_flipkart_data[0][0],best_val_croma[0][0]]
url=[best_val_amazon[0][1],best_val_flipkart_data[0][1],best_val_croma[0][1]]


merged=pd.DataFrame(
    {
        'Website':website,
        'Product Name':prod_name,
        'Price':pricing,
        'Url':url

    }
)
merged=merged.sort_values("Price")

#UI code

if merged["Website"].head(1).values=="Amazon" and merged["Website"].iloc[1]=="Flipkart":
    img_name1,img_name2,img_name3="amazon_logo.png","flipkart_logo.png","croma_logo.png"
    prod_name1,prod_name2,prod_name3=merged["Product Name"].iloc[0],merged["Product Name"].iloc[1],merged["Product Name"].iloc[2]
    price1,price2,price3=merged["Price"].iloc[0],merged["Price"].iloc[1],merged["Price"].iloc[2]


elif merged["Website"].head(1).values=="Amazon" and merged["Website"].iloc[1]=="Croma":
    img_name1,img_name2,img_name3="amazon_logo.png","croma_logo.png","flipkart_logo.png"
    prod_name1,prod_name2,prod_name3=merged["Product Name"].iloc[0],merged["Product Name"].iloc[1],merged["Product Name"].iloc[2]
    price1,price2,price3=merged["Price"].iloc[0],merged["Price"].iloc[1],merged["Price"].iloc[2]

elif merged["Website"].head(1).values=="Flipkart" and merged["Website"].iloc[1]=="Croma":
    img_name1,img_name2,img_name3="flipkart_logo.png","croma_logo.png","amazon_logo.png"
    prod_name1,prod_name2,prod_name3=merged["Product Name"].iloc[0],merged["Product Name"].iloc[1],merged["Product Name"].iloc[2]
    price1,price2,price3=merged["Price"].iloc[0],merged["Price"].iloc[1],merged["Price"].iloc[2]

elif merged["Website"].head(1).values=="Flipkart" and merged["Website"].iloc[1]=="Amazon":
    img_name1,img_name2,img_name3="flipkart_logo.png","amazon_logo.png","croma_logo.png"
    prod_name1,prod_name2,prod_name3=merged["Product Name"].iloc[0],merged["Product Name"].iloc[1],merged["Product Name"].iloc[2]
    price1,price2,price3=merged["Price"].iloc[0],merged["Price"].iloc[1],merged["Price"].iloc[2]

elif merged["Website"].head(1).values=="Croma" and merged["Website"].iloc[1]=="Amazon":
    img_name1,img_name2,img_name3="croma_logo.png","amazon_logo.png","flipkart_logo.png"
    prod_name1,prod_name2,prod_name3=merged["Product Name"].iloc[0],merged["Product Name"].iloc[1],merged["Product Name"].iloc[2]
    price1,price2,price3=merged["Price"].iloc[0],merged["Price"].iloc[1],merged["Price"].iloc[2]

elif merged["Website"].head(1).values=="Croma" and merged["Website"].iloc[1]=="Flipkart":
    img_name1,img_name2,img_name3="croma_logo.png","flipkart_logo.png","amazon_logo.png"
    prod_name1,prod_name2,prod_name3=merged["Product Name"].iloc[0],merged["Product Name"].iloc[1],merged["Product Name"].iloc[2]
    price1,price2,price3=merged["Price"].iloc[0],merged["Price"].iloc[1],merged["Price"].iloc[2]


#UI



def on_element_click(event, url):
    # Change the background color (or any other effect) when clicked
    event.widget.configure(bg="lightblue")
    open_url(url)
    # You can add more effects here

def on_element_release(event):
    # Change the background color (or other effects) back to the original when released
    event.widget.configure(bg="#5A5A5A")
    # You can reset other effects here

def move_text():
    x1, _ = canvas.coords(text_id)
    canvas.move(text_id, 5, 0)
    if x1 >= canvas.winfo_width():
        canvas.coords(text_id, 10, 50)  # Set the initial position
    canvas.after(50, move_text) 

def open_url(url):
    webbrowser.open(url)

img_path1="C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\py scripts\\electronics\\"+img_name1
img_path2="C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\py scripts\\electronics\\"+img_name2
img_path3="C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\py scripts\\electronics\\"+img_name3


# Create the main application window
root = tk.Tk()

root.title("Electronics : SmartShop")
# root.geometry("1920x1080")
root.attributes('-fullscreen',True)

#background image

img = Image.open('C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\py scripts\\electronics\\background.jpg')
img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

# Create a label for the image
img_label = tk.Label(root, image=img)
img_label.place(x=0, y=0, relwidth=1, relheight=1) 


#for the moving text
canvas = tk.Canvas(root, width=1000, height=80)
#canvas.grid(row=4,column=2)
text_id = canvas.create_text(10, 100, text="Welcome to SmartShop :) ", anchor="w", font=("Arial", 20),fill="white")
canvas.configure(bg="indigo")
move_text() 


# Load the image using PIL
image = Image.open(img_path1)
image = image.resize((400, 150))  # Resize the image to your desired size
image = ImageTk.PhotoImage(image)

image1 = Image.open(img_path2)
image1 = image1.resize((400, 130))  # Resize the image to your desired size
image1 = ImageTk.PhotoImage(image1)

image2= Image.open(img_path3)
image2 = image2.resize((400, 300))  # Resize the image to your desired size
image2 = ImageTk.PhotoImage(image2)

# Create a label to display the image
image_label = tk.Label(root, image=image)
image_label1 = tk.Label(root, image=image1)
image_label2= tk.Label(root, image=image2)

# Define the URL you want to open when the image is clicked
url_to_open1 = merged["Url"].head(1).values[0]  # Replace with your desired URL
url_to_open2 = merged["Url"].iloc[1]  # Replace with your desired URL
url_to_open3 = merged["Url"].iloc[2]

# Bind a click event to the label to open the URL
image_label.bind("<Button-1>", lambda event: open_url(url_to_open1))
image_label1.bind("<Button-1>", lambda event: open_url(url_to_open2))
image_label2.bind("<Button-1>", lambda event: open_url(url_to_open3))


image_label.configure(bg="#09090c")
image_label1.configure(bg="#09090c")
image_label2.configure(bg="#09090c")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

# Display the image label
image_label.grid(row=0+1,column=1)
image_label1.grid(row=1+1,column=1)
image_label2.grid(row=2+1,column=1)


text_var1 = tk.StringVar()
text_var2 = tk.StringVar()
text_var3=  tk.StringVar()


text_var1.set(prod_name1)
text_var2.set(prod_name2)
text_var3.set(prod_name3)

price_var1 = tk.StringVar()
price_var2 = tk.StringVar()
price_var3 = tk.StringVar()

price_var1.set("₹"+str(price1))
price_var2.set("₹"+str(price2))
price_var3.set("₹"+str(price3))


name1=tk.Label(root,textvariable=text_var1,font=("Arial", 25),fg="white",bg="#5A5A5A",relief=tk.RAISED,borderwidth=7)
name1.grid(row=0+1,column=2)

name2=tk.Label(root,textvariable=text_var2,font=("Arial", 25),fg="white",bg="#5A5A5A",relief=tk.RAISED,borderwidth=7)
name2.grid(row=1+1,column=2)

name3=tk.Label(root,textvariable=text_var3,font=("Arial", 25),fg="white",bg="#5A5A5A",relief=tk.RAISED,borderwidth=7)
name3.grid(row=2+1,column=2)

price_label1=tk.Label(root,textvariable=price_var1,font=("Arial", 25),fg="white",bg="#5A5A5A")
price_label1.grid(row=0+1,column=3)

price_label2=tk.Label(root,textvariable=price_var2,font=("Arial", 25),fg="white",bg="#5A5A5A")
price_label2.grid(row=1+1,column=3)

price_label3=tk.Label(root,textvariable=price_var3,font=("Arial", 25),fg="white",bg="#5A5A5A")
price_label3.grid(row=2+1,column=3)

#instr_label=tk.Label(root,text="Click on the image to redirect to the product page !",font=("Arial", 25))
#instr_label.grid(row=4,column=2)

name1.bind("<Button-1>", lambda event, url=url_to_open1: on_element_click(event, url))
name1.bind("<ButtonRelease-1>", on_element_release)

name2.bind("<Button-1>", lambda event, url=url_to_open2: on_element_click(event, url))
name2.bind("<ButtonRelease-1>", on_element_release)

name3.bind("<Button-1>", lambda event, url=url_to_open3: on_element_click(event, url))
name3.bind("<ButtonRelease-1>", on_element_release)



# Start the tkinter main loop
root.mainloop()
