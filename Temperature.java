package AlphaTest;

import java.text.DecimalFormat;
import java.util.Scanner;
public class Temperature
{
    private double degrees;
    private String scale;
    public Temperature()
    {
        degrees = 0.0;
        scale = "C";
    }
    public Temperature(double d)
    {
        degrees = d;
        scale = "C";
    }
    public Temperature(String s)
    {
        degrees = 0.0;
        scale = s;
    }
    public Temperature(double d, String s)
    {
        degrees = d;
        scale = s;
    }
    public double getValue()
    {
        return degrees;
    }
    public String getScale()
    {
        return scale;
    }
    public double getFahrenheit()
    {
        double degreesF, reTest;
        double degreesC = degrees;
        degreesF = (degreesC *9 /5) + 32;
        DecimalFormat df = new DecimalFormat("###.#");
        reTest = Double.parseDouble(df.format(degreesF));
        return reTest;
    }
    public double getCelcius()
    {
        double degreesC, reTest;
        double degreesF = degrees;
        degreesC = (degreesF - 32) *5 /9;
        DecimalFormat df = new DecimalFormat("###.#");
        reTest = Double.parseDouble(df.format(degreesC));
        return reTest;
    }
    public void setValue(double d)
    {
        degrees = d;
    }
    public void setScale(String s)
    {
    	Scanner kb = new Scanner(System.in);
        while (!s.equals("F") && !s.equals("f") && !s.equals("C") && !s.equals("c"))
        {
        	System.out.println("invalid scale");
        	s = kb.nextLine();
        }
        scale = s;
    }
    public void setBoth(double d, String s)
    {
    	Scanner kb = new Scanner(System.in);
        degrees = d;
        while (!s.equals("F") && !s.equals("f") && !s.equals("C") && !s.equals("c"))
        {
        	System.out.println("invalid scale");
        	s = kb.nextLine();
        }
        scale = s;
    }
    public boolean checkEquals(Temperature other)
    {
    	if (getScale() == "F" || other.getScale() == "F")
    	{
    		double first, second;
    	    if (getScale() == "F" && other.getScale() == "F")
    	    {
    	        first = getCelcius();
    	        second = other.getCelcius();
    	        if (first == second)
    	           return true;
    	        else
    	           return false;
    	    }
    	    if (getScale() == "F" && other.getScale() == "C")
    	    {
    	        first = getCelcius();
    	        second = getValue();
    	        if (first == second)
    	           return true;
    	        else
    	           return false;
    	    }
    	    if (getScale() == "C" && other.getScale() == "F")
    	    {
    	        first = getValue();
    	        second = other.getCelcius();
    	        if (first == second)
    	           return true;
    	        else
    	           return false;
    	    }
    	}
        if (getValue() == other.getValue())
           return true;
        else
           return false;
    }
    public boolean checkGreaterThan(Temperature other)
    {
    	if (getScale() == "F" || other.getScale() == "F")
    	{
    		double first, second;
    	    if (getScale() == "F" && other.getScale() == "F")
    	    {
    	        first = getCelcius();
    	        second = other.getCelcius();
    	        if (first > second)
    	           return true;
    	        else
    	           return false;
    	    }
    	    if (getScale() == "F" && other.getScale() == "C")
    	    {
    	        first = getCelcius();
    	        second = getValue();
    	        if (first > second)
    	           return true;
    	        else
    	           return false;
    	    }
    	    if (getScale() == "C" && other.getScale() == "F")
    	    {
    	        first = getValue();
    	        second = other.getCelcius();
    	        if (first > second)
    	           return true;
    	        else
    	           return false;
    	    }
    	}
        if (getValue() > other.getValue())
           return true;
        else
           return false;
    }
    public boolean checkLessThan(Temperature other)
    {
    	if (getScale() == "F" || other.getScale() == "F")
    	{
    		double first, second;
    	    if (getScale() == "F" && other.getScale() == "F")
    	    {
    	        first = getCelcius();
    	        second = other.getCelcius();
    	        if (first < second)
    	           return true;
    	        else
    	           return false;
    	    }
    	    if (getScale() == "F" && other.getScale() == "C")
    	    {
    	        first = getCelcius();
    	        second = getValue();
    	        if (first < second)
    	           return true;
    	        else
    	           return false;
    	    }
    	    if (getScale() == "C" && other.getScale() == "F")
    	    {
    	        first = getValue();
    	        second = other.getCelcius();
    	        if (first < second)
    	           return true;
    	        else
    	           return false;
    	    }
    	}
         if (getValue() < other.getValue())
            return true;
         else
            return false;
    }
}


