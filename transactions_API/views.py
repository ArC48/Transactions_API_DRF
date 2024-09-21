from django.core.paginator import Paginator
from django.http import JsonResponse
from .settings import CSV_FILE_PATH
from collections import defaultdict
import csv


# GET all transactions data
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


# GET user purchases by their ids
def user_purchases(request, user_id):
    page_number = request.GET.get("page", 1)
    page_size = request.GET.get("page_size", 10)

    csv_file_path = CSV_FILE_PATH

    purchases_by_date = defaultdict(int)

    with open(csv_file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # filter data by user_id
            if int(row["UserId"]) == user_id:
                date = row["TransactionTime"]
                total_items = int(row["NumberOfItemsPurchased"])
                purchases_by_date[date] += total_items

    purchase_list = [
        {"date": transaction_time, "total_items": total}
        for transaction_time, total in purchases_by_date.items()
    ]

    paginator = Paginator(purchase_list, page_size)
    page = paginator.get_page(page_number)

    return JsonResponse(
        {
            "total_records": paginator.count,
            "total_pages": paginator.num_pages,
            "current_page": page.number,
            "records": page.object_list,
        }
    )
