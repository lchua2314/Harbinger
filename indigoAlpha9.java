package AlphaTest;

import java.io.*;
import java.util.Scanner;
import java.util.Random;
import java.text.DecimalFormat;

public class indigoAlpha9
{
    public static void main(String[] args) throws IOException
    {
        int keepValid = 0;
        String command, anotherCommand;
        Scanner kb = new Scanner(System.in);
        System.out.println("-------------------------------------Indigo Alpha 9/ia9------------------------------------");
        System.out.print("Please, enter a command: ");
        command = kb.nextLine().toLowerCase();
        while (keepValid==0)
        {
            if (command.equals("calculator"))
            {
                calculator();
                System.out.print("\nWould you like to use another command? "
                		+ "Note: Any other input that does not answer the "
                		+ "question will make me run the command again. ");
                anotherCommand = kb.nextLine().toLowerCase();
                if (anotherCommand.equals("yes") || anotherCommand.equals("y"))
                {
                    System.out.println("Please, enter a command: ");
                    command = kb.nextLine().toLowerCase();
                    continue;
                }
                else if (anotherCommand.equals("no") || anotherCommand.equals("n"))
                {
                    System.out.print("Until next time.");
                    System.exit(0);
                }
            }
            else if (command.equals("help"))
            {
                System.out.println("List of commands:");
                System.out.println("1. help - Displays all commands.");
                System.out.println("2. calculator - Runs a calculator.");
                System.out.println("3. exit - Closes the program.");
                System.out.println("4. palindrome - Runs a palindrome checker");
                System.out.println("5. rpsg - Runs the "
                		           + "rock-paper-scissors game that you the computer.");
                System.out.println("6. prime checker - Checks if a number is prime or not.");
                System.out.println("7. seasons - Checks the seasons of a given date.");
                System.out.println("8. tcts - (Time Conversion to Seconds)");
                System.out.println("9. tcthms - (Time Conversion to Hours, "
                		           + "Minutes, and Seconds)");
                System.out.println("10. temp - Stores and converts temperature"
                		           + " values and scales.");
                System.out.println("11. RNG - Finds random values "
                		           + "and returns random outcomes.");
                System.out.println("12. files - Allows user to open, edit, and display"
                		           + " text document files.");
                System.out.print("\nWould you like to use another command? "
                		           + "Note: Any other input that does not answer the "
                		           + "question will make me run the command again. ");
                anotherCommand = kb.nextLine().toLowerCase();
                if (anotherCommand.equals("yes") || anotherCommand.equals("y"))
                {
                    System.out.println("Please, enter a command: ");
                    command = kb.nextLine().toLowerCase();
                    continue;
                }
                else if (anotherCommand.equals("no") || anotherCommand.equals("n"))
                {
                    System.out.print("Closing program...");
                    System.exit(0);
                }   
            }
            else if (command.equals("files"))
            {
                files();
                System.out.print("\nWould you like to use another command? "
                		+ "Note: Any other input that does not answer the "
                		+ "question will make me run the command again. ");
                anotherCommand = kb.nextLine().toLowerCase();
                if (anotherCommand.equals("yes") || anotherCommand.equals("y"))
                {
                    System.out.println("Please, enter a command: ");
                    command = kb.nextLine().toLowerCase();
                    continue;
                }
                else if (anotherCommand.equals("no") || anotherCommand.equals("n"))
                {
                    System.out.print("Until next time.");
                    System.exit(0);
                }
            }
            else if (command.equals("rng"))
            {
                rng();
                System.out.print("\nWould you like to use another command? "
                		+ "Note: Any other input that does not answer the "
                		+ "question will make me run the command again. ");
                anotherCommand = kb.nextLine().toLowerCase();
                if (anotherCommand.equals("yes") || anotherCommand.equals("y"))
                {
                    System.out.println("Please, enter a command: ");
                    command = kb.nextLine().toLowerCase();
                    continue;
                }
                else if (anotherCommand.equals("no") || anotherCommand.equals("n"))
                {
                    System.out.print("Until next time.");
                    System.exit(0);
                }
            }
            else if (command.equals("temp"))
            {
                temp();
                System.out.print("\nWould you like to use another command? "
                		+ "Note: Any other input that does not answer the "
                		+ "question will make me run the command again. ");
                anotherCommand = kb.nextLine().toLowerCase();
                if (anotherCommand.equals("yes") || anotherCommand.equals("y"))
                {
                    System.out.println("Please, enter a command: ");
                    command = kb.nextLine().toLowerCase();
                    continue;
                }
                else if (anotherCommand.equals("no") || anotherCommand.equals("n"))
                {
                    System.out.print("Until next time.");
                    System.exit(0);
                }
            }
            else if (command.equals("palindrome"))
            {
                palindrome();
                System.out.print("\nWould you like to use another command? "
                		+ "Note: Any other input that does not answer the "
                		+ "question will make me run the command again. ");
                anotherCommand = kb.nextLine().toLowerCase();
                if (anotherCommand.equals("yes") || anotherCommand.equals("y"))
                {
                    System.out.println("Please, enter a command: ");
                    command = kb.nextLine().toLowerCase();
                    continue;
                }
                else if (anotherCommand.equals("no") || anotherCommand.equals("n"))
                {
                    System.out.print("Until next time.");
                    System.exit(0);
                }
            }
            else if (command.equals("tcts"))
            {
                TCTS();
                System.out.print("\nWould you like to use another command? "
                		+ "Note: Any other input that does not answer the "
                		+ "question will make me run the command again. ");
                anotherCommand = kb.nextLine().toLowerCase();
                if (anotherCommand.equals("yes") || anotherCommand.equals("y"))
                {
                    System.out.println("Please, enter a command: ");
                    command = kb.nextLine().toLowerCase();
                    continue;
                }
                else if (anotherCommand.equals("no") || anotherCommand.equals("n"))
                {
                    System.out.print("Until next time.");
                    System.exit(0);
                }
            }
            else if (command.equals("tcthms"))
            {
            	TCTHMS();
                System.out.print("\nWould you like to use another command? "
                		+ "Note: Any other input that does not answer the "
                		+ "question will make me run the command again. ");
                anotherCommand = kb.nextLine().toLowerCase();
                if (anotherCommand.equals("yes") || anotherCommand.equals("y"))
                {
                    System.out.println("Please, enter a command: ");
                    command = kb.nextLine().toLowerCase();
                    continue;
                }
                else if (anotherCommand.equals("no") || anotherCommand.equals("n"))
                {
                    System.out.print("Until next time.");
                    System.exit(0);
                }
            }
            else if (command.equals("seasons"))
            {
                Seasons();
                System.out.print("\nWould you like to use another command? "
                		+ "Note: Any other input that does not answer the "
                		+ "question will make me run the command again. ");
                anotherCommand = kb.nextLine().toLowerCase();
                if (anotherCommand.equals("yes") || anotherCommand.equals("y"))
                {
                    System.out.println("Please, enter a command: ");
                    command = kb.nextLine().toLowerCase();
                    continue;
                }
                else if (anotherCommand.equals("no") || anotherCommand.equals("n"))
                {
                    System.out.print("Until next time.");
                    System.exit(0);
                }
            }
            else if (command.equals("rpsg"))
            {
            	rpsg();
                System.out.print("\nWould you like to use another command? "
                		+ "Note: Any other input that does not answer the "
                		+ "question will make me run the command again. ");
                anotherCommand = kb.nextLine().toLowerCase();
                if (anotherCommand.equals("yes") || anotherCommand.equals("y"))
                {
                    System.out.println("Please, enter a command: ");
                    command = kb.nextLine().toLowerCase();
                    continue;
                }
                else if (anotherCommand.equals("no") || anotherCommand.equals("n"))
                {
                    System.out.print("Until next time.");
                    System.exit(0);
                }
            }
            else if (command.equals("prime checker"))
            {
            	PrimeChecker();
                System.out.print("\n\nWould you like to use another command? "
                		+ "Note: Any other input that does not answer the "
                		+ "question will make me run the command again. ");
                anotherCommand = kb.nextLine().toLowerCase();
                if (anotherCommand.equals("yes") || anotherCommand.equals("y"))
                {
                    System.out.println("Please, enter a command: ");
                    command = kb.nextLine().toLowerCase();
                    continue;
                }
                else if (anotherCommand.equals("no") || anotherCommand.equals("n"))
                {
                    System.out.print("Until next time.");
                    System.exit(0);
                }
            }
            else if (command.equals("exit"))
            {
                System.out.println("Until next time.");
                System.exit(0);
            }
            else
            {
                System.out.println("Not a valid command!");
                System.out.print("Please, enter a valid command: ");
                command = kb.nextLine().toLowerCase();
            }
        }
    }
    public static void calculator()
    {
    	int firstNum, secondNum;
    	String operator;
        Scanner kb = new Scanner(System.in);
        System.out.println("Please enter an operator (+,-,* or /):");
        operator = kb.nextLine();
        System.out.println("Please enter the first number:");
        firstNum = kb.nextInt();
        System.out.println("Please enter the second number:");
        secondNum = kb.nextInt();
        System.out.println("Is " + firstNum + " " + operator + " " + secondNum +  
        		           " what you want me to compute?");
        
    }
    public static void palindrome()
    {
        String pal="0"; 
        int i, j, counter=0;
        Scanner kb = new Scanner(System.in);
        
        while (!pal.equals(""))
        {
        	System.out.println("You are now using the Palindrome Checker!");
            System.out.println("Please enter a word, phrase, " 
                               + "or sentence (blank line " 
                               + "to stop): ");
            pal = kb.nextLine().toLowerCase().replaceAll("\\d+","")
        	    .replaceAll("[\\W]", "");
        
            if (pal.equals(""))
            {
                System.out.printf("Congratulations! You found %d "
    			          + "palindrome(s)!\n", counter);
                System.out.println("Thank you for "
    			           + "using the Palindrome Checker!");
    	        break;
            }
        
            i=0; 
            j=pal.length()-1;
            int x = 0;
            int keepFlow;

        	
            while (x==0)
            {           
                if (i==j)
                {
                    System.out.println("This is a palindrome!\n");
                    counter++;
                    break;
                }
                while (i <= j)
                {
                    char intoChar, reverseChar;
                    intoChar=pal.charAt(i);
                    reverseChar=pal.charAt(j);                    
                    
                    if (intoChar == reverseChar)
                    {
                        i++; 
                        j--;
                        keepFlow = 0;
                    }
                    else
                    {
                        keepFlow = 1;
                    }
                    if (keepFlow==0 && i>=j)
                    {
                        System.out.println("This is a palindrome!\n");
                        counter++;
                        x++;
                        break;
                    }
                    
                    if (keepFlow==1)
                    {
                        System.out.println("Unforunately, this is not a palindrome.\n");
                        x++;
                        break;
                    }
                }
            }
        } 
    }
    
