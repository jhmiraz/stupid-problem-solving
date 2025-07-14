import java.util.Scanner;
import java.util.Random;

public class ninja {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();

        int userScore = 0;
        int computerScore = 0;
        int round = 1;

        System.out.println("Welcome to rock paper scissors!");
        System.out.println("First to 5 point wints let's go");

        while (userScore < 5 && computerScore < 5) {
            System.out.println("📦 Round  " + round);
            System.out.println("Enter your move (rock/paper/scissors): ");
            String userMove = sc.next().toLowerCase();

            if (!userMove.equals("rock") && !userMove.equals("paper") && !userMove.equals("sceissors")) {
                System.out.println("INVALID MOVE TRY AGAING");
                continue;

            }

            String[] moves = { "rock", "paper", "scissors" };
            String computerMove = moves[rand.nextInt(3)];
            System.out.println("🤖 Computer chose: " + computerMove);

            if (userMove.equals(computerMove)) {
                System.out.println("⚔️ It's a draw! ");
            } else if ((userMove.equals("rock") && computerMove.equals("scissors"))
                    || (userMove.equals("paper") && computerMove.equals("rock"))
                    || (userMove.equals("scissors") && computerMove.equals("paper"))) {
                System.out.println("✅ You win this round!");
                userScore++;
            } else {
                System.out.println("❌ Computer wins this round!");
                computerScore++;
            }

            System.out.println("Score - You: " + userScore + " | Computer: " + computerScore);
            System.out.println("------------------------------------------------");
            round++;

        }

        if (userScore == 5) {
            System.out.println("🎉 YOU WON THE GAME!");
        } else {
            System.out.println("💻 COMPUTER WON THE GAME!");
        }

        System.out.print("Do you want to play again? (yes/no): ");
        String playAgain = sc.next().toLowerCase();

        if (playAgain.equals("yes")) {
            main(null); // restart the game
        } else {
            System.out.println("👋 Thanks for playing!");
        }

        sc.close();

    }
}