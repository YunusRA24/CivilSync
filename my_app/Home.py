import streamlit as st

# Set page title and layout
st.set_page_config(page_title="CivilSync", page_icon="🌎", layout="wide")

# Custom CSS (keeping your existing CSS)
st.markdown(
    """
    <style>
        /* Correct background color */
        body {
            background-color: #e5dcc3;
            color: #333333;
            font-family: "Arial", sans-serif;
        }
        [data-testid="stAppViewContainer"] {
            background-color: #e5dcc3;
        }
        [data-testid="stHeader"] {
            background-color: #e5dcc3;
        }
        [data-testid="stToolbar"] {
            display: none;
        }

        /* Navigation Bar Styling - Moved Up Even More */
        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 5px 30px; /* Reduced padding to move up */
            background-color: #f0e6d2;
            border-bottom: 1px solid #d6cdb7;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            width: 100%;
            box-sizing: border-box;
            margin-top: -50px; /* Moves header further up */
        }

        .logo-container {
            display: flex;
            align-items: center;
        }

        .logo-circle {
            width: 50px; /* Increased size */
            height: 50px; /* Increased size */
            background-color: #e8c39e;
            border-radius: 50%;
            margin-right: 15px;
        }

        .company-name {
            font-size: 2.5rem; /* Increased font size */
            font-weight: bold;
            color: #8d7b68;
            font-family: "Georgia", serif;
        }

        .nav-menu {
            display: flex;
            align-items: center;
        }

        .nav-item {
            margin: 0 15px;
            color: #8d7b68;
            font-weight: 500;
            text-decoration: none;
            font-size: 1.5rem; /* Increased font size */
            transition: color 0.3s ease;
            cursor: pointer; /* Make it clickable */
        }

        .nav-item:hover {
            color: #5c4f3f;
        }
        
        /* Hide Streamlit buttons */
        .results-button-container {
            display: inline-block;
        }
        
        .results-button-container [data-testid="stHorizontalBlock"] {
            gap: 0 !important;
        }
        
        .results-button-container button {
            background: none !important;
            border: none !important;
            padding: 0 !important;
            color: #8d7b68 !important;
            font-size: 1.5rem !important;
            font-weight: 500 !important;
            font-family: "Arial", sans-serif !important;
            cursor: pointer !important;
        }
        
        .results-button-container button:hover {
            color: #5c4f3f !important;
        }
        
        /* Hide button outer container styling */
        .results-button-container [data-testid="element-container"] {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        .results-button-container .stButton {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        .results-button-container div[data-testid="stVerticalBlock"] {
            gap: 0 !important;
        }

        .login-button {
            background-color: #e8c39e;
            color: #8d7b68;
            padding: 12px 30px; /* Increased padding */
            border-radius: 20px;
            font-weight: bold;
            text-align: center;
            margin-left: 15px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            font-size: 1.5rem; /* Increased font size */
        }

        .login-button:hover {
            background-color: #d8b38e;
        }

        /* Hero Section */
        .hero {
            background-image: url('https://images.unsplash.com/photo-1580137189272-c9379f8864fd?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80');
            background-size: cover;
            background-position: center;
            height: 400px;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: white;
            margin-bottom: 40px;
            margin-top: 20px; /* Added space between header and hero section */
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }

        .hero-content {
            background-color: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 10px;
        }

        .hero-title {
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .hero-subtitle {
            font-size: 24px;
            font-style: italic;
        }

        /* Title and Motto */
        .title {
            font-size: 72px; /* Increased font size */
            font-weight: bold;
            text-align: center;
            color: #333333;
            opacity: 0;
            animation: fadeIn 1s ease-out forwards;
            margin-top: 5px; /* Reduced margin to move up */
        }
        .motto {
            font-size: 32px; /* Increased font size */
            text-align: center;
            font-style: italic;
            color: #555555;
            margin-bottom: 10px; /* Reduced margin to move up */
            opacity: 0;
            animation: fadeIn 1s ease-out forwards;
            animation-delay: 0.3s;
        }
        .intro-text {
            font-size: 32px; /* Increased font size */
            text-align: center;
            color: #333333;
            margin-bottom: 10px; /* Reduced margin to move up */
            opacity: 0;
            animation: fadeIn 1s ease-out forwards;
            animation-delay: 0.6s;
        }

        /* Features Section */
        .features {
            display: flex;
            justify-content: space-around;
            margin: 40px 0;
        }

        .feature-card {
            background-color: #f0e6d2;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            width: 30%;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
        }

        .feature-icon {
            width: 80px;
            height: 80px;
            margin-bottom: 10px;
        }

        .feature-title {
            font-size: 24px;
            font-weight: bold;
            color: #5c4f3f;
            margin-bottom: 10px;
        }

        .feature-description {
            font-size: 18px;
            color: #333333;
        }

        /* Footer */
        .footer {
            background-color: #f0e6d2;
            padding: 20px;
            text-align: center;
            border-top: 1px solid #d6cdb7;
            margin-top: 40px; /* Adjusted margin to match header spacing */
            margin-bottom: 20px; /* Added margin to create space at the bottom */
        }

        .footer a {
            color: #8d7b68;
            text-decoration: none;
            margin: 0 10px;
            font-size: 16px;
            transition: color 0.3s ease;
        }

        .footer a:hover {
            color: #5c4f3f;
        }

        /* Fully Centered Button */
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 10px; /* Reduced margin to move up */
            opacity: 0;
            animation: fadeIn 1s ease-out forwards;
            animation-delay: 0.9s;
            width: 100%; /* Ensure full width */
        }

        /* Update button styling to blue */
        .stButton>button {
            font-size: 20px !important; /* Reduced font size */
            padding: 10px 25px !important; /* Adjusted padding */
            background-color: #4267B2 !important; /* Changed to a Facebook-like blue */
            color: white !important;
            border-radius: 20px !important; /* More rounded corners like in the image */
            border: none !important;
            font-weight: 500 !important;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2) !important;
            margin: 0 auto; /* Center the button */
        }
        
        .stButton>button:hover {
            background-color: #365899 !important; /* Darker blue on hover */
        }

        /* Fade-in animation */
        @keyframes fadeIn {
            0% {
                opacity: 0;
                transform: translateY(-10px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a container for the navigation header
st.markdown(
    """
    <div class="nav-container">
        <div class="logo-container">
            <div class="logo-circle"></div>
            <span class="company-name">CivilSync</span>
        </div>
        <div class="nav-menu">
            <a href="/" class="nav-item">Home</a>
            <a href="/About" class="nav-item">About</a>
            <a href="/Questionnaire" class="nav-item">Questionnaire</a>
            <a href="/Results" class="nav-item">Results</a>
            <div class="login-button">Log In</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Hero Section
st.markdown(
    """
    <div class="hero">
        <div class="hero-content">
            <div class="hero-title">Your Voice Matters</div>
            <div class="hero-subtitle">See how your beliefs align with the actions of the current presidency.</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Content
st.markdown('<div class="title">CivilSync</div>', unsafe_allow_html=True)
st.markdown('<div class="motto">Sync your views with political reality</div>', unsafe_allow_html=True)
st.markdown('<p class="intro-text">Welcome to CivilSync, where you can compare your beliefs with the actions of the current presidency. '
            'Explore how political decisions align with your stance on important issues.</p>', unsafe_allow_html=True)

# Fully Centered "Get Started" Button
st.markdown('<div class="button-container">', unsafe_allow_html=True)
get_started = st.button("Get Started")
st.markdown('</div>', unsafe_allow_html=True)

if get_started:
    st.switch_page("pages/Questionnaire.py")

# Features Section
st.markdown(
    """
    <div class="features">
        <div class="feature-card">
            <img src="https://png.pngtree.com/element_pic/16/11/26/a49bef4c2559a64c0d1a80f6c66526a4.png" class="feature-icon" alt="Compare Your Beliefs">
            <div class="feature-title">Compare Your Beliefs</div>
            <div class="feature-description">See how your views align with presidential policies.</div>
        </div>
        <div class="feature-card">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135694.png" class="feature-icon" alt="Explore Policies">
            <div class="feature-title">Explore Policies</div>
            <div class="feature-description">Dive into detailed analyses of key political decisions.</div>
        </div>
        <div class="feature-card">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" class="feature-icon" alt="Stay Informed">
            <div class="feature-title">Stay Informed</div>
            <div class="feature-description">Get updates on how policies evolve over time.</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer for all pages
st.markdown(
    """
    <div class="footer">
        <a href="/About">About</a> | <a href="#">Contact</a> | <a href="#">Privacy Policy</a>
    </div>
    """,
    unsafe_allow_html=True,
)