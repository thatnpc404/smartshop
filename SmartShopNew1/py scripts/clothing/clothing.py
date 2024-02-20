import pandas as pd 
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser


myn_data=pd.read_excel('C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\myntra_data.xlsx',nrows=4)
myn_data['Price']=pd.to_numeric(myn_data['Price'].apply(lambda x:x.split()[1]))
myn_data=myn_data.sort_values('Price')
best_val_myn=myn_data.head(1).values

ajio_data=pd.read_excel('C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\ajio_data.xlsx',nrows=4)
ajio_data['Price']=ajio_data['Price'].apply(lambda x:x.replace("₹",""))
ajio_data['Price']=ajio_data['Price'].apply(lambda x:x.replace(",",""))
ajio_data['Price']=pd.to_numeric(ajio_data['Price'])
ajio_data=ajio_data.sort_values('Price')
best_val_ajio=ajio_data.head(1).values

website=["Myntra","AJIO"]
prod_name=[best_val_myn[0][0],best_val_ajio[0][0]]
url=[best_val_myn[0][1],best_val_ajio[0][1]]
pricing=[best_val_myn[0][2],best_val_ajio[0][2]]

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

if merged["Website"].head(1).values=="Myntra":
    img_name1="myntra_logo.png"
    img_name2="AJIO_logo.png"
    prod_name1=best_val_myn[0][0]
    prod_name2=best_val_ajio[0][0]
    price1=best_val_myn[0][2]
    price2=best_val_ajio[0][2]
else:
    img_name1="AJIO_logo.png"
    img_name2="myntra_logo.png"
    prod_name2=best_val_myn[0][0]
    prod_name1=best_val_ajio[0][0]
    price2=best_val_myn[0][2]
    price1=best_val_ajio[0][2]


def open_url(url):
    webbrowser.open(url)

def on_element_click(event, url):
    # Change the background color (or any other effect) when clicked
    event.widget.configure(bg="lightblue")
    open_url(url)
    # You can add more effects here

def on_element_release(event):
    # Change the background color (or other effects) back to the original when released
    event.widget.configure(bg="#5A5A5A")
    # You can reset other effects here
# Create the main application window
root = tk.Tk()

root.title("Electronics : SmartShop")
# root.geometry("1920x1080")
root.attributes('-fullscreen',True)

#background image

img = Image.open('C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\py scripts\\clothing\\background.jpg')
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

img_path1="C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\py scripts\\clothing\\"+img_name1
img_path2="C:\\Users\\shrey\\OneDrive\\Documents\\UiPath\\SmartShopNew1\\py scripts\\clothing\\"+img_name2


# Load the image using PIL
image = Image.open(img_path1)
image = image.resize((400, 150))  # Resize the image to your desired size
image = ImageTk.PhotoImage(image)

image1 = Image.open(img_path2)
image1 = image1.resize((400, 130))  # Resize the image to your desired size
image1 = ImageTk.PhotoImage(image1)


# Create a label to display the image
image_label = tk.Label(root, image=image)
image_label1 = tk.Label(root, image=image1)


# Define the URL you want to open when the image is clicked
url_to_open1 = merged["Url"].head(1).values[0]  # Replace with your desired URL
url_to_open2 = merged["Url"].iloc[1]  # Replace with your desired URL


# Bind a click event to the label to open the URL
image_label.bind("<Button-1>", lambda event: open_url(url_to_open1))
image_label1.bind("<Button-1>", lambda event: open_url(url_to_open2))



image_label.configure(bg="#09090c")
image_label1.configure(bg="#09090c")

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



text_var1 = tk.StringVar()
text_var2 = tk.StringVar()
text_var3=  tk.StringVar()


text_var1.set(prod_name1)
text_var2.set(prod_name2)


price_var1 = tk.StringVar()
price_var2 = tk.StringVar()
price_var3 = tk.StringVar()

price_var1.set("₹"+str(price1))
price_var2.set("₹"+str(price2))


name1=tk.Label(root,textvariable=text_var1,font=("Arial", 25),fg="white",bg="#5A5A5A",relief=tk.RAISED,borderwidth=7)
name1.grid(row=0+1,column=2)

name2=tk.Label(root,textvariable=text_var2,font=("Arial", 25),fg="white",bg="#5A5A5A",relief=tk.RAISED,borderwidth=7)
name2.grid(row=1+1,column=2)



price_label1=tk.Label(root,textvariable=price_var1,font=("Arial", 25),fg="white",bg="#5A5A5A")
price_label1.grid(row=0+1,column=3)

price_label2=tk.Label(root,textvariable=price_var2,font=("Arial", 25),fg="white",bg="#5A5A5A")
price_label2.grid(row=1+1,column=3)



#instr_label=tk.Label(root,text="Click on the image to redirect to the product page !",font=("Arial", 25))
#instr_label.grid(row=4,column=2)

name1.bind("<Button-1>", lambda event, url=url_to_open1: on_element_click(event, url))
name1.bind("<ButtonRelease-1>", on_element_release)

name2.bind("<Button-1>", lambda event, url=url_to_open2: on_element_click(event, url))
name2.bind("<ButtonRelease-1>", on_element_release)




# Start the tkinter main loop
root.mainloop()
