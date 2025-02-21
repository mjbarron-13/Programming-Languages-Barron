import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [userChoice, setUserChoice] = useState(null);
  const [botChoice, setBotChoice] = useState("question");
  const [result, setResult] = useState("");
  const [history, setHistory] = useState({ userWins: 0, botWins: 0 });

  const choices = ["rock", "paper", "scissors"];

  // Fetch game history on load
  useEffect(() => {
    fetch("/api/history")
      .then((response) => response.json())
      .then((data) => setHistory(data));
  }, []);

  const handleClick = async (choice) => {
    setUserChoice(choice);
    setBotChoice("question"); // Initially show question mark
    setResult("");

    setTimeout(async () => {
      const response = await fetch("/api/play", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ userChoice: choice }),
      });

      if (response.ok) {
        const data = await response.json();
        setBotChoice(data.botChoice);
        setResult(data.result);
        setHistory(data.history); // Update history after the game
      }
    }, 2000);
  };

  return (
    <div className="container">
      <h1 className={`result ${result.split(" ").pop().replace(/[^a-zA-Z]/g, "").toLowerCase()}`}>
      {result ? result.toUpperCase() : "Make Your Move!"}
      </h1>

      {/* Display game history */}
      <div className="history">
        <p>User Wins: {history.userWins}</p>
        <p>Bot Wins: {history.botWins}</p>
      </div>

      {/* Choices */}
      <div className="choices">
        <h2>You</h2>
        <img src={`/${userChoice ? userChoice : "question"}.png`} alt="Your Choice" />

        <h2>Bot</h2>
        <img src={`/${botChoice}.png`} alt="Bot's Choice" />
      </div>

      {/* Selection Buttons */}
      <div className="buttons">
        {choices.map((choice) => (
          <button key={choice} onClick={() => handleClick(choice)}>
            <img src={`/${choice}.png`} alt={choice} />
          </button>
        ))}
      </div>
    </div>
  );
}

export default App;
