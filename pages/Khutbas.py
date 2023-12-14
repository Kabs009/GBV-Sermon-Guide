import streamlit as st
# Import the module you created
import khutba_html
# Function to display HTML content
def display_html(html_content):
    st.markdown(html_content, unsafe_allow_html=True)


# Main app function
def main_app():
    st.title("Khutbas")
    

    # Navigation buttons
    if st.button('Divine Blueprint for Equality and Respect'):
        st.header("Divine Blueprint for Equality and Respect")
        display_html(khutba_html.khutba_list(khutba_number=1))
    

    elif st.button('Dangers of Unchecked Emotions: Lessons from Qabil and Habil '):
        st.header('Dangers of Unchecked Emotions: Lessons from Qabil and Habil')
        display_html(khutba_html.khutba_list(khutba_number=2))

    
    elif st.button('Confronting Sexual Violence: A Quranic Perspective'):
        st.header('Confronting Sexual Violence: A Quranic Perspective')
        display_html(khutba_html.khutba_list(khutba_number=3))


    # A line for visual separation
    st.markdown("---")

# Run the main app function
main_app()
