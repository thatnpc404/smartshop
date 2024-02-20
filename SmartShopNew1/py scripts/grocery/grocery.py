import pandas as pd 
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser


f_groc_data=pd.read_excel('C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\flip_grocery_data.xlsx',nrows=4)
f_groc_data['Price']=pd.to_numeric(f_groc_data['Price'].apply(lambda x:x[1:]))
f_groc_data=f_groc_data.sort_values('Price')
best_val_f_groc=f_groc_data.head(1).values


dmart_data=pd.read_excel('C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\dmart_data.xlsx',nrows=4)
dmart_data['Price']=pd.to_numeric(dmart_data['Price'])
dmart_data=dmart_data.sort_values('Price')
best_val_dmart_data=dmart_data.head(1).values



jio_data=pd.read_excel('C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\jiomart_data.xlsx',nrows=4)
jio_data['Price']=pd.to_numeric(jio_data['Price'].apply(lambda x:x[1:-3]))
jio_data=jio_data.sort_values('Price')
best_val_jio=jio_data.head(1).values

website=["Flipkart Grocery","Dmart","JioMart"]
pricing=[best_val_f_groc[0][2],best_val_dmart_data[0][2],best_val_jio[0][2]]
prod_name=[best_val_f_groc[0][0],best_val_dmart_data[0][0],best_val_jio[0][0]]
url=[best_val_f_groc[0][1],best_val_dmart_data[0][1],best_val_jio[0][1]]
re_url=[best_val_f_groc[0][1],"https://www.dmart.in/search?searchTerm="+best_val_dmart_data[0][0],best_val_jio[0][1]]
merged=pd.DataFrame(
    {
        'Website':website,
        'Product Name':prod_name,
        'Price':pricing,
        'Url':re_url

    }
)

merged=merged.sort_values("Price")

#UI code

if merged["Website"].head(1).values=="Flipkart Grocery" and merged["Website"].iloc[1]=="Dmart":
    img_name1="flipkart_grocery.png"
    img_name2="dmart_logo1.png"
    img_name3="jiomart_logo.png"
    prod_name1=merged["Product Name"].iloc[0]
    prod_name2=merged["Product Name"].iloc[1]
    prod_name3=merged["Product Name"].iloc[2]
    price1=merged["Price"].iloc[0]
    price2=merged["Price"].iloc[1]
    price3=merged["Price"].iloc[2]

elif merged["Website"].head(1).values=="Flipkart Grocery" and merged["Website"].iloc[1]=="JioMart":
    img_name1="flipkart_grocery.png"
    img_name2="jiomart_logo.png"
    img_name3="dmart_logo1.png"
    prod_name1=merged["Product Name"].iloc[0]
    prod_name2=merged["Product Name"].iloc[1]
    prod_name3=merged["Product Name"].iloc[2]
    price1=merged["Price"].iloc[0]
    price2=merged["Price"].iloc[1]
    price3=merged["Price"].iloc[2]

elif merged["Website"].head(1).values=="Dmart" and merged["Website"].iloc[1]=="JioMart":
    img_name1="dmart_logo1.png"
    img_name2="jiomart_logo.png"
    img_name3="flipkart_grocery.png"
    prod_name1=merged["Product Name"].iloc[0]
    prod_name2=merged["Product Name"].iloc[1]
    prod_name3=merged["Product Name"].iloc[2]
    price1=merged["Price"].iloc[0]
    price2=merged["Price"].iloc[1]
    price3=merged["Price"].iloc[2]

elif merged["Website"].head(1).values=="Dmart" and merged["Website"].iloc[1]=="Flipkart Grocery":
    img_name1="dmart_logo1.png"
    img_name2="flipkart_grocery.png"
    img_name3="jiomart_logo.png"
    prod_name1=merged["Product Name"].iloc[0]
    prod_name2=merged["Product Name"].iloc[1]
    prod_name3=merged["Product Name"].iloc[2]
    price1=merged["Price"].iloc[0]
    price2=merged["Price"].iloc[1]
    price3=merged["Price"].iloc[2]

