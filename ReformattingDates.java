//Java Challenge
//convert dates list format from '6th Jun 1933' to '1933-06-06'

//example of input
//10
//26th Dec 2061
//4th Nov 2030
//28th Jul 1963

//example of output
//2061-12-26
//2030-11-04
//1963-07-28

//complete ReformateDate method with an array ouput like ["2061-12-26","2030-11-04","1963-07-28"]
//Solution method was given



import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;


import java.time.format.DateTimeFormatter;
import java.time.temporal.TemporalAccessor;
import java.time.temporal.ChronoField;

class Result {

    /*
     * Complete the 'reformatDate' function below.
     *
     * The function is expected to return a STRING_ARRAY.
     * The function accepts STRING_ARRAY dates as parameter.
     */

    public static List<String> reformatDate(List<String> dates) {
        List<String> out = dates;
        for (int i = 0; i < dates.size(); i++){
            String wd = dates.get(i);
            if (wd.length() == 12) {
                wd = " " + wd;
            }
            String day = wd.substring(0, 2).replaceAll(" ", "0");

            String y = wd.substring(9, 13);

            String m = wd.substring(5, 8);

            DateTimeFormatter parser = DateTimeFormatter.ofPattern("MMM");
            TemporalAccessor accessor = parser.parse(m);
            m = String.valueOf(accessor.get(ChronoField.MONTH_OF_YEAR));
            if (m.length() == 1){
                m = "0" + m;
            }

            out.set(i,y + "-" + m + "-" + day);

        }
        return out;

        

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int datesCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> dates = IntStream.range(0, datesCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .collect(toList());

        List<String> result = Result.reformatDate(dates);

        bufferedWriter.write(
            result.stream()
                .collect(joining("\n"))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}
