from django.core.paginator import Paginator
from .settings import CSV_FILE_PATH
from collections import defaultdict
from rest_framework.response import Response
from .serializers import TransactionSerializer, PurchaseSerializer
from rest_framework.decorators import api_view
import csv


# to read a specific chunk of rows from the CSV
def read_csv_chunk(file_path, start_row, end_row):
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            if i < start_row:
                continue
            if i >= end_row:
                break
            yield row


# GET all transactions data
@api_view(["GET"])
def get_transactions(request):
    # get page number from request
    page_number = request.GET.get("page", 1)  # default page num is 1
    page_size = request.GET.get(
        "page_size", 10
    )  # default page_size is 10 records per page

    # Path to the CSV file
    csv_file_path = CSV_FILE_PATH

    start_row = (page_number) * page_size
    end_row = start_row + page_size

    # holds the transactions data
    transactions = list(read_csv_chunk(csv_file_path, start_row, end_row))

    serialized_data = TransactionSerializer(transactions, many=True).data

    return Response(
        {
            "total_records": len(transactions),
            "current_page": page_number,
            "records": serialized_data,
        }
    )


# GET user purchases by their ids
@api_view(["GET"])
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

    serialized_data = PurchaseSerializer(page.object_list, many=True).data
    return Response(
        {
            "total_records": paginator.count,
            "total_pages": paginator.num_pages,
            "current_page": page.number,
            "records": serialized_data,
        }
    )


# Get product purchase info by their unique code
@api_view(["GET"])
def product_purchases(request, item_code):
    page_number = request.GET.get("page", 1)
    page_size = request.GET.get("page_size", 10)

    csv_file_path = CSV_FILE_PATH
    purchases_by_date = defaultdict(int)

    with open(csv_file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # filter by item_code
            if int(row["ItemCode"]) == item_code:
                date = row["TransactionTime"]
                total_items = int(row["NumberOfItemsPurchased"])
                purchases_by_date[date] += total_items

    purchase_list = [
        {"date": transaction_time, "total_items": total}
        for transaction_time, total in purchases_by_date.items()
    ]

    paginator = Paginator(purchase_list, page_size)
    page = paginator.get_page(page_number)

    serialized_data = PurchaseSerializer(page.object_list, many=True).data

    return Response(
        {
            "total_records": paginator.count,
            "total_pages": paginator.num_pages,
            "current_page": page.number,
            "records": serialized_data,
        }
    )
