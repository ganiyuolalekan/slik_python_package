import streamlit as st

from slik_wrangler.loadfile import read_file
from slik_wrangler.dqa import data_cleanness_assessment


@st.cache
def collect_data(data):
    return read_file(data)


def main():
    st.write("""
    # Data Flow with Slik-Wrangler and Streamlit

    In this application, we'll see how the basic dataflow process with slik wrangler occurs.
    For quick reference, the dataflow process in slik is as follows:

    **Data Loading -> Data Quality Assessment -> Data Preprocessing -> Data Modelling**

    For this application though, we'll be taking the Data Loading and Data Quality Assessment flow 
    for the slik wrangler project.

    Let's start by uploading a file, which should exceed 200MB in size
    """)

    file_upload_help_text = """
    Upload a (single) data file of any of the extensions below:

    ['csv', 'xlsx', 'xs', 'parquet', 'json']

    The file will be read and display for data quality assessment
    """

    final_message = """
    The data quality assessment was carried, but the outputs were all displayed
    in the console where the application was ran.
    
    We would have to therefore build display packages to work with streamlit 
    if we hope to move forward, or is there another way???
    """

    data_file = st.text_input(
        label="Path to file to perform slik-wrangler flow",
        help=file_upload_help_text
    )

    if data_file is not None:
        if st.button("Read File"):
            dataframe = collect_data(data_file)
            st.write("### Your dataframe:", dataframe.head())
            st.write("After uploading the file you can assert it below")

    if data_file is not None:
        if st.button("Perform Quality Assessment"):
            dataframe = collect_data(data_file)
            st.write("### Your dataframe:")
            st.write(*data_cleanness_assessment(dataframe, return_as_str=True))


if __name__ == '__main__':
    main()

# With ❤️ Lekan

