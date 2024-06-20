import pickle
import streamlit as st
import base64

# Load the trained model
with open('classifier.pkl', 'rb') as model_file:
    classifier = pickle.load(model_file)

# Define the add_bg_from_local function with width and height parameters
def add_bg_from_local(image_file, width, height):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('data:image/png;base64,{encoded_string.decode()}');
            background-size: {width} {height};
        }}
        .white-text {{
            color: white;
        }}
        .white-title {{
            color: white;
        }}
        .large-text {{
            font-size: 45px; 
        }}
        .small-text {{
            font-size: 20px; 
        }}
        .bold-text {{
            font-weight: bold;
        }}
        .label {{
            color: white; 
        }}
        .med-text {{
            font-size: 25px; 
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the add_bg_from_local function with the desired width and height
add_bg_from_local('home1.png', '1280px', '700px') 

# Define the Streamlit app
def main():
    # Check if the "Validate Note" button was clicked to navigate to the second page
    if "page" in st.session_state and st.session_state.page == "second":
        second_page()
    else:
        # Button with a custom class for positioning
        if st.button("Validate Note", key="validate_button"):
            st.session_state.page = "second"

# Define the second page
def second_page():
    # Change the background for the second page to 'main2.png'
    add_bg_from_local('MA3.png', '1280px', '700px')

    # Change the text color, font size, and make it bold for "Bank Note Authentication"
    st.markdown('<div class="large-text white-title bold-text">Bank Note Authentication</div>', unsafe_allow_html=True)

    # Increase the font size for text on the second page
    st.markdown('<div class="small-text white-text">Enter the features for bank note authentication:</div>', unsafe_allow_html=True)

    st.markdown('<div class="label">Variance:</div>', unsafe_allow_html=True)
    variance = st.number_input("", key="variance_input")

    st.markdown('<div class="label">Skewness:</div>', unsafe_allow_html=True)
    skewness = st.number_input("", key="skewness_input")

    st.markdown('<div class="label">Curtosis:</div>', unsafe_allow_html=True)
    curtosis = st.number_input("", key="curtosis_input")

    st.markdown('<div class="label">Entropy:</div>', unsafe_allow_html=True)
    entropy = st.number_input("", key="entropy_input")

    if st.button("Predict"):
        data = [[variance, skewness, curtosis, entropy]]
        prediction = classifier.predict(data)
        result = "The Note is Authentic." if prediction[0] == 1 else "The Note is Unauthentic."

        # Play different audio files based on the prediction
        if prediction[0] == 1:
            st.audio("AU.mp3")
        else:
            st.audio("UNAU.mp3")

        # Display the prediction result
        st.markdown(f'<div class="med-text white-text">Prediction: {result}</div>', unsafe_allow_html=True)

    if st.button("Back to Main Page"):
        st.session_state.page = "main"

if __name__ == "__main__":
    main()