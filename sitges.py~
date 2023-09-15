import requests
from ics import Calendar, Event

def main():
    url = "https://sitgesfilmfestival.com/ca/service/films/2023"
    r = requests.get(url)
    body = r.json()
    c = Calendar()

    for session in body["sessions"]:

        e = Event()
        e.name = session["name"]["en"]
        e.begin = session["start_date"]
        e.end = session["end_date"]
        e.location = body["locations"][0]["name"]["es"]
        e.uid = session["id"]
        c.events.add(e)

    with open('sitges.ics', 'w') as my_file:
        my_file.writelines(c.serialize_iter())
    

if __name__ == "__main__":
    main()
