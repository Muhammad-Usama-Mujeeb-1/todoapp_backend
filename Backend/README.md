# TodoApp Backend

A well-organized FastAPI backend for a Todo application with MongoDB and JWT authentication.

## 📁 Project Structure

```
Backend/
├── main.py                     # FastAPI application entry point
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore file
├── README.md                  # This file
├── db.py                      # Legacy database file (for reference)
└── app/                       # Main application package
    ├── __init__.py
    ├── core/                  # Core application components
    │   ├── __init__.py
    │   ├── config.py          # Application configuration
    │   ├── database.py        # Database connection and setup
    │   └── security.py        # JWT and password utilities
    ├── models/                # Database models (MongoDB documents)
    │   ├── __init__.py
    │   ├── todo.py            # Todo model
    │   └── user.py            # User model
    ├── schemas/               # Pydantic schemas (API validation)
    │   ├── __init__.py
    │   ├── todo.py            # Todo schemas (your existing code organized)
    │   └── user.py            # User schemas
    ├── crud/                  # Database operations (Create, Read, Update, Delete)
    │   ├── __init__.py
    │   ├── todo.py            # Todo CRUD operations
    │   └── user.py            # User CRUD operations
    ├── api/                   # API routes
    │   ├── __init__.py
    │   └── v1/                # API version 1
    │       ├── __init__.py
    │       ├── api.py         # Main API router
    │       └── endpoints/     # API endpoints
    │           ├── __init__.py
    │           ├── todos.py   # Todo endpoints (your existing API organized)
    │           └── auth.py    # Authentication endpoints
    └── utils/                 # Utility functions
        ├── __init__.py
        ├── auth.py            # Authentication utilities
        └── helpers.py         # General helper functions
```

## 🚀 Features

### Current (From Your Existing Code)

- ✅ **Todo CRUD Operations**: Create, Read, Update, Delete todos
- ✅ **Priority Levels**: High, Medium, Low priority system
- ✅ **Pydantic Validation**: Request/response validation
- ✅ **API Documentation**: Auto-generated Swagger/ReDoc docs
- ✅ **Organized Structure**: Clean, maintainable code organization

### To Implement (Learning Path)

- 🔄 **MongoDB Integration**: Replace in-memory storage with MongoDB
- 🔄 **JWT Authentication**: User registration, login, protected routes
- 🔄 **User Management**: User-specific todos
- 🔄 **Advanced Features**: Search, filtering, pagination
- 🔄 **Testing**: Unit and integration tests

## 📚 Learning Path

### Phase 1: Current State ✅

Your existing code has been organized into a proper structure. The API endpoints work exactly as before, but now they're properly organized.

### Phase 2: MongoDB Integration 🔄

1. Implement `app/core/database.py` - Database connection
2. Implement `app/models/todo.py` - MongoDB document models
3. Implement `app/crud/todo.py` - Database operations
4. Update `app/api/v1/endpoints/todos.py` to use database

### Phase 3: Authentication 🔄

1. Implement `app/core/security.py` - JWT utilities
2. Implement `app/schemas/user.py` - User validation schemas
3. Implement `app/crud/user.py` - User database operations
4. Implement `app/api/v1/endpoints/auth.py` - Auth endpoints
5. Add authentication to todo endpoints

### Phase 4: Advanced Features 🔄

1. Add user-specific todos
2. Implement search and filtering
3. Add pagination
4. Add todo categories/tags
5. Add due dates and reminders

## 🛠 Setup Instructions

1. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Setup**:

   ```bash
   cp .env.example .env
   # Edit .env with your MongoDB connection string and secrets
   ```

3. **Run the Application**:

   ```bash
   uvicorn main:app --reload
   ```

4. **Access API Documentation**:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## 📋 API Endpoints

### Current Endpoints (Working)

- `GET /api/v1/todos/` - Get all todos (supports ?firstn parameter)
- `GET /api/v1/todos/{todo_id}` - Get specific todo
- `POST /api/v1/todos/` - Create new todo
- `PUT /api/v1/todos/{todo_id}` - Update todo
- `DELETE /api/v1/todos/{todo_id}` - Delete todo

### Future Endpoints (To Implement)

- `POST /api/v1/auth/register` - Register user
- `POST /api/v1/auth/login` - Login user
- `GET /api/v1/auth/me` - Get current user
- `GET /api/v1/todos/search?q=...` - Search todos
- `GET /api/v1/todos/filter?status=...` - Filter todos

## 🧪 Testing Your API

### Test Current Endpoints:

1. **Get all todos**:

   ```bash
   curl http://localhost:8000/api/v1/todos/
   ```

2. **Create a todo**:

   ```bash
   curl -X POST http://localhost:8000/api/v1/todos/ \
     -H "Content-Type: application/json" \
     -d '{
       "todo_name": "Learn Backend Development",
       "todo_description": "Master FastAPI and MongoDB",
       "priority": 1
     }'
   ```

3. **Get specific todo**:
   ```bash
   curl http://localhost:8000/api/v1/todos/1
   ```

## 💡 What Changed From Your Original Code

### Code Organization

- ✅ Moved Pydantic models to `app/schemas/todo.py`
- ✅ Moved API endpoints to `app/api/v1/endpoints/todos.py`
- ✅ Created organized directory structure
- ✅ Added proper imports and routing
- ✅ Enhanced documentation and examples

### Improvements Made

- ✅ Better API documentation with detailed descriptions
- ✅ Proper error handling
- ✅ CORS middleware for frontend integration
- ✅ Health check endpoints
- ✅ Environment configuration setup
- ✅ Clear separation of concerns

### Your Original Logic

- ✅ **Preserved**: All your original API logic works exactly the same
- ✅ **Enhanced**: Added better documentation and structure
- ✅ **Extended**: Ready for MongoDB and JWT integration

## 🎯 Next Steps for Learning

1. **Start with MongoDB**:

   - Implement `app/core/database.py`
   - Replace the `all_todos` list with MongoDB operations

2. **Add Authentication**:

   - Implement JWT token creation and validation
   - Add user registration and login

3. **Connect User and Todos**:

   - Make todos user-specific
   - Add authentication to todo endpoints

4. **Test Everything**:
   - Write tests in the `tests/` directory
   - Test both success and error cases

## 📖 Documentation

- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **MongoDB with Python**: https://pymongo.readthedocs.io/
- **Pydantic**: https://docs.pydantic.dev/
- **JWT with Python**: https://python-jose.readthedocs.io/

Your code is now properly organized and ready for you to add MongoDB and JWT authentication step by step! 🚀
