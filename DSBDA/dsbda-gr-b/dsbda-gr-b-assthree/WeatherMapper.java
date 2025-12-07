package com.mapreduce.wm;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

public class WeatherMapper extends Mapper<Object, Text, Text, WeatherDataWritable> {

    private Text location = new Text();
    private WeatherDataWritable weatherData = new WeatherDataWritable();

    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] fields = line.split(",");

        if (fields.length >= 5 && !fields[0].equalsIgnoreCase("City")) { // Skip header
            location.set(fields[0].trim()); // City
            int temperature = Integer.parseInt(fields[2].trim());
            int dewPoint = Integer.parseInt(fields[3].trim());
            int windSpeed = Integer.parseInt(fields[4].trim());

            weatherData = new WeatherDataWritable(temperature, dewPoint, windSpeed);

            context.write(location, weatherData);
        }
    }
}

