# PlacesToEat-Flask-APP-



Places To Eat

This project presents a complete web application developed with Python, Flask, and MongoDB Atlas, along with HTML (enhanced with Bootstrap) and CSS for styling. Serving as a versatile platform, it makes it easy to explore and evaluate various dining options across different districts within a city. Through its user-friendly interface, users can easily navigate restaurant listings, read existing reviews, share their own experiences, and discover the top-rated dining spots in each area.

#### Features
Restaurant Discovery: Users can search for restaurants in specific districts of the city.
Review Submission: The application allows users to submit reviews for restaurants, sharing their dining experiences with others.

Aggregated Ratings: Utilizing MongoDB Atlas, the application calculates and displays aggregated ratings for each restaurant based on user reviews.

Autocomplete Suggestions: Users can benefit from autocomplete suggestions while searching for restaurants, enhancing user experience and efficiency.

Technologies Used:
Backend: Python with Flask framework.
Database: MongoDB Atlas for storing restaurant data and user reviews.
Frontend: HTML, Bootstrap for styling, and CSS.
Integration: The application integrates with MongoDB Atlas for seamless data storage and retrieval.

#### Files

#### HTML and CSS Files


| File | Description|
| --- | --- |
|placestoeat.html|This template allows users to browse a place by name or state using a form. It includes options for selecting the search type (by name or state) and displays corresponding input fields accordingly. JavaScript code is included to handle user interactions such as switching between search types and providing autocomplete suggestions for the place name input field.
|layout.html|This template serves as the layout for the Flask application. It includes meta tags for character set and viewport settings, imports Bootstrap CSS for styling, and defines the title of the page within a block for individual templates to override. The navigation bar includes links to the homepage and a page for submitting reviews. The main content block is defined within the <main> tag and can be overridden by individual templates.
|main.css|This CSS code defines styles for various elements used in the application.
|place_results.html|This template is used to display reviews for a specific restaurant. It extends the layout template (layout.html) and sets the title of the page to "Reviews for {{ place_name }}". Inside the main content block, it displays the restaurant name and lists reviews if available, otherwise, it displays a message indicating no reviews found.
|district_results.html|This template is used to display the best restaurants in a specific district. It extends the layout template (layout.html) and sets the title of the page to "Best places in {{ location }}". Inside the main content block, it lists the best restaurants along with their average ratings and visit counts obtained from the Flask route.
|submit.html|This template allows users to submit new restaurant reviews. It provides options to browse a place by name or state using a form. Depending on the selected option, it displays an input field for the place name or a dropdown menu for selecting a state. JavaScript is included to handle user interactions, such as switching between search types and providing autocomplete suggestions for the place name input field. Finally, it includes a footer with attribution to the creator of the restaurant icons used in the page.
|error.html|This template is used to display an error message. It extends the layout template (layout.html) and sets the title of the page to "Error". The main content block displays the error message passed from the Flask route.
|thank_you.html|Is used to display a "Thank You" message after submitting a report. It sets the title of the page to "Thank You".

#### Python files

| File | Description|
| --- | --- |
|app.py| This file is the main script of the application. It connects to a MongoDB database and contains two core functions. The placestoeat() function handles both GET and POST requests. A GET request to this function renders the main page where users can search for restaurants by district or name. A POST request processes the user's input, retrieving either restaurant reviews or the best restaurants in a district. The submit() function also handles both GET and POST requests. A GET request renders the submission form for new restaurant reviews, while a POST request validates and stores the submitted review in the database.
|credentials.py|The get_mongodb_credentials function: This function retrieves MongoDB credentials needed to establish a connection to the database. It's essential for securely accessing the MongoDB instance where restaurant reviews are stored.
|helpers.py| The get_best_places function in this script is designed to retrieve the best-rated restaurants within a specified district from a MongoDB database. By executing a predefined aggregation pipeline, it calculates the average ratings for restaurants in the given district and returns a sorted list of the top-rated establishments, along with their average ratings and visit counts.
|insert_examples.py| The insert_reviews_from_file function facilitates the insertion of restaurant reviews stored in a JSON file into a MongoDB database. It streamlines the process of populating a MongoDB collection with review data, making it convenient for initializing or updating databases with sample reviews.

#### Text files
| File | Description|
| --- | --- |
|examples.txt| This file contains examples to insert into MongoDB DataBase 