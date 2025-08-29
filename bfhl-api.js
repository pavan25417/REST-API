const express = require('express');
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// PORT from environment or default to 3000
const PORT = process.env.PORT || 3000;

// POST endpoint /bfhl
app.post('/bfhl', (req, res) => {
    try {
        // Extract data from request body
        const { data } = req.body;

        // Validate input
        if (!data || !Array.isArray(data)) {
            return res.status(400).json({
                is_success: false,
                error: "Invalid input: 'data' should be an array"
            });
        }

        // Initialize result arrays
        let oddNumbers = [];
        let evenNumbers = [];
        let alphabets = [];
        let specialCharacters = [];
        let sumNumbers = 0;
        let allAlphabetChars = [];

        // Process each item in the data array
        data.forEach(item => {
            // Convert to string if not already
            const itemStr = String(item);

            // Check if it's a number (all digits)
            if (/^\d+$/.test(itemStr)) {
                const num = parseInt(itemStr);
                if (num % 2 === 0) {
                    evenNumbers.push(itemStr);
                } else {
                    oddNumbers.push(itemStr);
                }
                sumNumbers += num;
            }
            // Check if it's alphabetical (all letters)
            else if (/^[a-zA-Z]+$/.test(itemStr)) {
                alphabets.push(itemStr.toUpperCase());
                // Extract individual characters for concatenation
                for (let char of itemStr) {
                    allAlphabetChars.push(char.toLowerCase());
                }
            }
            // Otherwise, it's a special character
            else {
                specialCharacters.push(itemStr);
            }
        });

        // Create concatenation string with alternating caps in reverse order
        let concatString = "";
        if (allAlphabetChars.length > 0) {
            const reversedChars = allAlphabetChars.reverse();
            concatString = reversedChars.map((char, index) => {
                return index % 2 === 0 ? char.toLowerCase() : char.toUpperCase();
            }).join('');
        }

        // Response object
        const response = {
            is_success: true,
            user_id: "john_doe_17091999", // Replace with actual user ID logic
            email: "john@xyz.com", // Replace with actual email
            roll_number: "ABCD123", // Replace with actual roll number
            odd_numbers: oddNumbers,
            even_numbers: evenNumbers,
            alphabets: alphabets,
            special_characters: specialCharacters,
            sum: String(sumNumbers), // Return as string
            concat_string: concatString
        };

        // Send response with status 200
        res.status(200).json(response);

    } catch (error) {
        console.error('Error processing request:', error);
        res.status(500).json({
            is_success: false,
            error: "Internal server error"
        });
    }
});

// GET endpoint for testing
app.get('/', (req, res) => {
    res.json({
        message: "BFHL REST API is running!",
        endpoint: "/bfhl",
        method: "POST"
    });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({
        is_success: false,
        error: "Something went wrong!"
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

module.exports = app;