# Coffee Shop Domain Modelling

## **Description**
This project models a Coffee Shop domain using object-oriented programming principles in python.The application defines three main entities:'Customer','Coffee', and 'Order' and establishes their relationships to simulate a simple coffee ordering system.
## Project Structure
- 'customer.py' - defines the 'Customer' class with properties,order management and aggregate methods.
- 'coffee.py' - defines the 'Coffee' class with order tracking and statistics methods.
- 'order.py' - defines the 'Order' class linking 'Customer' and 'Coffee' instances with a price attribute.
- 'debug.py' - a script to manually test the domain model functionality interactively.



## Setup Instructions 

### **Requirements**
- Before setting up the project, ensure you have the following installed:

    - Python 3.7 or higher

    - 'pipenv' - for virtual environment and dependency management.

    - 'pytest' - for running automated tests

    - Git

    - Text Editor (e.g., Visual Studio Code)

    - Web Browser

### Getting Started 
1. **Clone the repository**   
Open your terminal and run the following command:
    ```sh
    $git clone https://github.com/awuorochelle75/coffee_shop.git



2. **Navigate to the project folder**
    ```sh
        $cd coffee_shop

3. **Install dependencies**
    ```sh
        $npm install

4. **Start the JSON Server**
The JSON server simulates a backend API for fetching and updating book data. Run:
    ```sh
        $json-server --watch db.json

5.Run the Application

    - Open index.html in your web browser

    - You can also use Live Server if using VS Code

## **How to Use WeBook**
- Browse Books: View a collection of books displayed on the homepage.

- Search Books: Use the search bar to find books by title.

- Filter by Genre: Select a genre from the dropdown to filter books.

- View Book Details: Click on a book to see more details, including title, author, description, and price.

- Purchase Books: Click "Purchase" to buy a book, with a confirmation alert.


## Live Demo
🔗 Access the web application here:
https://webook-website.vercel.app/


## JSON Server (API Endpoints)
The app interacts with a local JSON server that acts as the backend. Here are the available API endpoints:

        GET /books        # Fetch all books
        GET /books/:id    # Fetch a single book by ID
    

## Technologies Used
- This project is built using:

    - HTML for structure

    - CSS for styling

    - JavaScript for interactivity

    - JSON Server for mock API

## Dependencies
Google (for external resources)

## Contact Information
📧 Email: awuorochelle@gmail.com

## License
📜 MIT License @2025 Rochelle Awuor


