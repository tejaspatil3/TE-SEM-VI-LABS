package com.mapreduce.wm;

import org.apache.hadoop.io.Writable;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

public class WeatherDataWritable implements Writable {
    private int temperature;
    private int dewPoint;
    private int windSpeed;

    public WeatherDataWritable() {}

    public WeatherDataWritable(int temperature, int dewPoint, int windSpeed) {
        this.temperature = temperature;
        this.dewPoint = dewPoint;
        this.windSpeed = windSpeed;
    }

    public void write(DataOutput out) throws IOException {
        out.writeInt(temperature);
        out.writeInt(dewPoint);
        out.writeInt(windSpeed);
    }

    public void readFields(DataInput in) throws IOException {
        temperature = in.readInt();
        dewPoint = in.readInt();
        windSpeed = in.readInt();
    }

    public int getTemperature() { return temperature; }
    public int getDewPoint() { return dewPoint; }
    public int getWindSpeed() { return windSpeed; }
}

