import streamlit as st
import pandas as pd

# Load your CSV data
iphone_data = pd.read_csv('iphone_data.csv')
redmi_data = pd.read_csv('redmi_data.csv')
samsung_data = pd.read_csv('samsung_data.csv')
vivo_data = pd.read_csv('vivo_data.csv')
one_plus_data = pd.read_csv('one_plus_data.csv')

# Concatenate all dataframes into one
df = pd.concat([iphone_data, redmi_data, samsung_data, vivo_data, one_plus_data], ignore_index=True)

# Sample DataFrame with mobile product data for visualization
data = {
    'Brand': ['Samsung', 'OnePlus', 'Apple', 'Oppo', 'Realme', 'Vivo'],
    'Model': ['Galaxy S23', '11 5G', 'iPhone 13', 'Find N2 Flip', 'GT 2 Pro', 'X80 Pro'],
    'Rating': [4.5, 4.2, 4.8, 4.7, 4.5, 4.3],
    'Price': [44999, 56980, 51999, 54999, 49999, 47979],
    'Link': [
        'https://www.flipkart.com/samsung-galaxy-s23-5g-green-256-gb/p/itm6840743bfd1ef?pid=MOBGMFFXB7RGPNET&lid=LSTMOBGMFFXB7RGPNETJZGNDL&marketplace=FLIPKART&q=samsung+s23+5g&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_11_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_11_na_na_ps&fm=Search&iid=en_fSFU-tn3-gbtM8pL77AWFZUJsTUrqdmdWAkwpbw-OdOLzYF68o0Pg0mq1Af90e1NdOi-5iQ-i15gauqn8a1A2_UFjCTyOHoHZs-Z5_PS_w0%3D&ppt=pp&ppn=pp&ssid=4o6m86n5c00000001727905785010&qH=37068c103bda2953',
        'https://www.flipkart.com/oneplus-11-5g-eternal-green-128-gb/p/itm668119d115289?pid=MOBGMUGSSSJGKNDU&lid=LSTMOBGMUGSSSJGKNDUSVXRRD&marketplace=FLIPKART&q=one+plus+under+60000&store=tyy%2F4io&srno=s_1_4&otracker=search&otracker1=search&fm=Search&iid=097ded7a-9cf6-430f-acaa-f8e2d0fa83c9.MOBGMUGSSSJGKNDU.SEARCH&ppt=pp&ppn=pp&ssid=gjj42aoveo0000001727905728316&qH=9ee4166f3c5a048b',
        'https://www.flipkart.com/apple-iphone-13-blue-512-gb/p/itma26798ee418a6?pid=MOBG6VF5CBZ6EPF2&lid=LSTMOBG6VF5CBZ6EPF2UESEY3&marketplace=FLIPKART&q=iphone+13&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=8cd0b7c6-8025-448e-8a0e-8952069fc422.MOBG6VF5CBZ6EPF2.SEARCH&ppt=pp&ppn=pp&ssid=9zxxdglc000000001727905656396&qH=c68a3b83214bb235',
        'https://www.flipkart.com/oppo-find-n2-flip-astral-black-256-gb/p/itm8cfed9af48231?pid=MOBGN2NDWGYJTN8R&lid=LSTMOBGN2NDWGYJTN8RUXQVLH&marketplace=FLIPKART&q=oppo+under+60000&store=tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=search-autosuggest&iid=394350a8-f23b-447a-96ee-dd4ca5625dba.MOBGN2NDWGYJTN8R.SEARCH&ppt=pp&ppn=pp&ssid=10z76oo47k0000001727905397785&qH=a4325851ec25c271',
        'https://www.flipkart.com/realme-gt-2-pro-paper-green-128-gb/p/itm125e5a8c1de92?pid=MOBGCRYZJGW3UJWG&lid=LSTMOBGCRYZJGW3UJWGKRDEOJ&marketplace=FLIPKART&q=realme+mobile+under+60000&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_18_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_18_na_na_ps&fm=Search&iid=9b1e8834-1b09-40e1-99c6-35e70632ce5b.MOBGCRYZJGW3UJWG.SEARCH&ppt=sp&ppn=sp&ssid=s2bq5ynr4w0000001727905584364&qH=a3c70be5972ffc8c',
        'https://www.flipkart.com/vivo-x80-pro-cosmic-black-256-gb/p/itm91e0e7dd2d74d?pid=MOBGE89YSMWJV5PZ&lid=LSTMOBGE89YSMWJV5PZAEEDMK&marketplace=FLIPKART&q=vivio+under+50000&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=18d15ba9-8a75-4773-8e56-6cd6d617824b.MOBGE89YSMWJV5PZ.SEARCH&ppt=pp&ppn=pp&ssid=98epuclw5c0000001727905855099&qH=68774efa80147d3f'
        'https://www.flipkart.com/apple-iphone-14-starlight-256-gb/p/itmaeda15697bb79?pid=MOBGHWFHBJGZYRZC&lid=LSTMOBGHWFHBJGZYRZCUALABX&marketplace=FLIPKART&q=iphone+14&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_3_9_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_3_9_na_na_ps&fm=Search&iid=478b5fa0-a256-4dfd-be86-de0e61313b63.MOBGHWFHBJGZYRZC.SEARCH&ppt=pp&ppn=pp&ssid=y983o4cj3k0000001727935177170&qH=860f3715b8db08cd',
    ]
}

# Create a DataFrame for visualization
df_visual = pd.DataFrame(data)

# Streamlit Application
st.title("Mobile Product Recommendation from Flipkart")

# Sidebar for user input
st.sidebar.header("Select Brand")
brands = df_visual['Brand'].unique()
selected_brand = st.sidebar.selectbox("Choose a Brand", brands)

# Filter DataFrame based on the selected brand
recommended_products = df_visual[df_visual['Brand'] == selected_brand]

# Display recommended products
if not recommended_products.empty:
    st.subheader(f"Recommended Mobiles for {selected_brand}:")
    for index, row in recommended_products.iterrows():
        st.write(f"**Model:** {row['Model']}")
        st.write(f"**Rating:** {row['Rating']} ⭐")
        st.write(f"**Price:** ₹{row['Price']}")
        st.markdown(f"[View Product]({row['Link']})")  # Hyperlink to the Flipkart product page

    # Dashboard metrics
    avg_price = recommended_products['Price'].mean()
    avg_rating = recommended_products['Rating'].mean()

    st.subheader("Dashboard Metrics")
    st.write(f"**Average Price:** ₹{avg_price:.2f}")
    st.write(f"**Average Rating:** {avg_rating:.2f} ⭐")

    # Create a bar chart for visualization
    st.subheader("Price and Rating Comparison")
    st.bar_chart(recommended_products.set_index('Model')[['Price', 'Rating']])

else:
    st.write("No products found for the selected brand.")
