import streamlit as st

# Function to create testimonials sliders
def testimonials_slider(testimonials):
    st.markdown("<h2 style='text-align:center;'>Testimonials</h2>", unsafe_allow_html=True)
    st.markdown("<div id='testimonials' class='testimonials'>", unsafe_allow_html=True)
    for testimonial in testimonials:
        st.markdown(f"<div class='testimonial'><h4>{testimonial['author']}</h4><p>{testimonial['content']}</p></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Home Page
def home_page():
    st.title("Welcome to Saanvi Infotech")
    st.markdown("""
        <h3>Your IT Solutions Partner</h3>
        <p>Empowering Businesses with Innovative IT Solutions</p>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
        <h3>Our Services</h3>
        <ul>
            <li><strong>Software Development:</strong> Tailored solutions for your business needs.</li>
            <li><strong>App Development:</strong> Crafted mobile and web applications that resonate with your audience.</li>
            <li><strong>Data Analytics:</strong> Unlock the power of data to make informed decisions.</li>
        </ul>
        <p>Want to know more? Visit the <strong>Services</strong> page!</p>
    """, unsafe_allow_html=True)
    st.markdown("---")
    testimonials = [
        {"author": "Praphulla", "content": "I am extremely satisfied with the software development services provided by Saanvi Infotech. They exceeded my expectations and delivered high-quality solutions on time."},
        {"author": "Pranav", "content": "The team at Saanvi Infotech did an excellent job in developing our mobile app. Their attention to detail and commitment to delivering a user-friendly product were impressive."},
        {"author": "Vikash", "content": "With the data analytics solutions from Saanvi Infotech, we were able to gain valuable insights that helped us make strategic business decisions. Highly recommend their services."}
    ]
    testimonials_slider(testimonials)

# Services Page
def services_page():
    st.title("Our Services")
    st.markdown("""
        <h3>Software Development</h3>
        <p>Tailored solutions for your business needs.</p>
        <h3>App Development</h3>
        <p>Crafted mobile and web applications that resonate with your audience.</p>
        <h3>Data Analytics</h3>
        <p>Unlock the power of data to make informed decisions.</p>
    """, unsafe_allow_html=True)

# About Us Page
def about_us_page():
    st.title("About Us")
    st.markdown("""
        <h3>Company Overview</h3>
        <p>Saanvi Infotech</p>
        <h3>Our Team</h3>
        <p>team members</p>
        <h3>Achievements</h3>
        <p>Awards, milestones, success stories</p>
    """, unsafe_allow_html=True)

# Contact Page
def contact_page():
    st.title("Contact Us")
    st.markdown("""
        <h3>Contact Form</h3>
        <p>Form fields for name, email, message</p>
        <h3>Contact Information</h3>
        <p>Company address, phone number, email</p>
    """, unsafe_allow_html=True)

# Main function
def main():
    st.markdown("""
        <style>
            .sidebar {
                position: fixed;
                left: 0;
                top: 0;
                height: 100%;
                width: 250px;
                background-color: #333;
                padding: 20px;
                overflow-x: hidden;
            }

            .sidebar a {
                display: block;
                color: #f2f2f2;
                padding: 10px;
                text-decoration: none;
            }

            .sidebar a:hover {
                background-color: #ddd;
                color: black;
            }

            .page-content {
                margin-left: 250px;
                padding: 20px;
            }

            .testimonials {
                width: 250px;
                height: 100%;
                overflow-y: auto;
                position: fixed;
                right: 0;
                top: 0;
                padding: 20px;
                background-color: #f4f4f4;
            }

            .testimonial {
                margin-bottom: 20px;
                padding: 10px;
                background-color: #fff;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }

            /* Marquee effect */
            .marquee {
                width: 100%;
                overflow: hidden;
                white-space: nowrap;
                box-sizing: border-box;
            }

            .marquee p {
                display: inline-block;
                padding-left: 100%;
                animation: marquee 15s linear infinite;
            }

            @keyframes marquee {
                0% { transform: translate(0, 0); }
                100% { transform: translate(-100%, 0); }
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="sidebar">
            <a href="#home">Home</a>
            <a href="#services">Services</a>
            <a href="#about">About Us</a>
            <a href="#contact">Contact</a>
        </div>
    """, unsafe_allow_html=True)

    page = st.sidebar.selectbox("Navigate", ["Home", "Services", "About Us", "Contact"])

    st.markdown("<div class='page-content'></div>", unsafe_allow_html=True)

    if page == "Home":
        home_page()
    elif page == "Services":
        services_page()
    elif page == "About Us":
        about_us_page()
    elif page == "Contact":
        contact_page()

if __name__ == "__main__":
    main()
