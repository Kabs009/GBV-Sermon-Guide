import streamlit as st
# Import the module you created
import gbv_html
 
def display_html(html_content):
    st.markdown(html_content, unsafe_allow_html=True)


# Main app function
def main_app():
    st.title("GBV Basics")
    

    # Navigation buttons
    if st.button('Introduction to GBV'):
        st.header("Introduction to GBV")
        display_html(gbv_html.gbv_list(gbv_topic=1))
    

    elif st.button('Forms of GBV '):
        st.header('Forms of GBV')
        display_html(gbv_html.gbv_list(gbv_topic=2))

    
    elif st.button('Prevalence of GBV'):
        st.header('Prevalenc of GBV')
        display_html(gbv_html.gbv_list(gbv_topic=3))


    # A line for visual separation
    st.markdown("---")

# Run the main app function
main_app()
