import streamlit as st

# Configure the page
st.set_page_config(
    page_title="CivilSync - Trump Policies",
    page_icon="🇺🇸",
    layout="wide"
)

# Base width for Gun Control (10% smaller than previous version)
gun_control_width = 706  # 784 * 0.9 = 705.6, rounded to 706

# Adjusted widths - maintaining the same proportions
abortion_width = int(gun_control_width * 0.875)  # 12.5% smaller
healthcare_width = int(gun_control_width * 0.75)   # 25% smaller
immigration_width = int(gun_control_width * 0.5)     # Half the length
taxation_width = int(gun_control_width * 0.75)       # 25% smaller

# Custom CSS for clean aesthetics and improvements
st.markdown("""
<style>
body {
    background-color: #e5dcc3; /* Slightly darker beige/brown background */
    font-family: "Arial", sans-serif;
    margin: 0;
    padding: 0;
}

/* Center the main container */
.main > div {
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Global fade-in from top animation */
@keyframes fadeInFromTop {
    0% {
        opacity: 0;
        transform: translateY(-50px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Apply the animation to various elements with the same delay */
.nav-container, .president-label, .image-container, .bar, .vertical-line, .alignment-container {
    animation: fadeInFromTop 0.8s ease-out forwards;
}

/* Navigation Bar Styling */
.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 30px;
    background-color: #f0e6d2; /* Slightly lighter than the background */
    border-bottom: 1px solid #d6cdb7;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    width: 100%;
    box-sizing: border-box;
}

.logo-container {
    display: flex;
    align-items: center;
}

.logo-circle {
    width: 40px;
    height: 40px;
    background-color: #e8c39e; /* Peachy circle */
    border-radius: 50%;
    margin-right: 15px;
}

.company-name {
    font-size: 1.5rem;
    font-weight: bold;
    color: #8d7b68; /* Brownish text color */
    font-family: "Georgia", serif;
}

.nav-menu {
    display: flex;
    align-items: center;
}

.nav-item {
    margin: 0 15px;
    color: #8d7b68; /* Match company name color */
    font-weight: 500;
    text-decoration: none;
    font-size: 1rem;
    transition: color 0.3s ease;
    cursor: default; /* Shows it's not clickable */
}

.nav-item:hover {
    color: #5c4f3f;
}

.login-button {
    background-color: #e8c39e; /* Peachy button */
    color: #8d7b68; /* Same color as company name */
    padding: 8px 20px;
    border-radius: 20px;
    font-weight: bold;
    text-align: center;
    margin-left: 15px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.login-button:hover {
    background-color: #d8b38e;
}

/* President label - positioned in top left */
.president-label {
    font-size: 2rem;
    font-weight: bold;
    color: #5c4f3f;
    font-family: "Georgia", serif;
    text-align: left;
    margin-top: 5px; /* Further reduced from 10px */
    margin-left: 30px;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
}

/* Enhanced Image Styling */
.image-container {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 5px; /* Reduced from 20px */
    margin-bottom: 20px; /* Reduced from 30px */
    overflow: visible; /* Changed to visible for animations */
}

/* Professional painting frame for Trump image */
.image-frame {
    position: relative;
    display: inline-block;
    padding: 20px; /* Increased padding to accommodate larger image */
    background: #8b7d6b;
    border-radius: 2px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    z-index: 1;
}

/* Ornate frame effect with pseudo-elements */
.image-frame:before {
    content: '';
    position: absolute;
    top: 7px; /* Adjusted for larger frame */
    left: 7px;
    right: 7px;
    bottom: 7px;
    border: 2px solid #d5c4a1;
    background: linear-gradient(45deg, #8b7d6b, #a69382);
    z-index: -1;
}

.image-frame:after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    border: 1px solid #36281f;
    box-shadow: inset 0 0 8px rgba(0,0,0,0.5);
    z-index: 2;
    pointer-events: none;
}

/* Inner gold trim */
.image-inner-frame {
    position: relative;
    border: 4px solid #d5c4a1; /* Slightly thicker border */
    padding: 3px; /* Increased padding */
    background: linear-gradient(to right, #e8d8bf, #d5c4a1, #e8d8bf);
}

/* Make Trump image 30% larger */
.trump-image {
    width: 195px; /* 150px * 1.3 = 195px */
    display: block;
    border: 1px solid #36281f;
    transition: all 0.3s ease;
}

/* Presidential seal watermark behind the image */
.presidential-seal {
    position: absolute;
    width: 260px; /* Increased size to match larger image */
    height: 260px;
    background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIj48Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjkwIiBmaWxsPSJub25lIiBzdHJva2U9IiNkOGIzOGUiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWRhc2hhcnJheT0iNSIgLz48Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjcwIiBmaWxsPSJub25lIiBzdHJva2U9IiNkOGIzOGUiIHN0cm9rZS13aWR0aD0iMiIgLz48cGF0aCBkPSJNNTAgMTAwQzUwIDcyIDcyIDUwIDEwMCA1MFMxNTAgNzIgMTUwIDEwMCAxMjggMTUwIDEwMCAxNTAgNTAgMTI4IDUwIDEwMHoiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2Q4YjM4ZSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSIzLDIiIC8+PHRleHQgeD0iMTAwIiB5PSI3MCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2Q4YjM4ZSIgc3R5bGU9ImZvbnQtZmFtaWx5OiBHZW9yZ2lhLCBzZXJpZjsgZm9udC1zaXplOiA4cHg7Ij5TRUFMIEFORCBPRkZJQ0U8L3RleHQ+PHRleHQgeD0iMTAwIiB5PSIxMzAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNkOGIzOGUiIHN0eWxlPSJmb250LWZhbWlseTogR2VvcmdpYSwgc2VyaWY7IGZvbnQtc2l6ZTogOHB4OyI+UFJFUzhERU5UIE9GIFRIRSBVSC5TPC90ZXh0Pjwvc3ZnPg==');
    background-repeat: no-repeat;
    background-position: center;
    opacity: 0.2;
    z-index: -1;
}

/* Styling for Trump name - positioned at bottom left of image - 50% larger and animated */
.name-label {
    position: absolute;
    bottom: -10px;
    left: 40%; /* Increased distance from the image */
    font-size: 3.3rem; /* 50% larger than 2.2rem */
    font-weight: bold;
    color: #5c4f3f;
    font-family: "Georgia", serif;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    transform: translateX(-100%);
    animation: slideInFromLeft 1.5s ease forwards;
}

/* Animation for name to slide in from left */
@keyframes slideInFromLeft {
    0% {
        transform: translateX(-100vw); /* Start from far left of viewport */
        opacity: 0;
    }
    100% {
        transform: translateX(-100%); /* End at original position */
        opacity: 1;
    }
}

/* Styling for Republican label - positioned at top right of image - 50% larger and animated */
.party-label {
    position: absolute;
    top: -10px;
    right: 40%; /* Increased distance from the image */
    font-size: 3.3rem; /* 50% larger than 2.2rem */
    font-weight: bold;
    color: #5c4f3f;
    font-family: "Georgia", serif;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    transform: translateX(100%);
    animation: slideInFromRight 1.5s ease forwards;
}

/* Animation for party label to slide in from right */
@keyframes slideInFromRight {
    0% {
        transform: translateX(100vw); /* Start from far right of viewport */
        opacity: 0;
    }
    100% {
        transform: translateX(100%); /* End at original position */
        opacity: 1;
    }
}

/* Enhanced Bar styles with professional text - now black text with Georgia font */
.bar {
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 15px;
    height: 70px;
    margin: 15px 0;
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    font-size: 1.4rem; /* Keep the same size */
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #000000; /* Black text instead of white */
    font-weight: bold;
    font-family: "Georgia", serif; /* Same font as Trump's name */
}

/* Hover effect on bars */
.bar:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

/* Red and Green Bars - softened colors */
.red-bar {
    background-color: #f44336;
    background-image: linear-gradient(to right, #f44336, #f5665a);
}

.green-bar {
    background-color: #4CAF50;
    background-image: linear-gradient(to right, #4CAF50, #5fc463);
}

/* Thicker vertical center line with darker color - slightly longer */
.vertical-line {
    position: relative;
    width: 5px;
    background-color: black; /* Fully black - darker */
    height: 520px; /* Increased from 450px to 520px */
    margin: 0 auto;
    border-radius: 5px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.5); /* Darker shadow */
}

/* Alignment percentage text */
.alignment-container {
    text-align: center;
    margin-top: 40px; /* Reduced from 50px */
    padding: 20px;
}

.alignment-text {
    font-size: 2rem;
    font-weight: bold;
    color: #5c4f3f;
    font-family: "Georgia", serif;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
}

.alignment-subtext {
    font-size: 1.2rem; /* 40% smaller than 2rem */
    color: #5c4f3f;
    font-family: "Georgia", serif;
    margin-top: 15px;
}

.stApp {
    background-color: #e5dcc3; /* Same beige/brown background for the whole app */
}

/* Remove default Streamlit padding */
.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    max-width: 100% !important;
}

/* Hide Streamlit menu and footer */
#MainMenu, footer, header {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# 1) Navigation Bar
# ---------------------------
st.markdown(
    """
    <div class="nav-container">
        <div class="logo-container">
            <div class="logo-circle"></div>
            <span class="company-name">CivilSync</span>
        </div>
        <div class="nav-menu">
            <span class="nav-item">Home</span>
            <span class="nav-item">About</span>
            <span class="nav-item">Questionnaire</span>
            <span class="nav-item">Results</span>
            <div class="login-button">Log In</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# 2) Add "Current President:" label in top left
# ---------------------------
st.markdown(
    """
    <div class="president-label">Current President:</div>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# 3) Enhanced Trump Image with professional painting frame - 30% larger
# ---------------------------
st.markdown(
    """
    <div class="image-container">
        <span class="name-label">Donald Trump</span>
        <div class="presidential-seal"></div>
        <div class="image-frame">
            <div class="image-inner-frame">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg"
                     class="trump-image" alt="Donald Trump">
            </div>
        </div>
        <span class="party-label">Republican</span>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# 4) Create three columns: Left Bars | Vertical Line | Right Bars (centered)
# ---------------------------
col1, col2, col3 = st.columns([1, 0.05, 1], gap="small")

with col1:
    # Left-side (Red) bars - first three
    st.markdown(f"""<div class="bar red-bar" style="width:{gun_control_width}px; margin-left: auto;">Gun Control</div>""", unsafe_allow_html=True)
    st.markdown(f"""<div class="bar red-bar" style="width:{abortion_width}px; margin-left: auto;">Abortion</div>""", unsafe_allow_html=True)
    st.markdown(f"""<div class="bar red-bar" style="width:{healthcare_width}px; margin-left: auto;">Healthcare</div>""", unsafe_allow_html=True)
    
    # Add an invisible fourth item
    st.markdown("<div style='height: 70px; margin: 15px 0;'></div>", unsafe_allow_html=True)
    
    # Immigration as fifth item
    st.markdown(f"""<div class="bar red-bar" style="width:{immigration_width}px; margin-left: auto;">Immigration</div>""", unsafe_allow_html=True)

with col2:
    # Vertical Black Line
    st.markdown('<div class="vertical-line"></div>', unsafe_allow_html=True)

with col3:
    # Create three blank spaces to align the taxation block as the fourth item
    st.markdown("<div style='height: 70px; margin: 15px 0;'></div>", unsafe_allow_html=True)  # First empty bar
    st.markdown("<div style='height: 70px; margin: 15px 0;'></div>", unsafe_allow_html=True)  # Second empty bar
    st.markdown("<div style='height: 70px; margin: 15px 0;'></div>", unsafe_allow_html=True)  # Third empty bar
    
    # Taxation block (fourth position)
    st.markdown(f"""<div class="bar green-bar" style="width:{taxation_width}px; margin-right: auto;">Taxation</div>""", unsafe_allow_html=True)

# ---------------------------
# 5) Add alignment percentage text at bottom with YOU capitalized
# ---------------------------
st.markdown(
    """
    <div class="alignment-container">
        <div class="alignment-text">There is a 19.3% alignment between the political views that matter to YOU and the actions of the presidency thus far</div>
        <div class="alignment-subtext">If you want to learn more about how we categorized certain viewpoints of the current president, visit our About homepage</div>
    </div>
    """,
    unsafe_allow_html=True
)
