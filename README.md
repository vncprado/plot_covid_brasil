plot_covid_brasil
-----------------

Small project to load a dataset from [Brasil.io](https://brasil.io) and retrieve information regarding a specific city.

Running the Python script you download the datasets `casos.csv.gz`  and `casos_fullcsv.gz` and extract a csv file each.

There is a creation of a csv file with the specific data extracted: number of daily cases and number of total confirmed cases for the hard-coded city.

`test_plot_csv.html` has a small javascript code for plotting the resulted csv.
This page has an online version [here](https://vncprado.githhub.io/pebas/) for the city of Parauapebas, PA, Bazil.

You can test locally the html page using:

    $ python -m SimpleHTTPServer

On this folder and open [`test_plot_csv.html`](http://localhost:8000/test_plot_csv.html) on your browser.

I also included a javascript version that uses the [Brasil.io](https://brasil.io) API and plots a selected city: `test_plot_api.html`.

An online version of this is available [here](https://vncprado.github.io/cidades/)
