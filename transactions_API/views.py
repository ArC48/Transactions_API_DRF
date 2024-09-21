from django.core.paginator import Paginator
from django.http import JsonResponse
from .settings import CSV_FILE_PATH
import csv


def get_transactions(request):
    # get page number from request
    page_number = request.GET.get("page", 1)  # default page num is 1
    page_size = request.GET.get(
        "page_size", 10
    )  # default page_size is 100 records per page

    # Path to the CSV file
    csv_file_path = CSV_FILE_PATH

    # holds the transactions data
    transactions = []

    # read the csv file and store rows in a list
    with open(csv_file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        transactions = list(reader)

    # paginate the results
    paginator = Paginator(transactions, page_size)
    page = paginator.get_page(page_number)

    return JsonResponse(
        {
            "total_records": paginator.count,
            "total_pages": paginator.num_pages,
            "current_page": page.number,
            "records": page.object_list,
        }
    )
