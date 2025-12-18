import tkinter as tk
from tkinter import messagebox

# AGRI WASTE DATABASE

AGRI_WASTE_DB = {
    "🌾 Rice Straw": {
        "uses": ["Cattle Feed", "Biofuel", "Organic Compost"],
        "price": 3000
    },
    "🌿 Wheat Straw": {
        "uses": ["Animal Bedding", "Paper Making", "Compost"],
        "price": 2500
    },
    "🍬 Sugarcane Bagasse": {
        "uses": ["Bio Energy", "Eco Packaging", "Paper Industry"],
        "price": 4000
    },
    "🥥 Coconut Husk": {
        "uses": ["Coir Fiber", "Rope Making", "Mulching"],
        "price": 3500
    },
    "🍌 Banana Stem": {
        "uses": ["Fiber Extraction", "Organic Manure"],
        "price": 2800
    }
}

# CALCULATION FUNCTION

def calculate_profit():
    waste = waste_var.get()
    qty = quantity_entry.get()

    if waste == "Select Waste":
        messagebox.showerror("Error", "Please select a waste type")
        return

    try:
        qty = float(qty)
        if qty <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid quantity")
        return

    data = AGRI_WASTE_DB[waste]
    total_profit = qty * data["price"]
    uses_text = "\n".join(data["uses"])

    result_label.config(
        text=f"""
Waste Type      : {waste}
Quantity        : {qty} tons

Possible Uses:
{uses_text}

Price per ton   : ₹{data['price']}
Estimated Profit: ₹{total_profit}
""",
        bg="#E8F5E9",
        fg="black"
    )

# GUI SETUP

root = tk.Tk()
root.title("Agri Waste Profit Estimator")
root.geometry("460x520")
root.resizable(False, False)

# Window background
root.configure(bg="lightgreen") 
# TITLE

title = tk.Label(
    root,
    text="🌾 Agri Waste Profit Estimator 🌾",
    font=("Arial", 16, "bold"),
    bg="#E8F5E9",
    fg="#2E7D32"
)
title.pack(pady=12)

# WASTE SELECTION

tk.Label(
    root,
    text="Select Waste Type:",
    font=("Arial", 11),
    bg="#E8F5E9"
).pack()

waste_var = tk.StringVar()
waste_var.set("Select Waste")

waste_menu = tk.OptionMenu(root, waste_var, *AGRI_WASTE_DB.keys())
waste_menu.config(
    bg="#A5D6A7",
    fg="black",
    font=("Arial", 10, "bold"),
    width=25
)
waste_menu["menu"].config(
    bg="#E8F5E9",
    fg="darkgreen"
)
waste_menu.pack(pady=6)

# QUANTITY INPUT

tk.Label(
    root,
    text="Enter Quantity (in tons):",
    font=("Arial", 11),
    bg="white"
).pack()

quantity_entry = tk.Entry(root, width=20)
quantity_entry.pack(pady=6)

# BUTTON

tk.Button(
    root,
    text="Calculate Profit",
    command=calculate_profit,
    bg="#2E7D32",
    fg="white",
    font=("Arial", 11, "bold"),
    width=18
).pack(pady=10)

# RESULT DISPLAY

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 10),
    justify="left",
    bg="White"
)
result_label.pack(pady=10)

# RUN APPLICATION

root.mainloop()
