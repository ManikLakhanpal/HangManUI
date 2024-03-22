const words = ['hangman', 'javascript', 'programming', 'computer', 'code']; 

let chosenWord = words[Math.floor(Math.random() * words.length)]; 
let guessedWord = Array(chosenWord.length).fill('_'); 

const wordToGuessElement = document.getElementById('wordToGuess');
const lettersGuessedElement = document.getElementById('lettersGuessed');
const hangmanGraphicsElement = document.getElementById('hangmanGraphics');

wordToGuessElement.textContent = guessedWord.join(' '); 

function Guessed(letter) {
  if (!guessedWord.includes('_')) {
    return; 
  }

  if (chosenWord.includes(letter)) { 
    chosenWord.split('').forEach((wordLetter, index) => {
      if (wordLetter === letter) {
        guessedWord[index] = letter; 
      }
    });
    wordToGuessElement.textContent = guessedWord.join(' '); 
    if (!guessedWord.includes('_')) {
      alert('Congratulations! You guessed the word: ' + chosenWord);
    }
  } else {
    lettersGuessedElement.textContent += letter + ' '; 
    let hangManParts = ['head', 'body', 'arm-left', 'arm-right', 'leg-left', 'leg-right'];  
    // Here you can implement logic for drawing Hangman graphics
  }
}
