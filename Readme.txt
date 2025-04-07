/*
 * 📄 **Documentation**:
 * This application, developed by **Lukanyo Nkohla**, allows users to withdraw money from their bank accounts. 
 * The business logic is implemented using a service layer that interacts with the database and communicates 
 * with **AWS SNS** to log each withdrawal event. 🚀

---

### 🌟 **Main Features**:
- 🏦 **Withdrawal Endpoint**: `/bank/withdraw`
- 📡 **AWS SNS Integration**: Publishes withdrawal events to SNS topics.
- 🗄️ **Database**: SQLite is used for storing account balances.

---

### 🛠️ **Design Decisions**:
- **Service Layer**: Business logic is kept separate from the controller to maintain clean, reusable code. 🧹
- **Repositories**: The repository pattern abstracts database queries from the rest of the application. 🗂️
- **FastAPI**: Chosen for its speed, automatic validation with Pydantic, and native async support. ⚡
- ** Database** : Chosen ORM to instead of writing SQL queries directly, making the code cleaner, more readable, and potentially easier to maintain.
- **AWS SNS**: Decouples event publishing from the core logic, enabling better scaling and monitoring. 📈

---

### 📂 **Folder Structure**:
- **controllers/**: Contains route handlers that process requests and send responses. 📬
- **repositories/**: Contains database access logic. 🛢️
- **models/**: Defines the structure for database models and event models. 🏗️
- **schemas/**: Defines input and output validation using Pydantic. ✅
- **exceptions/**: Contains custom error classes. 🚨
- **events/**: Includes utility functions like AWS SNS publishing and logging. 📤
- **databaseConn/**: Manages database connections. 🔗
- **config/**: Contains configuration files for the application, including settings for AWS and database connections. ⚙️
- **.env**: Holds environment variables such as AWS credentials and region. 🔒

---

### 📚 **Libraries Used**:
1. **FastAPI**:
    - A modern asynchronous web framework for building APIs with Python 3.6+. 🐍
    - Used for routing, dependency injection (DI), and request validation. 🚀

2. **SQLAlchemy**:
    - An Object-Relational Mapping (ORM) library used for database access. 🗄️
    - `declarative_base()` is used to create model mappings.
    - `Session` is utilized for querying and updating the database.

3. **boto3**:
    - AWS SDK for Python, used to interact with AWS services. ☁️
    - Specifically used to send messages to AWS Simple Notification Service (SNS). 📡
    - Requires AWS credentials and a configured region.

4. **Pydantic**:
    - A data validation and parsing library. ✅
    - Used in FastAPI to validate and parse incoming request bodies.

5. **Decimal**:
    - A Python library used for accurate financial calculations. 💰
    - Preferred over floats to avoid rounding errors.

---

### 💡 **Key Concepts**:
- **Dependency Injection**:
  - FastAPI’s `Depends()` is used to wire services automatically into endpoints, promoting clean separation of concerns. 🧩

---

### 📝 **Summary**:
- Cleanly separates responsibilities within the application. 🧹
- Components are designed to be testable and debuggable, enhancing development and maintenance workflows. 🛠️
*/
