from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
import json
from reelsapi import process


def index(request):
    data = {
        "message": "",
    }
    return render(request, "index.html", data)


@api_view(["GET", "POST"])
def fetch_video_data(request):
    # Get the video URL from the request
    url = request.POST.get("url")
    target_url = "API PRIVATE URL" #private api url to download video not available to public,

    # Set the payload for the request
    payload = {"url": url}

    # Make the request to the savefromus API
    response = requests.post(target_url, data=payload)

    # Check the status code of the response
    if response.status_code == 200:
        # If the request was successful, return a success response
        video_data = process.fetch_data(response.content)
        return JsonResponse(video_data, safe=False)
    else:
        # If the request failed, return an error response
        error_message = {"status": "failed"}
        return JsonResponse(error_message)


def response(request):
    # Call fetch_video_data function and get the response
    video_data_response = fetch_video_data(request)
    json_data = process.convert_json(video_data_response.content)
    if json_data['status'] == "success":
        return render(request, "response.html", json_data)
    else:
        data = {
            "message": "invalid instagram url",
        }
        return render(request, "index.html", data)
