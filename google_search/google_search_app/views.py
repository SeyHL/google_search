from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.http import FileResponse
import os
from serpapi import GoogleSearch
import csv
from dotenv import load_dotenv

# Create your views here.
def home(request):
    return render(request, "pages/home.html")

def result(request):
    # Gets user keyword and assigns value to the variable
    keyword = request.GET.get("searchKeyword")
    # Loads variables from .env file into the environment
    current_directory = os.path.dirname(os.path.realpath(__file__))
    dotenv_path = os.path.join(current_directory, ".env")
    load_dotenv(dotenv_path)
    # Sets search parameters
    params = {
    "api_key": os.getenv("SERPAPI_KEY"),
    "q": keyword,
    "page": 1
    }

    # Search on Google
    search = GoogleSearch(params)
    result = search.get_dict()

    # Sets variable for creating dictionary
    title_list = []
    link_list = []
    results_dict = []

    # Selects organic results
    for organic_result in result.get("organic_results", []):
        title = organic_result.get("title", "")
        link = organic_result.get("link", "")

        # Creates final result displayed on result page
        final_result =""
        title_list.append(title)
        link_list.append(link)
        for t_list, l_list in zip(title_list, link_list):
            one_result = f"Title: {t_list}\n Link: {l_list}\n\n"
            final_result = final_result + one_result
        
        # Creates dictionary in order to use it for csv file creation
            result_dict = {"Title": t_list, "Link": l_list}
            results_dict.append(result_dict)

        request.session["dictionary"] = results_dict

    return render(request, "pages/result.html", {"yourResult": final_result, "yourKeyword": keyword})

def download(request):
    # Creates csv file from dictionary
    results_dict = request.session["dictionary"]
    fields = ["Title", "Link"]
    with open("results.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        for row in results_dict:
            writer.writerow(row)

    # Downloads results.csv file
    return FileResponse(open('results.csv', 'rb'), as_attachment=True)

def successful_download(request):
    return render(request, "pages/successful_download.html")
        



