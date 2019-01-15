//Java Challenge
//Stock Open Close Price on Particular Weekdays

//Get data from json content and select specific dates with its stock open close data, including json over pages

//example of input
//1-January-2000 22-February-2000 Monday
//{"page":"1","per_page":500,"total":2500,"total_pages":5,"data":[{"date":"5-January-2000","open":5265.09,"high":5464.35,"low":5184.48,"close":5357},{"date":"6-January-2000","open":5424.21,"high":5489.86,"low":5391.33,"close":5421.53},{"date":"7-January-2000","open":5358.28,"high":5463.25,"low":5330.58,"close":5414.48}]}


//example of output
//31-January-2000 5338.67 5205.29


//method main is given


import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.net.*;
import com.google.gson.*;
    


public class Solution {
    /*
     * Complete the function below.
     */
    static void openAndClosePrices(String firstDate, String lastDate, String weekDay) {
        
        Date dt = new Date(firstDate);
        Date n = new Date(lastDate);

        String URL = "https://jsonmock.hackerrank.com/api/stocks/?page=";
        int page = 1;
        String json = callURL(URL + page);

        JsonParser parser = new JsonParser();

        JsonElement jsonTree = parser.parse(json);
        JsonObject jsonObject = jsonTree.getAsJsonObject();

        int total = jsonObject.get("total_pages").getAsInt();
        List<JsonArray> pages = new ArrayList<JsonArray>();

        for (int l = page; l <= total; l++) {
            JsonElement data = jsonObject.get("data");
            pages.add(data.getAsJsonArray());
            page++;
            json = callURL(URL + page);
            jsonTree = parser.parse(json);
            jsonObject = jsonTree.getAsJsonObject();
        }

        for (int j = 0; j < total; j++) {
            JsonArray d0 = pages.get(j);
            for (int i = 0; i < d0.size(); i++) {
                JsonObject dat = d0.get(i).getAsJsonObject();
                String date = dat.get("date").getAsString();
                Date now = new Date(date);
                JsonElement open = dat.get("open");
                JsonElement close = dat.get("close");
                if (checkRangeDate(dt, n, now) && weekDay(weekDay, getDoW(date))) {
                    System.out.println(date + " " + open + " " + close);
                }

            }
        }

        

    }

    public static boolean checkRangeDate(Date d1, Date d2, Date d3) {

        if (d3.compareTo(d2) <= 0 && d3.compareTo(d1) >= 0) {
            return true;
        }

        return false;
    }

    public static int getDoW(String cal) {

        String[] dd = cal.split("-");
        int day = Integer.parseInt(dd[0]);
        int y = Integer.parseInt(dd[2]);
        Date dt = new Date(cal);
        int m = dt.getMonth() + 1;
        Calendar c = new GregorianCalendar(y, m - 1, day);
        return c.get(Calendar.DAY_OF_WEEK);
    }

    public static boolean weekDay(String weekDay, int w) {
        int day = 0;
        switch (weekDay) {
        case "Sunday":
            day = 1;
            break;
        case "Monday":
            day = 2;
            break;
        case "Tuesday":
            day = 3;
            break;
        case "Wednesday":
            day = 4;
            break;
        case "Thursday":
            day = 5;
            break;
        case "Friday":
            day = 6;
            break;
        case "Saturday":
            day = 7;
            break;
        }
        if (day == w) {
            return true;
        }
        return false;
    }

    public static String callURL(String myURL) {
        StringBuilder sb = new StringBuilder();
        URLConnection urlConn = null;
        InputStreamReader in = null;
        try {
            URL url = new URL(myURL);
            urlConn = url.openConnection();
            if (urlConn != null)
                urlConn.setReadTimeout(60 * 1000);
            if (urlConn != null && urlConn.getInputStream() != null) {
                in = new InputStreamReader(urlConn.getInputStream());
                BufferedReader bufferedReader = new BufferedReader(in);
                if (bufferedReader != null) {
                    int cp;
                    while ((cp = bufferedReader.read()) != -1) {
                        sb.append((char) cp);
                    }
                    bufferedReader.close();
                }
            }
            in.close();
        } catch (Exception e) {
            throw new RuntimeException("Exception while calling URL:" + myURL, e);
        }

        return sb.toString();
    }

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        String _firstDate;
        try {
            _firstDate = in.nextLine();
        } catch (Exception e) {
            _firstDate = null;
        }
        
        String _lastDate;
        try {
            _lastDate = in.nextLine();
        } catch (Exception e) {
            _lastDate = null;
        }
        
        String _weekDay;
        try {
            _weekDay = in.nextLine();
        } catch (Exception e) {
            _weekDay = null;
        }
        
        openAndClosePrices(_firstDate, _lastDate, _weekDay);
        
    }
}
