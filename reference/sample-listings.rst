Sample listings table
=====================

The format I used to give the agent its listings. Prices are in US dollars per night, as shown on the Tubayo homepage on 1 November 2026.

.. warning::

   This table is incomplete. It comes from my homepage screenshots only. It does not include listings on the See more pages, and it does not include MiniPalais Bukoto, which Tubayo's own assistant named at USD 27 but which I could not find in my screenshots. Some area names are cut off in my screenshots, and I could not confirm every listing is in Kampala. Check every row against the live site before you rely on it.

.. csv-table::
   :header: "Name", "Type", "Area", "Price per night (USD)", "Breakfast"
   :widths: 28, 14, 28, 15, 15

   "Grand Plaza Hotel", "Hotel", "Luzige Road, Kampala", "43", "Included"
   "Forest Cottages", "Hotel", "Naguru Hill", "73", "Included"
   "Millennium Terrace Hotel", "Hotel", "Bukoto Street", "90", "Included"
   "Urban By Cityblue", "Hotel", "Akii Bua Road", "124", "Included"
   "The Athena Hotel", "Hotel", "Faraday Road", "147", "Included"
   "Cassia Lodge", "Hotel", "Buziga Hill", "148", "Included"
   "Golden Tulip Canaan", "Hotel", "Kafu Road", "158", "Included"
   "Protea Hotel by Marriott", "Hotel", "Elgon Terrace", "186", "Included"
   "Bibi Homes", "Entire house", "Kyanja Ring Road", "34", "Not stated"
   "Talpaville", "Entire house", "Naalya", "34", "Not stated"
   "Talpa Residences", "Entire house", "Malaba Road area", "34", "Not stated"
   "Bukoto Kisasi Apartments 1", "Entire house", "Bukoto Kisasi Road", "43", "Not stated"
   "Haven Homes", "Entire house", "Ntinda", "45", "Not stated"
   "Rutuha Homes 2", "Entire house", "Kisaasi, Kyanja Road", "51", "Not stated"
   "Skylar Homes", "Entire house", "Kanyankole Trading Centre", "68", "Not stated"
   "Remy Bb", "Apartment", "Kigali, Rwanda", "57", "Not stated"

Why each column is there
------------------------

* **Name and area** let the agent match a traveler's place names.
* **Type** lets it separate hotels from homes.
* **Price per night** lets it filter by budget without converting currencies.
* **Breakfast** is a filter travelers use, so it needs its own column. "Not stated" means the card did not say, not that breakfast is excluded.
