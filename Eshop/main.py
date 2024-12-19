import requests
import streamlit as st

# Set page configuration
st.set_page_config(page_title="E-Shop", page_icon=":shopping_bags:", layout="wide")

# Define functions
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(style):
    try:
        with open(style) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Could not load CSS file: {style}")

local_css("style.css")

def set_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #008000; 
        }
        .header-bar {
            background-color: #007000; 
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 40px;
            font-weight: bold;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .section {
            background-color: #90EE90; 
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def display_products(products):
    cols = st.columns(4)
    for (product, details), col in zip(products.items(), cols):
        col.image(details["image"], use_column_width=True)
        col.title(product)
        col.write(f"Starting from {details['price']}")

def main():
    set_custom_css()

    # Header bar with E-Shop title and icon
    st.markdown(
        """
        <div class="header-bar">
            E-SHOP
            <img src="https://emojipedia-us.s3.amazonaws.com/source/skype/289/shopping-bags_1f6cd-fe0f.png" width="100"/>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Main content sections

    # Header section
    with st.container():
        st.title("Welcome to E-Shop")
        st.write("Discover a world of endless possibilities at our e-shop, where quality meets convenience. Browse, click, and indulge in seamless online shopping from the comfort of your home.")

    # Mobile Phones and Accessories section
    with st.container():
        st.header("Mobile Phones And Accessories")

        products = {
            "iPhone 15 Pro": {
                "price": "$999",
                "image": "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch_AV2_GEO_EMEA?wid=2560&hei=1440&fmt=p-jpg&qlt=80&.v=1693009275424"
            },
            "iPhone 15 Pro Max": {
                "price": "$1199",
                "image": "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-7inch_AV1?wid=2560&hei=1440&fmt=p-jpg&qlt=80&.v=1693009278581"
            },
            "iPhone 14": {
                "price": "$899",
                "image": "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone-14-finish-select-202209-6-1inch_GEO_EMEA?wid=2560&hei=1440&fmt"
                },
            "iPhone 14 Plus": {
                "price": "$1099",
                "image": "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone-14-finish-select-202209-6-7inch_AV1?wid=2560&hei=1440&fmt=p-jpg&qlt=80&.v=1671474798353"
            }
        }

        display_products(products)

    # Laptop & Desktop section
    with st.container():
        st.header("Laptops And Accessories")

        products = {
            "MacBook Pro 16-inch": {
                "price": "$2399",
                "image": "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/mbp16-spaceblack-gallery2-202310?wid=4000&hei=3074&fmt=jpeg&qlt=90&.v=1698156921319"
            },
            "MacBook Air 13-inch": {
                "price": "$1600",
                "image": "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/mba13-m3-midnight-gallery1-202402?wid=4000&hei=3074&fmt=jpeg&qlt=90&.v=1707262727684"
            },
            "Mac Pro": {
                "price": "$3500",
                "image": "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/mac-pro-tower-2023-gallery3?wid=4000&hei=3074&fmt=jpeg&qlt=90&.v=1684192597214"
            },
            "iMac": {
                "price": "$1800",
                "image": "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/imac-24-touch-id-blue-gallery-2?wid=4000&hei=3074&fmt=jpeg&qlt=90&.v=1697304406001"
            }
        }

        display_products(products)

    # Contact section
    # Contact section
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")

        with st.form("contact_form"):
            st.write("Please fill out the form to get in touch with me.")
            name = st.text_input("Your name", placeholder="ABC")
            email = st.text_input("Your email", placeholder="ABC@gmail.com")
            message = st.text_area("Your message", placeholder="Type your message here")

            submitted = st.form_submit_button("Send")

            if submitted:
                st.write("Form submitted successfully!")
            # You can add code here to send the form data to your email or database
            # For example, you can use the requests library to send a POST request to your email service
            # import requests
            # response = requests.post("https://formsubmit.co/5ed42bc4-bb29-41d7-9c73-92cd28bb137f", data={"name": name, "email": email, "message": message})
            # if response.status_code == 200:
            #     st.write("Form submitted successfully!")
            # else:
            #     st.write("Error submitting form. Please try again.")

if __name__ == "__main__":
    main()