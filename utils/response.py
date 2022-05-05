from rest_framework.response import Response
from rest_framework import status


class EdueResponse(Response):
    SUCCESS = dict(
        status=status.HTTP_200_OK,
        name='success'
    )

    def _init_(self, status, message, data):
        super()._init_(dict(
            status=status,
            message=message,
            data=data if data else {}
        ), status=status)

    @classmethod
    def set_response(cls, response):
        return cls(status=response.get("status"), message=response.get("message"), data=response.get("data"))