    public static void rpsg()
    {
        playAgain();
    }
    public static void playAgain ()
    {
        String realCompChoice, realUserChoice;
        realCompChoice = computerChoice();
        realUserChoice = userChoice();
        determineWinner(realCompChoice, realUserChoice);
    }
    public static String computerChoice ()
    {
        String compChoice;
        int randomNumber;
        Random oneOfThreeComp = new Random();
        randomNumber = oneOfThreeComp.nextInt(3)+1;
        if (randomNumber == 1)
           compChoice = "rock";
        else if (randomNumber == 2)
           compChoice = "paper";
        else
           compChoice = "scissors";
        return compChoice;
    }
    public static String userChoice ()
    {
        String personChoice, convertCase;
        Scanner kb = new Scanner(System.in);
        System.out.print("Enter rock, paper, or scissors: ");
        personChoice = kb.nextLine();
        convertCase = personChoice.toLowerCase();
        while (isValidChoice(convertCase) == false)
        {
            System.out.print("Invalid input, enter rock, " 
                             + "paper, or scissors: ");
            personChoice = kb.nextLine();
            convertCase = personChoice.toLowerCase();
        }
        return personChoice;
    }
    public static boolean isValidChoice (String choice)
    {
        boolean valid;
        if (choice.equals("scissors") || choice.equals("paper") 
            || choice.equals("rock"))
           valid = true;
        else
           valid = false;
        return valid;
    }
    public static void determineWinner (String computer, String user)
    {
        String playAgain;
    	Scanner keyboard = new Scanner(System.in);
        if (computer.equals("scissors") 
            && user.toLowerCase().equals("paper"))
        {
            System.out.println("The computer's choice was scissors.\n" + 
            		       "The user's choice was " 
                               + user + ".\n" + "\n"
            		       + "Scissors cuts paper.\n" 
            		       + "The computer wins!\n" + "\n"
            		       + "Play again? (y/n)");
            playAgain = keyboard.nextLine().toLowerCase();
            while (!playAgain.equals("yes") && !playAgain.equals("y") &&
            	   !playAgain.equals("no") && !playAgain.equals("n"))
               playAgain = keyboard.nextLine().toLowerCase();
            if (playAgain.equals("yes") || playAgain.equals("y"))
               playAgain();
            else if (playAgain.equals("no") || playAgain.equals("n"))
               return;
        }
        else if (computer.equals("scissors") 
                 && user.toLowerCase().equals("rock"))
        {
            System.out.println("The computer's choice was scissors.\n" + 
            		       "The user's choice was " 
                               + user + ".\n" + "\n"
            		       + "Rock smashes scissors.\n" 
            		       + "The user wins!\n" + "\n"
            		       + "Play again? (y/n)");
            playAgain = keyboard.nextLine().toLowerCase();
            while (!playAgain.equals("yes") && !playAgain.equals("y") &&
            	   !playAgain.equals("no") && !playAgain.equals("n"))
               playAgain = keyboard.nextLine().toLowerCase();
            if (playAgain.equals("yes") || playAgain.equals("y"))
               playAgain();
            else if (playAgain.equals("no") || playAgain.equals("n"))
               return;
        }
        else if (computer.equals("rock") 
                 && user.toLowerCase().equals("paper"))
        {
            System.out.println("The computer's choice was rock.\n" + 
            		       "The user's choice was " 
                               + user + ".\n" + "\n"
            		       + "Paper wraps rock.\n" 
            		       + "The user wins!\n" + "\n"
            		       + "Play again? (y/n)");
            playAgain = keyboard.nextLine().toLowerCase();
            while (!playAgain.equals("yes") && !playAgain.equals("y") &&
            	   !playAgain.equals("no") && !playAgain.equals("n"))
               playAgain = keyboard.nextLine().toLowerCase();
            if (playAgain.equals("yes") || playAgain.equals("y"))
               playAgain();
            else if (playAgain.equals("no") || playAgain.equals("n"))
               return;
        }
        else if (computer.equals("rock") 
                 && user.toLowerCase().equals("scissors"))
        {
            System.out.println("The computer's choice was rock.\n" + 
            		       "The user's choice was " 
                               + user + ".\n" + "\n"
            		       + "Rock smashes scissors.\n" 
            		       + "The computer wins!\n" + "\n"
            		       + "Play again? (y/n)");
            playAgain = keyboard.nextLine().toLowerCase();
            while (!playAgain.equals("yes") && !playAgain.equals("y") &&
            	   !playAgain.equals("no") && !playAgain.equals("n"))
               playAgain = keyboard.nextLine().toLowerCase();
            if (playAgain.equals("yes") || playAgain.equals("y"))
               playAgain();
            else if (playAgain.equals("no") || playAgain.equals("n"))
               return;
        }
        else if (computer.equals("paper") 
                 && user.toLowerCase().equals("rock"))
        {
            System.out.println("The computer's choice was paper.\n" + 
            		       "The user's choice was " 
                               + user + ".\n" + "\n"
            		       + "Paper wraps rock.\n"
            		       + "The computer wins!\n" + "\n"
            		       + "Play again? (y/n)");
            playAgain = keyboard.nextLine().toLowerCase();
            while (!playAgain.equals("yes") && !playAgain.equals("y") &&
            	   !playAgain.equals("no") && !playAgain.equals("n"))
               playAgain = keyboard.nextLine().toLowerCase();
            if (playAgain.equals("yes") || playAgain.equals("y"))
               playAgain();
            else if (playAgain.equals("no") || playAgain.equals("n"))
               return;
        }
        else if (computer.equals("paper") 
                 && user.toLowerCase().equals("scissors"))
        {
            System.out.println("The computer's choice was paper.\n" + 
            		       "The user's choice was " 
                               + user + ".\n" + "\n"
            		       + "Scissors cuts paper.\n" 
            		       + "The user wins!\n" + "\n"
            		       + "Play again? (y/n)");
            playAgain = keyboard.nextLine().toLowerCase();
            while (!playAgain.equals("yes") && !playAgain.equals("y") &&
            	   !playAgain.equals("no") && !playAgain.equals("n"))
               playAgain = keyboard.nextLine().toLowerCase();
            if (playAgain.equals("yes") || playAgain.equals("y"))
               playAgain();
            else if (playAgain.equals("no") || playAgain.equals("n"))
               return;
        }
        else if (user.toLowerCase().equals(computer))
        {
            System.out.println("The computer's choice was " 
                               + computer + ".\n" 
            		       + "The user's choice was " 
                               + user + ".\n");
            System.out.println("The game is tied!\n"
                               + "Get ready to play again...");
            playAgain();
        }
    }
    public static void PrimeChecker()
    {
        int num;
        Scanner kb = new Scanner(System.in);
        System.out.print("Enter a number: ");
        num = kb.nextInt();
        if (isPrime(num)==true)
           System.out.print("That is a prime number.");
        else if (isPrime(num)==false)
           System.out.print("That is not a prime number.");
    }
    
