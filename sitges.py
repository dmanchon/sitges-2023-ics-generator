import requests
from ics import Calendar, Event
import arrow


def main():
    url = "https://sitgesfilmfestival.com/ca/service/films/2023"
    r = requests.get(url)
    body = r.json()
    c = Calendar()

    locations = {l["id"]: l["name"]["es"] for l in body["locations"]}
    films = {f["id"]: f for f in body["films"]}
    for session in body["sessions"]:

        e = Event()
        name = session["name"]["en"]
        e.name = name
        
        # Shift time to match Sitges timezone
        e.begin = arrow.get(session["start_date"]).shift(hours=-2)
        e.end = arrow.get(session["end_date"]).shift(hours=-2)
        e.location = locations[session["locations"][0]]
        e.uid = session["id"]

        desc = ""
        if "films" in session:
            for f_id in session["films"]:
                film = films[f_id]
                desc = f"""{desc}<a href="https://sitgesfilmfestival.com{film["url"]["en"]}">{name}</a>\n"""
        
                desc = f"""{desc}\n<p>{film["synopsis"]["en"]}</p>"""
        e.url = f"https://sitgesfilmfestival.com/{url}"

        e.description = desc
        c.events.add(e)

    with open('sitges.ics', 'w') as my_file:
        my_file.writelines(c.serialize_iter())
    

if __name__ == "__main__":
    main()
