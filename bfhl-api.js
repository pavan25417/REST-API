const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());

// Health check
app.get("/", (req, res) => {
  res.json({
    message: "BFHL REST API is running!",
    endpoint: "/bfhl",
    method: "POST"
  });
});

// Main BFHL POST route
app.post("/bfhl", (req, res) => {
  try {
    const { data } = req.body;
    if (!data || !Array.isArray(data)) {
      return res.status(400).json({ is_success: false, error: "Invalid input" });
    }

    // Separate inputs
    const odd_numbers = [];
    const even_numbers = [];
    const alphabets = [];
    const special_characters = [];
    let sum = 0;

    data.forEach(item => {
      if (/^-?\\d+$/.test(item)) {
        // number (keep as string in output)
        const num = parseInt(item, 10);
        if (num % 2 === 0) {
          even_numbers.push(item);
        } else {
          odd_numbers.push(item);
        }
        sum += num;
      } else if (/^[a-zA-Z]+$/.test(item)) {
        alphabets.push(item.toUpperCase());
      } else {
        special_characters.push(item);
      }
    });

    // Concat string logic: reverse, alternating caps
    let concat_string = "";
    const lettersOnly = data.filter(x => /^[a-zA-Z]+$/.test(x)).join("");
    const reversed = lettersOnly.split("").reverse();

    reversed.forEach((ch, idx) => {
      concat_string += idx % 2 === 0
        ? ch.toUpperCase()
        : ch.toLowerCase();
    });

    // Response
    res.json({
      is_success: true,
      user_id: "john_doe_17091999",  
      email: "john@xyz.com",         
      roll_number: "ABCD123",       
      odd_numbers,
      even_numbers,
      alphabets,
      special_characters,
      sum: sum.toString(),
      concat_string
    });
  } catch (err) {
    res.status(500).json({ is_success: false, error: err.message });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
