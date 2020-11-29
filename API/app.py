from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
        )

@app.route("/api/v1.0/precipitation")
 # Convert the query results to a dictionary using date as the key and prcp as the value
    session = Session(engine)

    all_prcp = []
    for prcp in results:
        prcp_dict = {}
        prcp_dict["prcp"] = name
        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)

@app.route("/api/v1.0/stations")
 # Return a JSON list of stations from the dataset
    session = Session(engine)

    station_list = {}
    

    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
 # Query the dates and temperature observations of the most active station for the last year of data
 # Return a JSON list of temperature observations (TOBS) for the previous year
    session = Session(engine)

    Last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    Last_data_point = dt.date(2017,8,23) - dt.timedelta(days=365)
    print(Last_data_point)

    pcp_scores = session.query(Measurement.station,Measurement.tobs).filter(Measurement.station>Last_data_point).order_by(Measurement.station).all()


    pcp_df = pd.DataFrame(pcp_scores, columns = ["Station", "Temperature"])

    return jsonify(pcp_df)

@app.route("/api/v1.0/<start>") ("/api/v1.0/<start>/<end>")
 # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    # When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    # When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    session = Session(engine)

    session.query(Measurement.tobs).filter(Measurement.station=='USC00519281').order_by(Measurement.tobs).first()
    session.query(Measurement.tobs).filter(Measurement.station=='USC00519281').order_by(Measurement.tobs.desc()).first()
    session.query(Measurement.tobs, func.mean(Measurement.tobs)).group_by(Measurement.station=='USC00519281').order_by(func.mean(Measurement.tobs))

    
    return jsonify(session)

if __name__ == '__main__':
    app.run(debug=True)

