"""
Create a map of the voting/polling stations in NYC.
Uses folium, which has to be installed with "pip install folium"
Folium creates a web page with a map on it.
We use the webbrowser module to open the web browser to the map web page
"""

import csv
from pathlib import Path
import webbrowser
import folium  # must be installed!


def main():
    # make this path work on all computer operating systems.
    filepath = Path("data/Voting_Poll_Sites_20250618.csv").resolve()
    f = open(filepath, mode="r", encoding="utf-8")

    # create a list of the lines in the file where each line is converted to a Python dictionary
    reader = csv.DictReader(f)

    # create a map using folium
    nyc_center_point = (40.71427, -74.00597)  # center on NYC's center (or so we say)
    m = folium.Map(location=nyc_center_point, zoom_start=12)

    # iterate line by line through the file
    for line in reader:
        # get the geospatial (latitude, longitude) from the Dictionary that represents this line
        location = line["Location"]  # a string in the format, "(40.755951, -73.799746)"

        # check that the location exists and is valid
        if location != "" and "(" in location and ")" in location and "," in location:

            # break up the location string into the two parts
            parts = location.split(",")  # break up by comma
            lat = parts[0]  # grab the first value
            lat = lat.replace("(", "")  # remove the parentheses
            long = parts[1]  # grab the second value
            long = long.replace(")", "")  # remove the parentheses
            location = [
                float(lat),
                float(long),
            ]  # put location back together into a list

            # create the text that will appear when a user clicks on the map marker
            # this includes HTML code to format the text in a way that works on the web page...
            popup_text = f"""
    <h2>{line["SITE_NAME"]}</h2>
    <p>
        {line["NTA"]}
    </p>
    <address>
        {line["STREET_NUMBER"]} {line["STREET_NAME"]} <br />
        {line["CITY"]}, NY {line["POSTCODE"]}
    </address>
    """

            # add a marker to the map for this location
            folium.Marker(
                location=location,
                tooltip=line["SITE_NAME"],
                popup=popup_text,
                icon=folium.Icon(icon="person-booth", prefix="fa"),
            ).add_to(m)

        # print to console
        print(location)

    # save the map to an HTML file so we can open it in a web browser
    filepath = Path("output/index.html").resolve()  # platform-agnostic file path
    m.save(filepath)

    # now go and open the index.html file in your web browser
    webpage_path = f"file:///{str(filepath)}"  # browser-friendly path to file
    webbrowser.open(webpage_path, new=True, autoraise=True)


# run the main function if running this file directly
if __name__ == "__main__":
    main()
