import requests
import selectorlib
import folium
import streamlit as st
from streamlit_folium import st_folium
urls = ["https://volcano.oregonstate.edu/volcano_table", "https://volcano.oregonstate.edu/volcano_table?page=1",
        "https://volcano.oregonstate.edu/volcano_table?page=2"]


def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tours']

    def split_list(lst, chunk_size):
        return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

    chunk_size = 6
    chunks = split_list(value, chunk_size)
    return chunks


def color_detector(height):
    height = int(height)
    if height < 1000:
        color = "green"
    elif 1000 < height <= 3000:
        color = "orange"
    elif height > 3000:
        color = "red"
    return color


if __name__ == "__main__":
    st.title("Volcano Table")


    all_volcanoes = []
    for page in urls:
        volcanoes_from_page = extract(scrape(page))
        all_volcanoes += volcanoes_from_page

    map = folium.Map(zoom_start=10)

    for volacno in all_volcanoes:
        if all([i != "" for i in volacno]):
            folium.Marker(location=[volacno[3], volacno[4]], popup=volacno[0],
                                       icon=folium.Icon(color=color_detector(volacno[5]))).add_to(map)
    st_data = st_folium(map, width=700)
    # map.save("VOLCANOES.html")
