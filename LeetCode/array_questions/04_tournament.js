/**
 * all teams matches all teams
 * only two team begin and end each match
 *
 * if win gets  5 points
 *
 * [home, away]
 *
 * result = [0: away win, 1:home win]
 *
 * sample output = Python
 */

const competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"],
];

const results = [0, 0, 1];

function MyGetWinner(competitions, results) {
  let resultIdex = 0;
  let scoreBoard = {};
  let currentWinningTeam = "";

  for (const competition of competitions) {
    const [home, away] = competition;

    let isHomeWon = results[resultIdex];

    const winner = isHomeWon ? home : away;

    if (!(winner in scoreBoard)) {
      scoreBoard[winner] = 1;
    } else {
      scoreBoard[winner]++;
    }

    if (!currentWinningTeam) currentWinningTeam = winner;

    if (currentWinningTeam && scoreBoard[winner] > scoreBoard[currentWinningTeam]) {
      currentWinningTeam = winner;
    }

    resultIdex++;
  }

  return currentWinningTeam;
}

console.log(MyGetWinner(competitions, results));
