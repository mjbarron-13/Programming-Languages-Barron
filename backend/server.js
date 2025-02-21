const express = require("express");
const cors = require("cors");

const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

// Game history tracking
let userWins = 0;
let botWins = 0;

// Route to play the game
app.post("/api/play", (req, res) => {
  const { userChoice } = req.body;
  const choices = ["rock", "paper", "scissors"];
  const botChoice = choices[Math.floor(Math.random() * choices.length)];

  let result = "";

  if (userChoice === botChoice) {
    result = "It's a tie!";
  } else if (
    (userChoice === "rock" && botChoice === "scissors") ||
    (userChoice === "paper" && botChoice === "rock") ||
    (userChoice === "scissors" && botChoice === "paper")
  ) {
    result = "You Win!";
    userWins++;
  } else {
    result = "You Lose!";
    botWins++;
  }

  res.json({
    botChoice,
    result,
    history: { userWins, botWins }
  });
});

// Route to get game history
app.get("/api/history", (req, res) => {
  res.json({ userWins, botWins });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
