CREATE TABLE IF NOT EXISTS location (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    city_id INTEGER NOT NULL REFERENCES location(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    temperature DECIMAL,
    humidity DECIMAL,
    wind_speed DECIMAL,
    weather_main VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER DEFAULT 1
);


CREATE TABLE IF NOT EXISTS daily_weather_stats (
    id SERIAL PRIMARY KEY,
    report_date DATE NOT NULL,
    city_id INTEGER NOT NULL REFERENCES location(id) ON DELETE CASCADE,
    avg_temp DECIMAL,
    max_wind DECIMAL,
    avg_hum DECIMAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER DEFAULT 1
);

ALTER TABLE daily_weather_stats
ADD CONSTRAINT unique_date_city UNIQUE (report_date, city_id);


CREATE TABLE anomalies (
    id SERIAL PRIMARY KEY,
    city_id INTEGER NOT NULL REFERENCES location(id),
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    current_temp DECIMAL,
    avg_temp_last_7d DECIMAL,
    source_record_id INTEGER REFERENCES weather_data(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER DEFAULT 1
);
