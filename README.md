plot_covid_brasil
-----------------

Small project to load a dataset from [Brasil.io](brasil.io) and retrieve information regarding a specific city.

Running the Python script you download the datasets `casos`  and `casos_full` and extract a csv file.
There is a creation of a csv file with the specific data extracted: number of daily cases and number of total confirmed cases

`test_plot_csv.html` with a small javascript code for plotting.
This page has an online version [here](vncprado.githhub.io/pebas/) for the city of Parauapebas, PA, Bazil.

You can test the online html page using:

    $ python -m SimpleHTTPServer

On this folder and open [`test_plot_csv.html`](localhost:8000/test_plot_csv.html) on your browser.

I also included a javascript version that uses the [Brasil.io](brasil.io) API and plots a selected city: `test_plot_api.html`.

An online version of this is available [here](vncprado.github.io/cidades/)
