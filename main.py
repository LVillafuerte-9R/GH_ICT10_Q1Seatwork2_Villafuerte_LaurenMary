from pyscript import display

# Variables with data types
restaurant_name = "Cinnamoroll Cafe"   # string
owner_name = "Lauren Mary Villafuerte"   # string
year_established = 1980   # integer
popular_item_price = 499.00   # float
has_delivery = True   # boolean
product_names = ["Cinnamoroll Cake", "Banana Cake", "Chicken Tenders"]   # list
business_hours = "10:00 AM - 11:00 PM"   # string
menu_prices = {   # dictionary
    "Cinnamoroll Cake": 499.00,
    "Banana Cake": 50.00,
    "Chicken Tenders": 150.00,
    "Iced Tea": 30.00,
    "Cinnamoroll Latte": 150.00
}
common_allergens = ["Peanuts", "Dairy", "Gluten"]   # list
tax_rate = 0.12   # float

# Display Restaurant Header
display(restaurant_name, target="restaurantName")
display(f"Owner: {owner_name}", target="ownerName")
display(f"Since {year_established}", target="yearEst")

# Populate Menu Table (append rows correctly)
for item, price in menu_prices.items():
    display(f"<tr><td>{item}</td><td>₱{price:.2f}</td></tr>", target="menuTable", append=True)

# Footer Info
display(f"Open: {business_hours}", target="businessHours")
delivery_text = "Delivery Available" if has_delivery else "No Delivery"
display(delivery_text, target="deliveryStatus")