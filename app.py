import streamlit as st
from multiapp import MultiApp
from apps import mainwindow , Dash # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("main window", mainwindow.app)
app.add_app("Dashbord", Dash.app)

# The main app
app.run()