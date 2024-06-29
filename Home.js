import React, { useState } from 'react';
import './Home.css';
// import logo from './logo.png'; // Assuming the logo is in the same directory as this file

const Homepage = () => {
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  return (
    <div className="home-container">
      <nav className="navbar">
        <img src={"logo.png"} alt="IT Solutions Logo" className="logo" />
        <div className={`hamburger-menu ${menuOpen ? 'active' : ''}`} onClick={toggleMenu}>
          <span></span>
          <span></span>
          <span></span>
        </div>
        <div className={`nav-links ${menuOpen ? 'active' : ''}`}>
          <a href="services.js" onClick={toggleMenu}>Home</a>
          <a href="#about" onClick={toggleMenu}>About</a>
          <a href="#services" onClick={toggleMenu}>Services</a>
          <a href="#contact" onClick={toggleMenu}>Contact</a>
        </div>
      </nav>
      <header className="home-header">
        <h1>Welcome to IT Solutions</h1>
        <p>Your partner in technology and innovation</p>
      </header>
      <main>
        <section className="home-about" id="about">
          <h2>About Us</h2>
          <p>
            At IT Solutions, we provide top-notch technology services to help your business thrive in the digital age. Our team of experts is dedicated to delivering innovative solutions tailored to your unique needs.
          </p>
        </section>
        <section className="home-services" id="services">
          <h2>Our Services</h2>
          <ul>
            <li>Custom Software Development</li>
            <li>Cloud Computing</li>
            <li>Cybersecurity</li>
            <li>IT Consulting</li>
            <li>Data Analytics</li>
          </ul>
        </section>
        <section className="home-testimonials">
          <h2>What Our Clients Say</h2>
          <div className="testimonial-cards">
            <div className="testimonial-card">
              <p>"IT Solutions has been instrumental in helping us scale our business. Their expertise in cloud computing has been invaluable."</p>
              <span>John Doe, CEO of XYZ Corporation</span>
            </div>
            <div className="testimonial-card">
              <p>"The cybersecurity solutions provided by IT Solutions have given us peace of mind and protected our business from potential threats."</p>
              <span>Jane Smith, IT Manager of ABC Inc.</span>
            </div>
          </div>
        </section>
        <section className="home-contact" id="contact">
          <h2>Contact Us</h2>
          <p>
            Ready to take your business to the next level? Get in touch with us today!
          </p>
          <button>Contact Us</button>
        </section>
      </main>
    </div>
  );
};

export default Homepage;