    public static boolean isPrime(int num) 
    {
        int i;
        for (i = 2; i < num; i++) 
        {
            if (num % i == 0) 
            {
                return false;
            }
        }
        return true;
    }
    public static void Seasons()
    {
        int day, month;
    	Scanner kb = new Scanner(System.in);
    	System.out.print("enter month (1-12): ");
    	month = kb.nextInt();
    	switch (month)
    	{
    	    case 1:
    	    {
    	        System.out.print("enter day (1-31): ");
    	        day = kb.nextInt();
    	        if (day >= 1 && day <= 31)
    	           System.out.print(month + "/" + day + " is in the Winter season.");
    	        else
    	           System.out.print("Invalid day!"); 
    	        break;
    	    }
    	    case 2:
    	    {
    	        System.out.print("enter day (1-28): ");
    	        day = kb.nextInt();
    	        if (day >= 1 && day <= 28)
    	           System.out.print(month + "/" + day + " is in the Winter season.");
    	        else
    	           System.out.print("Invalid day!");
    	        break; 
    	    }
    	    case 3:
    	    {
    	        System.out.print("enter day (1-31): ");
    	        day = kb.nextInt();
    	        if (day >= 1 && day <= 20)
    	           System.out.print(month + "/" + day + " is in the Winter season.");
    	        else if (day >= 21 && day <= 31)
    	           System.out.print(month + "/" + day + " is in the Spring season.");
    	        else
    	           System.out.print("Invalid day!"); 
    	        break;
    	    }
    	    case 4:
    	    {
    	        System.out.print("enter day (1-30): ");
    	        day = kb.nextInt();
    	        if (day >= 1 && day <= 30)
    	           System.out.print(month + "/" + day + " is in the Spring season.");
    	        else
    	           System.out.print("Invalid day!");
    	        break;
    	    }
    	    case 5:
    	    {
    	        System.out.print("enter day (1-31): ");
    	        day = kb.nextInt();
    	        if (day >= 1 && day <= 31)
    	           System.out.print(month + "/" + day + " is in the Spring season.");
    	        else
    	           System.out.print("Invalid day!");
    	        break;
    	    }
    	    case 6:
    	    {
    	        System.out.print("enter day (1-30): ");
    	        day = kb.nextInt();
    	        if (day >= 1 && day <= 20)
    	           System.out.print(month + "/" + day + " is in the Spring season.");
    	        else if (day >= 21 && day <= 30)
    	           System.out.print(month + "/" + day + " is in the Summer season.");
    	        else
    	           System.out.print("Invalid day!"); 
    	        break;
    	    }
    	    case 7:
    	    {
    	        System.out.print("enter day (1-31): ");
    	        day = kb.nextInt();
    	        if (day >= 1 && day <= 31)
    	           System.out.print(month + "/" + day + " is in the Summer season.");
    	        else
    	           System.out.print("Invalid day!"); 
    	        break;
    	    }
    	    case 8:
    	    {
    	        System.out.print("enter day (1-31): ");
    	        day = kb.nextInt();
    	        if (day >= 1 && day <= 31)
    	           System.out.print(month + "/" + day + " is in the Summer season.");
    	        else
    	           System.out.print("Invalid day!"); 
    	        break;
    	    }
    	    case 9:
    	    {
    	        System.out.print("enter day (1-30): ");
    	        day = kb.nextInt();
    	        if (day >= 1 && day <= 20)
    	           System.out.print(month + "/" + day + " is in the Summer season.");
    	        else if (day >= 21 && day <= 30)
    	           System.out.print(month + "/" + day + " is in the Fall season.");
    	        else
    	           System.out.print("Invalid day!");
    	        break;
    	    }
    	    case 10:
    	    {
    	        System.out.print("enter day (1-31): ");
    	        day = kb.nextInt();
    	        if (day >= 1 && day <= 31)
    	           System.out.print(month + "/" + day + " is in the Fall season.");
    	        else
    	           System.out.print("Invalid day!"); 
    	        break;
    	    }
    	    case 11:
    	    {
    	        System.out.print("enter day (1-30): ");
    	        day = kb.nextInt();
    	        if (day >= 1 && day <= 30)
    	           System.out.print(month + "/" + day + " is in the Fall season.");
    	        else
    	           System.out.print("Invalid day!"); 
    	        break;
    	    }
    	    case 12:
    	    {
    	        System.out.print("enter day (1-31): ");
    	        day = kb.nextInt();
    	        if (day >= 1 && day <= 20)
    	           System.out.print(month + "/" + day + " is in the Fall season.");
    	        else if (day >= 21 && day <= 31)
    	           System.out.print(month + "/" + day + " is in the Winter season.");
    	        else
    	           System.out.print("Invalid day!");
    	        break;
    	    }
    	    default:
    	       System.out.print("Invalid month!");
        }
    }
    public static void TCTS()
    {
        int hours, minutes, seconds, totalSeconds;
    	Scanner keyboard = new Scanner(System.in);
    	System.out.print("enter hours: ");
    	hours = keyboard.nextInt();
    	System.out.print("enter minutes: ");
    	minutes = keyboard.nextInt();
    	System.out.print("enter seconds: ");
    	seconds = keyboard.nextInt(); 
        totalSeconds = hours * 3600 + minutes * 60 + seconds;
   	    System.out.print(hours + " hours, " + minutes + 
   	                     " minutes, " + seconds + 
   	                     " seconds is equivalent to " + 
   	                     totalSeconds + " seconds.");  
    }
    public static void TCTHMS()
    {
  	    int hours, minutes, seconds, totalSeconds;
    	Scanner keyboard = new Scanner(System.in);
    	System.out.print("enter total seconds: ");
    	totalSeconds = keyboard.nextInt();
    	hours = totalSeconds / 3600;
    	minutes = ( totalSeconds - hours * 3600 ) / 60;
        seconds = totalSeconds - ( hours * 3600 + minutes * 60 ) ;
    	System.out.print(hours + " hours, " + minutes + 
    	                 " minutes, " + seconds + 
    	                 " seconds is equivalent to " + 
    	                 totalSeconds + " seconds.");  
    }
 	public static void temp()
    {
  	    int keepFlow = 0, keepSecondFlow = 0;
        double tempValue, newValue;
        String tempScale, validate, command, newScale;
        Scanner kb = new Scanner(System.in);
        System.out.println("This program allows you to set, display, "
    		   		       + "and convert temperatures (F and C).");
        System.out.print("Please enter the number value of the temperature"
    		   		     + " with it rounded to the tenths place: ");
        tempValue = kb.nextDouble();
        kb.nextLine();
        System.out.print("Please enter the scale of the temperature: ");
        tempScale = kb.nextLine().toUpperCase();
        while (!tempScale.equals("F") && !tempScale.equals("C"))
        {
    	    System.out.println("Invalid scale! Please use 'F' or 'C'.");
    		tempScale = kb.nextLine().toUpperCase();
        }
        System.out.println("Is your temperature " + tempValue + " "
    				       + tempScale + "?");
        while (keepFlow == 0)
        {
            validate = kb.nextLine().toUpperCase();
    		if (validate.equals("Y") || validate.equals("YES"))
    		   break;
    		else if (validate.equals("N") || validate.equals("NO"))
    		{
    		    tempValue = askTempValue();
    		    tempScale = askTempScale();
    		    System.out.println("Your new temperature is " 
    		    			       + tempValue + " " + tempScale);
    		    System.out.println("Is this the temperature you want?");
    		    validate = kb.nextLine().toUpperCase();
    		    continue;
    		}
    		else
    		   continue;
        }
        Temperature t1 = new Temperature(tempValue, tempScale);
        System.out.println("What would you like to do with the "
    		   		       + "temperature? (Note: 'help' lists all commands): ");
        while (keepSecondFlow == 0)
        {   
    	    command = kb.nextLine().toUpperCase();
    	    if (command.equals("HELP"))
    	    {
    		    System.out.println("1. Help - Lists all commands.");
    		    System.out.println("2. Exit - Exits the Temperature program.");
    			System.out.println("3. GetValue - Retrieves temperature value.");
    			System.out.println("4. GetScale - Retrieves temperature scale.");
    			System.out.println("5. EquF - Displays the equivalent Celsius value to "
    				   		       + "Fahrenheit");
    		    System.out.println("6. EquC - Displays the equivalent Fahrenheit "
    	 	   		               + "value to "
    						       + "Celsius");
    			System.out.println("7. SetValue - Changes an old temperature value "
    		   		               + "for a new one.");
    			System.out.println("8. SetScale - Changes an old temperature scale "
    				   		       + "for a new one.");
    			System.out.println("9. SetBoth - Changes both old temperature value "
    						       + "for new ones.");
    		}
    	    else if (command.equals("GETVALUE"))
         	   System.out.println(t1.getValue());
    	    else if (command.equals("GETSCALE"))
    		   System.out.println(t1.getScale());
    		else if (command.equals("EXIT"))
    		   keepSecondFlow++;
    		else if (command.equals("EQUF"))
    		{
    		    if (t1.getScale().equals("C"))
    		       System.out.println(t1.getValue() + " C = " 
    				                  + t1.getFahrenheit() + " F.");
	            else
	               System.out.println("The value is already in Fahrenheit!");
    	    }
    	    else if (command.equals("EQUC"))
    		{
    		    if (t1.getScale().equals("F"))
    		       System.out.println(t1.getValue() + " F = " 
    				                  + t1.getFahrenheit() + " C.");
	            else
	               System.out.println("The value is already in Celsius!");
    	    }
    	    else if (command.equals("SETVALUE"))
    		{
    		    System.out.println("Setting " + t1.getValue() + " to: ");
    		    newValue = kb.nextDouble();
    		    t1.setValue(newValue);
    			System.out.println("New value is: " + t1.getValue());
    	    }
    		else if (command.equals("SETSCALE"))
    		{
    		    System.out.println("Setting " + t1.getScale() + " to: ");
    		    newScale = kb.nextLine();
    		    t1.setScale(newScale);
    			System.out.println("New scale is: " + t1.getScale());
    	    }
    	    else if (command.equals("SETBOTH"))
    	    {
    		    System.out.println("Setting " + t1.getValue() + " to: ");
    		    newValue = kb.nextDouble();
    			kb.nextLine();
    			t1.setValue(newValue);
    			System.out.println("New value is: " + t1.getValue());
    			System.out.println("Setting " + t1.getScale() + " to: ");
    			newScale = kb.nextLine();
    			t1.setScale(newScale);
    			System.out.println("New value is: " + t1.getScale());
    		}
    		else
    		   System.out.println("Invalid command! Use 'help' for the list of commands.");
    	}
    }
    public static double askTempValue()
    {
        double tempValue;
    	Scanner kb = new Scanner(System.in);
    	System.out.print("Please enter the number value of the temperature"
	   		             + " with it rounded to the tenths place:");
	    return tempValue = kb.nextDouble();
    }
    public static String askTempScale()
    {
        String tempScale;
    	int keepFlow = 0;
    	Scanner kb = new Scanner(System.in);
    	System.out.print("Please enter the scale of the temperature:");
    	tempScale = kb.nextLine().toUpperCase();
    	while (!tempScale.equals("F") && !tempScale.equals("C"))
    	{
		    System.out.println("Invalid scale! Please use 'F' or 'C'.");
		    tempScale = kb.nextLine().toUpperCase();
		}
        return tempScale;
    }
    public static void rng()
    {
        boolean secondLoopInfinite = true;
    	int[] numOfRan;
    	int numOfNums, nextRanNum;
    	String isValid, answer;
    	Scanner kb = new Scanner(System.in);
    	System.out.print("Enter the number of random "
    		   		     + "numbers you would like: ");
    	numOfNums = kb.nextInt();
    	numOfRan = new int[numOfNums];
    	for (int count = 0; count < numOfNums; count++)
    	{
    	    System.out.print("Random Number #" + (count + 1) + ": ");
    		nextRanNum = kb.nextInt();
    		numOfRan[count] = nextRanNum;
    	}
    	kb.nextLine();
    	System.out.print("Are these the numbers you would like to"
    		   		       + " randomize? ");
    	isValid = kb.nextLine().toLowerCase();
    	while (!isValid.equals("yes") && !isValid.equals("no") 
    		   && !isValid.equals("y") && !isValid.equals("n"))
        {
             System.out.println("Invalid response!");
             System.out.print("Please give me a 'yes' or 'no' answer: ");
             isValid = kb.nextLine().toLowerCase();
        }
        if (isValid.equals("yes") || isValid.equals("y"))
    	   rngCal(numOfRan);
    	else if (isValid.equals("no") || isValid.equals("n"))
    	{   
    	    rngGetAgain();
    	    rngCal(numOfRan);
    	}
    	while (secondLoopInfinite = true)
        {   
    	    System.out.print("Would you like another random number? ");
    		answer = kb.nextLine();
    		if (answer.equals("yes") || answer.equals("y"))
    		   rngCal(numOfRan);
    		else if (answer.equals("no") || answer.equals("n"))
    		   break;
    		else
    		   System.out.println("Invalid answer!");
        }
    }
    public static void rngCal(int[] nums)
    {
        int length = nums.length, chosen;
        Random rd = new Random();
        chosen = rd.nextInt(length);
        System.out.println(nums[chosen] + " is the chosen random number!");
    }
    public static int[] rngGetAgain()//In progress
    {
        int[] numOfRan;
    	int numOfNums, nextRanNum;
    	String isValid, answer;
    	Scanner kb = new Scanner(System.in);
    	System.out.print("Enter the number of random numbers you would like: ");
    	numOfNums = kb.nextInt();
    	numOfRan = new int[numOfNums];
    	for (int count = 0; count < numOfNums; count++)
    	{
    	    System.out.print("Random Number #" + (count + 1) + ": ");
    		nextRanNum = kb.nextInt();
    		numOfRan[count] = nextRanNum;
    	}
    	kb.nextLine();
    	System.out.print("Are these the numbers you would like to randomize?");
        isValid = kb.nextLine().toLowerCase();
       	while (!isValid.equals("yes") && !isValid.equals("no") 
       		   && !isValid.equals("y") && !isValid.equals("n"))
        {
            System.out.println("Invalid response!");
            System.out.print("Please give me a 'yes' or 'no' answer: ");
            isValid = kb.nextLine().toLowerCase();
        }
        if (isValid.equals("no") || isValid.equals("n"))
       	   rngGetAgain();
    	return numOfRan;
    }
    public static void files() throws IOException
    {
    	boolean keepFlow = true;
        String command;
        Scanner kb = new Scanner(System.in);
        System.out.print("Would you like to create, "
        		         + "append, or display a file?(or use 'exit' to exit): ");
        command = kb.nextLine();
        while (keepFlow = true)
        {
            if (command.equalsIgnoreCase("create"))
            {
        	   createFile();
        	   System.out.print("Would you like to create, "
        	   		            + "append, or display a file?(or use 'exit' to exit): ");
            }
            else if (command.equalsIgnoreCase("append"))
            {
        	   appendFile();
        	   System.out.print("Would you like to create, "
        	   		            + "append, or display a file?(or use 'exit' to exit): ");
            }
            else if (command.equalsIgnoreCase("display"))
            {
        	   displayFile();
        	   System.out.print("Would you like to create, "
        	   		            + "append, or display a file?(or use 'exit' to exit): ");
            }
            else if (command.equalsIgnoreCase("exit"))
            	return;
            else
            {
        	    System.out.print("Invalid command! Please choose "
        			             + "'create', 'append', 'display', or 'exit': ");
            }
            command = kb.nextLine();
        }
    }
    public static void createFile() throws IOException
    {
        String createFilename, filesInput;
        boolean keepFlow = true;
        Scanner kb = new Scanner(System.in);
        System.out.print("Please input your new file name: ");
        createFilename = kb.nextLine();
        File newFile = new File("C:\\Users\\Lance2314\\Desktop\\Text Documents\\" 
                                + createFilename + ".txt");
        if (newFile.exists())
        {
            System.out.println("This file already exists. "
            		+ "If you would like to edit this file, use the 'append' command.");
            return;
        }
        PrintWriter outputFile = new PrintWriter("C:\\Users\\Lance2314\\Desktop\\"
        		                                 + "Text Documents\\" 
                                                 + createFilename + ".txt");
        System.out.println("Please enter data into the file. "
        		           + "Hit the 'Enter' key to stop writing");
        while (keepFlow = true)
        {
        	System.out.print(">> ");
        	filesInput = kb.nextLine();
        	if (filesInput.equals(""))
        		break;
            outputFile.println(filesInput);
        }
        outputFile.close();
        System.out.println("File " + createFilename + ".txt is complete.");
    }
    public static void appendFile() throws IOException
    {
    	boolean keepFlow = true;
        String appendFileName, filesAppend;
        Scanner kb = new Scanner(System.in);
        System.out.print("Please input the file you want to append: ");
        appendFileName = kb.nextLine();
        File openFile = new File("C:\\Users\\Lance2314\\Desktop\\Text Documents\\" 
                + appendFileName + ".txt");
        if (!openFile.exists())
        {
            System.out.println("This file does not exist. "
            		+ "If you would like to creat this file, use the 'create' command.");
            return;
        }
        Scanner inputFile = new Scanner(openFile);
        System.out.println("Currently in " + appendFileName + ".txt: ");
        System.out.println("--------------------------"
        		           + "-----------------------------------"
        		           + "-----------------------------------");
        while(inputFile.hasNext())
        {
            String printing = inputFile.nextLine();
            System.out.println(printing);
        }
        System.out.println("--------------------------"
                		   + "-----------------------------------"
                		   + "-----------------------------------");
        inputFile.close();
        System.out.println("Now please append the text document(Press the 'Enter' key "
        		           + "to stop): ");
        FileWriter oldFile = new FileWriter("C:\\Users\\Lance2314\\Desktop\\Text Documents\\" 
                + appendFileName + ".txt", true);
        PrintWriter olderFile = new PrintWriter(oldFile);
        while (keepFlow = true)
        {
        	System.out.print(">> ");
        	filesAppend = kb.nextLine();
        	if (filesAppend.equals(""))
        		break;
            olderFile.println(filesAppend);
        }
        olderFile.close();
    }
    public static void displayFile() throws IOException
    {
    	boolean keepFlow = true;
        String appendFileName, filesAppend;
        Scanner kb = new Scanner(System.in);
        System.out.print("Please input the file you want to append: ");
        appendFileName = kb.nextLine();
        File openFile = new File("C:\\Users\\Lance2314\\Desktop\\Text Documents\\" 
                + appendFileName + ".txt");
        if (!openFile.exists())
        {
            System.out.println("This file does not exist. "
            		+ "If you would like to creat this file, use the 'create' command.");
            return;
        }
        Scanner inputFile = new Scanner(openFile);
        System.out.println("Currently in " + appendFileName + ".txt: ");
        System.out.println("--------------------------"
        		           + "-----------------------------------"
        		           + "-----------------------------------");
        while(inputFile.hasNext())
        {
            String printing = inputFile.nextLine();
            System.out.println(printing);
        }
        System.out.println("--------------------------"
                		   + "-----------------------------------"
                		   + "-----------------------------------");
        inputFile.close();
    }
}
