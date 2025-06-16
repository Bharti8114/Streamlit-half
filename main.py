import streamlit as st
st.title("Title-> Good Morning")
st.header("Header-> Good Morning")
st.subheader("Subheader-> Good Morning")
st.text("Text-> Good Morning")

st.markdown("# Hii")
st.markdown("## Hii")
st.markdown("### Hii")
st.markdown("#### Hii")
st.markdown("##### Hii")
st.markdown("###### Hii")
st.markdown("Hii")


st.success("Data is Submitted")
st.info("Data is Submitted")
st.warning("Warning!")
st.error("Error")

exp = ZeroDivisionError("Zero Division Not possible")
st.exception(exp)
st.exception(ZeroDivisionError("Zero Division Not possible"))

st.write("range(1,10)")
st.write(range(1,10))         # not a string
st.write("1+2+3")
st.write(1+2+3)
st.write(1*2+3)

st.code("x =10 \n"
        "for i in range(x):\n"
        "   print(i)")

st.checkbox("Male")       # checkbox
st.checkbox("Female")

if(st.checkbox("Adult")):                        # checkbox with validation
    st.write("You're an Adult")


st.radio("select: ",("Check","Uncheck"))
st.radio("Select: ",("Male","Female","Other"))

st.subheader("Select Box")
st.selectbox("Data Science: ",["Data analysis","Web Scraping",
                               "Machine Learning","Deep Learning",
                               "Natural Language Processing",
                               "Computer Vision","Image Processing"])     # single select

st.subheader("MultiSelect Box")
multiSelBox = st.multiselect("Data Science: ",["Data analysis","Web Scraping",
                               "Machine Learning","Deep Learning",
                               "Natural Language Processing",
                               "Computer Vision","Image Processing"])      # multiple select options
st.write("You have Selected : ", len(multiSelBox),"Courses")

st.subheader("Button")
st.button("Select")


st.subheader("Slider")
st.slider("Select the Level",1,10,step=1)

# taking input from user
st.subheader("Text Input")
username = st.text_input("Enter Your Name: ")
if(username):
    st.write(f"Hello {username}")

user_name = st.text_input("Username: ")
password = st.text_input("Password : ", type = "password")


st.subheader("Text Area")
st.text_area("Write about yourself in 100 words", height = 100)     # height use for words limit


st.subheader("Age")
st.number_input("Select your age",18,100)

st.subheader("Input Date")
st.date_input("select your DOB")

st.subheader("Input Time")
st.time_input("Enter time")
