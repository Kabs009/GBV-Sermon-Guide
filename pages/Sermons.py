import streamlit as st
# Import the module you created
import html_files

# Function to display HTML content
def display_html(html_content):
    st.markdown(html_content, unsafe_allow_html=True)


# Main app function
def main_app():
    st.title("Sermons")
    

    # Navigation buttons
    if st.button('Divine Blueprint for Equality and Respect'):
        st.header("Divine Blueprint for Equality and Respect")
        display_html(html_files.sermon_list(sermon_number=1))
    

    elif st.button('Dangers of Unchecked Emotions: Lessons from Cain and Abel'):
        st.header('Dangers of Unchecked Emotions: Lessons from Cain and Abel')
        display_html(html_files.sermon_list(sermon_number=2))

    elif st.button('God Sees and Cares for the Oppressed: Lessons from Hagar'):
        st.header('God Sees and Cares for the Oppressed: Lessons from Hagar')
        display_html(html_files.sermon_list(sermon_number=3))


    # A line for visual separation
    st.markdown("---")

# Run the main app function
main_app()
