# OUS Trip Booking Web App

#### Video Demo: <https://youtu.be/-nrRk1s0cZ0>

#### Description:

**Live Demo:** https://ous-6o1j.onrender.com/

This web application allows users to seamlessly book trips for OUS Company. It provides a user-friendly interface with features like:

- **Web Structure:** The web application's foundation is built upon HTML, SASS, and Bootstrap to create a visually appealing and responsive user interface. Python serves as the backbone, handling the application's logic and functionality.

  - layout.html : serves as the foundational template for the website's structure, defining its header and footer sections. Upon successful login, the navigation bar dynamically updates, replacing the registration button with the user's name. Clicking this name provides access to the user's profile. Additionally, a LinkedIn link is prominently displayed in the footer for user convenience.

  - index.html : page serves as the primary entry point, providing a concise overview of the website and its key offerings. Dynamically generated content, powered by JavaScript, alternates the featured main trip between Beppu and Nagasaki to enhance user engagement. The homepage also features prominent links to dedicated central trip and extra trip pages.

  - central_trip.html : incorporates a unique layout and interactive features. A prominent 'Add Trip' button facilitates trip additions. The system is designed to handle multiple trips efficiently, preventing duplicate entries and ensuring accurate pricing calculations. By avoiding redundant central trip additions, users can maintain control over their itinerary and associated costs.

  - extra_trip.html : shares a similar layout with central_trip.html but omits the plus button and associated functionality. This page focuses on providing a wider selection of optional trips for customers to explore and potentially include in their itineraries.

  - profile.html : dynamically displays personalized content based on user authentication. Unauthorized access is redirected to the login page. For authenticated users, the page showcases booked trips, including detailed trip information and total costs. A convenient cancellation option is provided. For site owners, a dedicated dashboard within the profile page offers comprehensive analytics, including user counts, booking trends, and popular trip insights.

  - login.html : handles user authentication. Upon incorrect login credentials, a clear and informative error message is displayed to guide the user in rectifying the issue.

  - register.html : presents a user-friendly registration form for new users. It incorporates essential fields for account creation and includes robust validation to ensure data integrity.

- **Data Integrity and Security:** Rigorous data validation and protection protocols are implemented. Before storage, all data undergoes thorough inspection. Leveraging Python's capabilities and SQL's validation power, sensitive information is securely managed and protected against potential vulnerabilities.

  - app.py : serves as the heart of the application, orchestrating its core functionalities. This well-structured script incorporates robust data validation measures to ensure the integrity of stored information. User input is thoroughly sanitized to prevent the inclusion of symbols, guaranteeing only numbers and letters are processed. Additionally, unique user IDs are generated and secured using bcrypt, a powerful hashing algorithm. These comprehensive safeguards significantly minimize the risk of unexpected or malicious data entry into the information.db

- **Data Storage and Management:** A SQLite database (information.db) houses essential data organized into three tables: users for customer details, trip for trip information and codes, and reserve for tracking booked trips. reserve table also serves as a foundation for data aggregation and analysis.

  - informations.db : adheres to strict SQL database design principles, ensuring data integrity and consistency. The database schema is meticulously structured to prevent duplicate entries and accommodate future data expansion. Tables are optimized for efficient data retrieval and management, supporting the application's core functionalities.

- **Core Functionality:** The platform offers seamless tour booking and cancellation capabilities. A robust system ensures efficient management of reservations. Additionally, a flexible pricing structure allows for dynamic adjustments to tour costs."

- **Customer-Centric Display:** The platform provides a clear and intuitive interface showcasing customers' booked trips and associated costs. This user-friendly design enhances the overall booking experience.

  - app.py : orchestrates seamless user interactions by providing a comprehensive booking experience. Here's how it achieves this:

  • Booking History: Customers can access and view all their booked trips in a convenient and organized manner.
  • Duplicate Prevention: Robust validation mechanisms within app.py prevent users from accidentally booking the same trip twice.
  • Individual Trip Display: The application ensures clarity by presenting only unique trip information, avoiding confusion caused by duplicate entries.
  • Trip-Specific Messages and Pricing: app.py manages the system for handling special messages and associated trip pricing. This functionality can be used to display important details or promotions relevant to each booked trip.

- **Owner Analytics:** A dedicated dashboard provides owners with essential insights, including customer count, total bookings, and popular trip trends. Advanced data analytics, powered by Python and SQLite, deliver actionable information for informed decision-making.

  - app.py : Leveraging Python's data manipulation capabilities, app.py extracts valuable insights from user interactions.db. It retrieves data from the information.db database, particularly focusing on customer bookings. This retrieved data is then processed and analyzed, potentially generating a new table within the database. This new table could provide insights such as:

  • Customer Bookings: Comprehensive information about which trips individual customers have booked.
  • Trip Popularity: Identification of the most popular trips based on booking trends.
  • User Count: An accurate count of total users registered with the application.

  These insights empower site owners with actionable data, enabling them to make informed decisions regarding trip offerings, pricing strategies, and marketing campaigns.

- **Render:** To ensure widespread accessibility, the application is seamlessly deployed on the internet using Render. This robust platform facilitates efficient project management and deployment, making the booking service readily available to users globally.

**In my own words**

I meticulously crafted this web project, pouring countless hours into every aspect. From the initial concept to the final design, I carefully selected colors, layouts, and wording to create a visually appealing and user-friendly experience.

Data security was a paramount concern. I implemented robust measures to safeguard customer information, ensuring that data collection, browsing, management, and display were handled with the utmost care.

The development journey was not without its challenges. Countless hours were spent troubleshooting code and overcoming obstacles. With unwavering determination and the invaluable knowledge gained from CS50x, I persevered through setbacks to deliver a complete project within a demanding two-week timeframe.

I am immensely proud of the final product and grateful for the opportunity to develop my skills through this project.

**Summary**

- **User Management:** Users can register, sign in, and sign out to manage their accounts.
- **Trip Booking:** Users can easily browse and reserve desired trips with a simple click of the "Booking" button.
- **Booking Overview:** A dedicated profile section (/profile) displays the user's booked trips, including the total number and trip names.
- **Data Analysis:** The app leverages SQLite3 to gather insights into user activity and trip popularity, providing valuable information for OUS Company.
- **Deployment:** The application is deployed using Flask, a lightweight web framework.
- **Frontend Styling:** Bootstrap and Sass are employed to create an attractive and responsive user interface.

**Getting Started**

1. **Prerequisites:**
   - Python 3.x (https://www.python.org/downloads/)
   - pip (package manager for Python - usually included with Python)
2. **Installation:**
   - Clone this repository: `https://github.com/TEbefine/ous_travel.git`
   - Navigate to the project directory: `cd profect`
   - Install dependencies: `pip install -r requirements.txt`
3. **Running the App:**
   - Start the development server: `flask run`
   - Access the application in your web browser: http://127.0.0.1:5000/

**Contributing**

We welcome contributions to this project! Please see the `CONTRIBUTING.md` file (if present) for details on how to contribute code, report issues, and propose improvements.

**Disclaimer**

This is a basic example application and may require further development for production use.
