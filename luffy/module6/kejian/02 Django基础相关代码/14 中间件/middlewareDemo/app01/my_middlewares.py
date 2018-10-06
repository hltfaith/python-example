

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class CustomerMiddleware(MiddlewareMixin):

    def process_request(self,request):
        print("CustomerMiddleware1 process_request....")

        #return HttpResponse("forbidden....")


    def process_response(self,request,response):
        print("CustomerMiddleware1 process_response")

        return response
        #return HttpResponse("hello yuan")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("CustomerMiddleware1 process_view")


    def process_exception(self, request, exception):

        print("CustomerMiddleware1 process_exception")
        return HttpResponse(exception)




class CustomerMiddleware2(MiddlewareMixin):

    def process_request(self,request):
        print("CustomerMiddleware2 process_request....")

    def process_response(self,request,response):
        print("CustomerMiddleware2 process_response")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        # print("====>",callback(callback_args))
        print("CustomerMiddleware2 process_view")
        # ret=callback(callback_args)
        # return ret

    def process_exception(self, request, exception):

        print("CustomerMiddleware2 process_exception")

        #return HttpResponse(exception)
