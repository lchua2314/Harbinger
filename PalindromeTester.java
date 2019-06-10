import java.util.Scanner;
public class PalindromeTester 
{
    public static void main(String[] args) 
    {
        String pal="0"; 
        int i, j, counter=0;
        Scanner kb = new Scanner(System.in);
        
        while (!pal.equals(""))
        {
            System.out.println("enter a word, phrase, " 
                               + "or sentence (blank line " 
                               + "to stop): ");
            pal = kb.nextLine().toLowerCase().replaceAll("\\d+","")
        	    .replaceAll("[\\W]", "");
        
            if (pal.equals(""))
            {
                System.out.printf("You found %d "
    			          + "palindromes.\n", counter);
                System.out.println("Thank you for "
    			           + "using PalindromeTester.");
    	        System.exit(0);
            }
        
            i=0; 
            j=pal.length()-1;
            int x = 0;
            int keepFlow;

        	
            while (x==0)
            {           
                if (i==j)
                {
                    System.out.println("palindrome\n");
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
                        System.out.println("palindrome\n");
                        counter++;
                        x++;
                        break;
                    }
                    
                    if (keepFlow==1)
                    {
                        System.out.println("not palindrome\n");
                        x++;
                        break;
                    }
                }
            }
        }   
    }   
}
