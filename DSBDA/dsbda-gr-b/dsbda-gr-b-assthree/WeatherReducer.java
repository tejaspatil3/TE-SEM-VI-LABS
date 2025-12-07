package com.mapreduce.wm;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;

public class WeatherReducer extends Reducer<Text, WeatherDataWritable, Text, Text> {

    public void reduce(Text key, Iterable<WeatherDataWritable> values, Context context) throws IOException, InterruptedException {
        int tempSum = 0, dewSum = 0, windSum = 0, count = 0;

        for (WeatherDataWritable val : values) {
            tempSum += val.getTemperature();
            dewSum += val.getDewPoint();
            windSum += val.getWindSpeed();
            count++;
        }

        int avgTemp = tempSum / count;
        int avgDew = dewSum / count;
        int avgWind = windSum / count;

        Text outputValue = new Text("AvgTemp: " + avgTemp + "°C, AvgDew: " + avgDew + "°C, AvgWind: " + avgWind + " km/h");
        context.write(key, outputValue);
    }
}