elif merged["Website"].head(1).values=="JioMart" and merged["Website"].iloc[1]=="Flipkart Grocery":
    img_name1="jiomart_logo.png"
    img_name2="flipkart_grocery.png"
    img_name3="dmart_logo1.png"
    prod_name1=merged["Product Name"].iloc[0]
    prod_name2=merged["Product Name"].iloc[1]
    prod_name3=merged["Product Name"].iloc[2]
    price1=merged["Price"].iloc[0]
    price2=merged["Price"].iloc[1]
    price3=merged["Price"].iloc[2]

elif merged["Website"].head(1).values=="JioMart" and merged["Website"].iloc[1]=="Dmart":
    img_name1="jiomart_logo.png"
    img_name2="dmart_logo1.png"
    img_name3="flipkart_grocery.png"
    prod_name1=merged["Product Name"].iloc[0]
    prod_name2=merged["Product Name"].iloc[1]
    prod_name3=merged["Product Name"].iloc[2]
    price1=merged["Price"].iloc[0]
    price2=merged["Price"].iloc[1]
    price3=merged["Price"].iloc[2]

'''

def move_text():
    # Get the current x-coordinate of the text
    x1, _ = canvas.coords(text_id)
    
    # Move the text 5 pixels to the right
    canvas.move(text_id, 5, 0)
    
    # If the text has moved off the canvas, reset its position to the starting point
    if x1 >= canvas.winfo_width():
        canvas.coords(text_id, 10, 50)  # Set the initial position
    
    canvas.after(50, move_text) 

def open_url(url):
    webbrowser.open(url)
img_path1="C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\py scripts\\grocery\\"+img_name1
img_path2="C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\py scripts\\grocery\\"+img_name2
img_path3="C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\py scripts\\grocery\\"+img_name3


# Create the main application window
root = tk.Tk()

root.title("Clothing : SmartShop")
root.geometry("700x350")

canvas = tk.Canvas(root, width=400, height=100)
canvas.grid(row=0,column=2)
text_id = canvas.create_text(10, 50, text="SmartShop (4934 & 4935)", anchor="w", font=("Arial", 20))

move_text()  # Start the text animation

# Load the image using PIL
image = Image.open(img_path1)
image = image.resize((300, 200))  # Resize the image to your desired size
image = ImageTk.PhotoImage(image)

image1 = Image.open(img_path2)
image1 = image1.resize((300, 200))  # Resize the image to your desired size
image1 = ImageTk.PhotoImage(image1)

image2= Image.open(img_path3)
image2 = image2.resize((300, 200))  # Resize the image to your desired size
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


name1=tk.Label(root,textvariable=text_var1,font=("Arial", 25))
name1.grid(row=0+1,column=2)

name2=tk.Label(root,textvariable=text_var2,font=("Arial", 25))
name2.grid(row=1+1,column=2)

name3=tk.Label(root,textvariable=text_var3,font=("Arial", 25))
name3.grid(row=2+1,column=2)

price_label1=tk.Label(root,textvariable=price_var1,font=("Arial", 25))
price_label1.grid(row=0+1,column=3)

price_label2=tk.Label(root,textvariable=price_var2,font=("Arial", 25))
price_label2.grid(row=1+1,column=3)

price_label3=tk.Label(root,textvariable=price_var3,font=("Arial", 25))
price_label3.grid(row=2+1,column=3)

instr_label=tk.Label(root,text="Click on the image to redirect to the product page !",font=("Arial", 25))
instr_label.grid(row=4,column=2)

# Start the tkinter main loop
root.mainloop()

'''

def on_element_click(event, url):
    # Change the background color (or any other effect) when clicked
    event.widget.configure(bg="lightblue")
    open_url(url)
    # You can add more effects here

def on_element_release(event):
    # Change the background color (or other effects) back to the original when released
    event.widget.configure(bg="#5A5A5A")
    # You can reset other effects here

def open_url(url):
    webbrowser.open(url)

img_path1="C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\py scripts\\grocery\\"+img_name1
img_path2="C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\py scripts\\grocery\\"+img_name2
img_path3="C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\py scripts\\grocery\\"+img_name3


# Create the main application window
root = tk.Tk()

root.title("Electronics : SmartShop")
# root.geometry("1920x1080")
root.attributes('-fullscreen',True)

#background image

img = Image.open('C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\py scripts\\grocery\\background.jpg')
img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

# Create a label for the image
img_label = tk.Label(root, image=img)
img_label.place(x=0, y=0, relwidth=1, relheight=1) 


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