package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strings"
	"time"
)

var words = []string{"apple", "grape", "lemon", "peach", "mango", "chili", "berry", "olive", "melon", "guava"}

func getRandomWord() string {
	rand.Seed(time.Now().UnixNano())
	return words[rand.Intn(len(words))]
}

func checkWord(guess, target string) string {
	result := []rune{'⬜', '⬜', '⬜', '⬜', '⬜'}
	used := make([]bool, 5)

	for i := 0; i < 5; i++ {
		if guess[i] == target[i] {
			result[i] = '🟩'
			used[i] = true
		}
	}

	for i := 0; i < 5; i++ {
		if guess[i] != target[i] {
			for j := 0; j < 5; j++ {
				if guess[i] == target[j] && !used[j] {
					result[i] = '🟨'
					used[j] = true
					break
				}
			}
		}
	}

	return string(result)
}

func playGame() {
	targetWord := getRandomWord()
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("Welcome to Go-Wordle! Guess the 5-letter word.")
	for attempts := 0; attempts < 6; attempts++ {
		fmt.Print("Enter guess: ")
		input, _ := reader.ReadString('\n')
		guess := strings.TrimSpace(strings.ToLower(input))

		if len(guess) != 5 {
			fmt.Println("Word must be exactly 5 letters long.")
			continue
		}

		feedback := checkWord(guess, targetWord)
		fmt.Println(feedback)

		if guess == targetWord {
			fmt.Println("🎉 You guessed it right! Congratulations!")
			return
		}
	}

	fmt.Println("😢 Out of attempts! The word was:", targetWord)
}

func main() {
	for {
		playGame()
		fmt.Print("Do you want to play again? (y/n): ")
		var response string
		fmt.Scanln(&response)
		if strings.ToLower(response) != "y" {
			fmt.Println("Thanks for playing!")
			break
		}
	}
}
