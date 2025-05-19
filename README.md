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

   

### Getting Started 
1. **Clone the repository**   
Open your terminal and run the following command:
    ```sh
    $git clone https://github.com/awuorochelle75/coffee_shop.git



2. **Navigate to the project folder**
    ```sh
        $cd coffee_shop

3. **Set up and activate a virtual environment with pipenv**
    ```sh
        $pipenv install
        $pipenv shell

4. **Install testing dependencies(optional)**
    ```sh
        $pipenv install pytest

## **Usage**
1. Run debug.py to manually test and interact with the classes.




## Features
- Creates Customer and Coffee instances with validation on names.
- Place orders linking customers to coffees with price validation.
- Retrieve all orders and unique coffees for each customer.
- Retrieve all orders and unique customers for each coffee.
- Calculate total orders and average price for each coffee.
- Identify the customer who has spent the most on a specific coffee(most_aficionado class method)
- Input validation with meaningful exceptions for invalid data.
    



## Contact Information
📧 Email: awuorochelle@gmail.com

## License
📜 MIT License @2025 Rochelle Awuor


