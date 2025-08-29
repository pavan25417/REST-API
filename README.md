# BFHL REST API - VIT Assignment

This is a REST API implementation for the VIT Full Stack assignment.

## Features

- **POST /bfhl**: Processes an array and returns categorized data
- Separates odd/even numbers, alphabets, and special characters
- Calculates sum of all numbers
- Creates concatenated string with alternating caps in reverse order
- Returns structured JSON response

## API Specification

### Endpoint
- **URL**: `/bfhl`
- **Method**: POST
- **Content-Type**: application/json

### Request Format
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
```

### Response Format
```json
{
  "is_success": true,
  "user_id": "john_doe_17091999",
  "email": "john@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "rA"
}
```

## Local Development

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Run the server**:
   ```bash
   npm start
   ```

3. **Development with auto-reload**:
   ```bash
   npm run dev
   ```

The server will run on `http://localhost:3000`

## Deployment Options

### 1. Vercel Deployment
1. Push code to GitHub repository
2. Connect repository to Vercel
3. Deploy automatically

### 2. Railway Deployment
1. Push code to GitHub
2. Connect to Railway
3. Deploy with one click

### 3. Render Deployment
1. Fork the repository
2. Connect to Render
3. Deploy as web service

## Testing

Test the API using curl or Postman:

```bash
curl -X POST https://your-api-url/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["a","1","334","4","R","$"]}'
```

## Project Structure

```
├── bfhl-api.js      # Main server file
├── package.json     # Dependencies and scripts
├── vercel.json      # Vercel deployment config
└── README.md        # This file
```

## Requirements Met

✅ REST API with POST method  
✅ Array processing for odd/even numbers  
✅ Alphabets conversion to uppercase  
✅ Special characters identification  
✅ Sum calculation  
✅ Concatenation with alternating caps in reverse order  
✅ Proper error handling  
✅ JSON response format  
✅ Hosting configuration for Vercel/Railway/Render  

## Author

Student Name - VIT University
