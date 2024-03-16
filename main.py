import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Semester Ticket Validity Checker by ofurkancoban",
    page_icon="🐼"
)

def add_hover_effects():
    st.markdown("""
        <style>
            a img { 
                transition: transform 0.2s ease; /* Smooth transition */
            }
            a img:hover {
                transform: scale(2); /* Slightly enlarge the icon */
                opacity: 0.7; /* Make the icon a bit transparent */
            }
        </style>
        """, unsafe_allow_html=True)

# Apply the custom CSS for hover effects
add_hover_effects()
def add_title_hover_effect():
    st.markdown("""
        <style>
            /* Custom style for the main title with class 'title-hover' */
            .title-hover{
                 transition: transform 0.2s ease; /* Smooth transition */
            }
            .title-hover:hover {
                transform: scale(1.3); /* Slightly enlarge the icon */
                opacity: 0.7; /* Make the icon a bit transparent */
            }
        </style>
        """, unsafe_allow_html=True)

# Apply the custom CSS for hover effects
add_title_hover_effect()


# Custom CSS to inject larger fonts
def set_font(font_name):
    st.markdown(f"""
    <style>
        html, body, [class*="st-"] {{
            font-family: '{font_name}', sans-serif;
        }}
        h1 {{
            text-align: center;
        }}
    </style>
    """, unsafe_allow_html=True)
# Set font for entire app
set_font("Helvetica")



# Initialize Streamlit application
st.markdown('<div style="text-align: center;font-size:230%;margin-bottom: 0px"><b>🚆🚍</b></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;font-size:230%;margin-bottom: 40px"><b>Semester Ticket Validity Checker</b></div>', unsafe_allow_html=True)



# Load the dataset
dataset_path = 'semester_ticket_dataset.csv'  # Adjust the path as necessary
data = pd.read_csv(dataset_path, delimiter=';')

# Create a list of unique stops for the selectbox options
stops = data['Stop'].unique().tolist()

# Selectbox for choosing the starting city
from_city = st.selectbox('From:', stops, index=8)

# Selectbox for choosing the destination city
to_city = st.selectbox('To:', stops, index=11)

# Button to check the ticket validity
if st.button('Check Ticket Validity',use_container_width=True, type="primary" ):
    # Infer routes and implement the logic based on the selected cities
    from_valid = data[data['Stop'] == from_city]['Valid'].iloc[0]
    to_valid = data[data['Stop'] == to_city]['Valid'].iloc[0]

    # Check if ticket is valid for both selected stops
    if from_valid and to_valid:
        st.success(f'✅ Your semester ticket is valid for travel from {from_city} to {to_city}. ✅')

        # Public transportation validity at the destination
        public_transport_destination = data[data['Stop'] == to_city]['Public_Transportation_Valid'].iloc[0]
        if public_transport_destination:
            st.info(f"❕ You also can use Public Transportation (Tram, Bus) in {to_city}. ❕")

        # IC train usage check
        valid_ic_route_from = data[data['Stop'] == from_city]['Valid_IC_route'].iloc[0]
        valid_ic_route_to = data[data['Stop'] == to_city]['Valid_IC_route'].iloc[0]
        if valid_ic_route_from and valid_ic_route_to:
            st.warning("❗️ You also can use IC trains only between Bremen Hbf and Norddeich Mole. ❗️")

        # Last accessible stop message
        last_accessible_destination = data[data['Stop'] == to_city]['Last_Accessible'].iloc[0]
        if last_accessible_destination:
            st.error(f"⛔️ This stop is the last accessible stop with your semester ticket in this route. ⛔️")
    else:
        st.error('Your semester ticket is not valid for this route.')
st.markdown('___________')
st.image('map.jpg')
st.markdown('___________')
# Creating three columns at the bottom of the page
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
with col1:
    st.link_button("Github", "https://github.com/ofurkancoban",use_container_width=True,type="primary")

with col2:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/ofurkancoban",use_container_width=True,type="primary")
with col3:
    st.link_button("Kaggle", "https://www.kaggle.com/ofurkancoban",use_container_width=True, type="primary")
with col5:
    st.markdown('Created by @ofurkancoban')